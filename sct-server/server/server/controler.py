"""
This module is ...
"""
import collections
import importlib
import logging
import os
import pkgutil
import psutil
import platform
import queue
import operator
import shutil
import subprocess
import signal
import sys
import time
import threading
import uuid

import jsonpickle
from sqlalchemy.exc import SQLAlchemyError

try:
    from .models import models
    from . import cfg
except SystemError:
    from models import models
    import cfg

# @TODO Write doc
# @TODO register plugins from there spinalcordtoolbox directory

__author__ = 'Pierre-Olivier Quirion <pioliqui@gmail.com>'


class PluginUpdater(object):
    def __init__(self, script_path, config=None, session=None, reload=False):

        if config:
            self.session = config.registry.dbmaker()
        else:
            self.session = session
        # self.script_path = script_path
        # plugin_list = self._load_old_plugins(config)
        plugin_list = self._load_plugins(config, script_path, reload=reload)
        self.rebuild_table(plugin_list)

    def rebuild_table(self, plugin_list):
        """
        Update exiting plugins, add new ones and remove others
        :param plugin_list:
        :return:
        """
        # remove old plugins
        try:
            self.session.query(models.RegisteredTool).delete()
            self.session.add_all(plugin_list)
            self.session.commit()
        except SQLAlchemyError:
            self.session.rollback()


    def _load_plugins(self, config, script_path, reload=False):

        # all_script = os.listdir(script_path)
        if reload or not os.path.isdir(cfg.EXEC_TMP):
            shutil.rmtree(cfg.EXEC_TMP, ignore_errors=True)
            def ignore(src, names):
                    return [name for name in names if "pyc" in name]
            shutil.copytree(script_path, cfg.EXEC_TMP, ignore=ignore)
            #subprocess.call(["/usr/bin/env", "2to3-3.4",  "-w", cfg.EXEC_TMP])
            subprocess.call(["/usr/bin/env", "2to3",  "-w", cfg.EXEC_TMP]) #DEBUG

        modules = pkgutil.iter_modules([cfg.EXEC_TMP])
        sys.path.insert(0, "{}/../".format(cfg.EXEC_TMP))
        sys.path.insert(0, "{}/".format(cfg.EXEC_TMP))
        importlib.__import__(cfg.SCT_TMP_PKG, globals(), locals(), [], 0)
        sct_tools = []
        for loader, mod_name, ispkg in modules:
            module = importlib.import_module('.'+mod_name, package=cfg.SCT_TMP_PKG)
            get_parser = getattr(module, cfg.GET_PARSER, None)
            if get_parser:
                parser = get_parser()
                options = {}
                for i, o in enumerate(parser.options.values()):
                    if not getattr(o, cfg.OPTION_DEPRECATED, None):
                        options.update({o.name: {k: v for k, v in o.__dict__.items()
                                                 if k in cfg.OPTION_TRANSMIT}})
                        #add a value key for user parameters
                        options[o.name]['value']=None
                        #add section handling
                        parser.usage.section[1] = "Main Config"
                        x = parser.usage.section
                        sorted_x = sorted(x.items(), key=operator.itemgetter(0))
                        for i in sorted_x:
                            if options[o.name]['order'] >= i[0]:
                                options[o.name]['section'] = i[1]

                # options.sort(key=lambda e: e[cfg.OPTION_ORDER])
                sct_tools.append(models.RegisteredTool(name=mod_name,
                                                       help_str=parser.usage.description,
                                                       options=options))

        return sct_tools


    def _load_old_plugins(self, config):

        path = cfg.OLD_TYPE_JSON
        list_path = os.path.join(path, 'liste_scripts.json')
        config_path = os.path.join(path, 'config')
        with open(list_path) as fp:
            tool_list = json.load(fp)

        rtools = []
        for script in tool_list:
            if script['activateScript']:
                name = script['title']
                help_str = 'no help yet'
                section = 'no section here'
                cfg_path = os.path.join(config_path, name + '_config.json')
                if not os.path.isfile(cfg_path):
                    continue
                with open(cfg_path) as fp:
                    options = json.load(fp)[0]
                rtools.append(models.RegisteredTool(name=name, help_str=help_str,section=section, options=options))

        return rtools


def get_platform():
    """
    TODO ADD windows support
    :return: platform name
    """
    if "linux" in platform.platform().lower():
        return "linux"
    else:
        return "osx"




class ToolboxRunner(object):
    """
    Class that can be used to execute script
    @TODO write a parent class that could be used to build runner
    for other software (niak)
    @TODO Have the process run by a worker, not right in the server!
    """

    def __init__(self, register_tool: models.RegisteredTool,
                 bin_dir: str, process_uid=None, user_id= None):

        self.rt = register_tool

        self.cancel = False
        self._activity = {}
        self._timeout_once_done = cfg.TIMEOUT

        self.fill_cmd_template = {
            cfg.EXEC_DIR_TAG: bin_dir}

        self.process_uid = process_uid if process_uid else uuid.uuid1()


        self.completion_time = 0
        self.process_is_done = False
        self.stdout_is_close = False
        self.child = None
        self.stdout = None
        self.user_id = user_id



    def toolbox_env(self):
        """
        @TODO could be worth it to clean the env var to be minimal
        :return:
        """

        SCT_DIR= cfg.SPINALCORDTOOLBOX

        PATH=[cfg.SPINALCORD_BIN]

        PATH.append("{}/{}".format(cfg.SPINALCORD_BIN,get_platform()))

        PYTHONPATH="{}/scripts".format(cfg.SPINALCORDTOOLBOX)

        all_env = os.environ

        all_env["PATH"] = ":".join(PATH) + ":" + all_env["PATH"]+":"+cfg.PATHFSLBIN
        all_env["PYTHONPATH"] = PYTHONPATH
        all_env["SCT_DIR"] = SCT_DIR

        return all_env


    def run_blocking(self):
        """
        Running mechanism that lock until the process ends
        :return:
        """

        cmd = self.rt.cmd.format(**self.fill_cmd_template)
        logging.info('Executing {0}'.format(cmd))
        #cmd = "python2.7 " + cmd #@todo: fix that to be more flexible DEBUG
        cmd = cmd #@todo: fix that to be more flexible
        child = subprocess.Popen(cmd.split(' '),
                                 stderr=subprocess.STDOUT,
                                 stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 bufsize=1,
                                 env=self.toolbox_env())

        completion_time = 0
        process_is_done = False
        stdout_is_close = False
        interrupt_the_process = False

        stdout_queue = queue.Queue()
        stdout_monitor_thread = threading.Thread(
            target=self.read_from_stream,
            args=(child.stdout, self._activity, stdout_queue, True),
            )

        stdout_monitor_thread.daemon = True
        stdout_monitor_thread.start()

        # stdout_lines = []
        while not (process_is_done or stdout_is_close):

            now = time.time()

            # We need to cancel the processing!
            if self.cancel:
                logging.info('The execution needs to be stopped.')
                break

            # If the subprocess is dead/done, we exit the loop.
            if child.poll() is not None:
                logging.info("Subprocess is done.")
                process_is_done = True

            # Once the process is done, we keep
            # receiving standard out/err up until we reach the done_timeout.
            if (completion_time > 0) and (self._timeout_once_done > 0) and (now - completion_time > self._timeout_once_done):
                logging.info("Done-timeout reached.")
                break

            # TODO Check if that is really necessary
            # If there is nothing received from child process, either from the
            # standard output or the standard error streams, past a given amount
            # of time, we assume that the sidekick is done/dead.
            # if (self.inactivity_timeout > 0) and (now - self._activity['last'] > self.inactivity_timeout):
            #     logging.info("Inactivity-timeout reached.")
            #     break

            # Handle the standard output from the child process
            if not child.stdout:
                # while not stdout_queue.empty():
                #     stdout_lines.append(stdout_queue.get_nowait())
            # else:
                interrupt_the_process = False
                stdout_is_close = True
                process_is_done = True

            # Start the countdown for the done_timeout
            if process_is_done and not completion_time:
                completion_time = now

            # Sleep a bit to avoid using too much CPU while waiting for execution to be done.
            time.sleep(cfg.PROCESS_LOOP_SLEEP)

        return_code = child.poll()

        if return_code is None:

            if interrupt_the_process:
                logging.info("The child process is running (PID {0}). Sending it an interrupt signal..."
                             .format(child.pid))
                child.send_signal(signal.SIGTERM)


            # Let the subprocess die peacefully...
            time_to_wait = cfg.PEACEFUL_DEAD_CLOCK
            while time_to_wait > 0 and child.poll() is None:
                time.sleep(0.1)
                time_to_wait -= 0.1

            # Force the process to die if it's still running.
            return_code = child.poll()
            if return_code is None:
                logging.info("The child process is still running (PID {}). Sending it a kill signal..."
                             .format(child.pid))
                self.force_stop(child)

        return_code = child.poll()
        if return_code == 0:
            logging.error("The process has exited with a non-zero return code: {}".format(return_code))
        else:
            logging.info("The process was completed and returned 0 (success)")

        return return_code

    def run(self):
        """
        Running mechanism that return stderr and stdout
        :return:
        """

        cmd = self.rt.cmd.format(**self.fill_cmd_template)
        logging.info('Executing {0}'.format(cmd))
        cmd = cfg.PYHTON_NAME + cmd #@todo: fix that to be more flexible
        self.child = subprocess.Popen(cmd.split(' '),
                                 stderr=subprocess.STDOUT,
                                 stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 bufsize=1,
                                 env=self.toolbox_env())


        self.stdout_queue = queue.Queue()
        stdout_monitor_thread = threading.Thread(
            target=self.read_from_stream,
            args=(self.child.stdout, self._activity, self.stdout_queue, True),
            )

        stdout_monitor_thread.daemon = True
        stdout_monitor_thread.start()
        # add the process and log to the registry

        SCTLog.register_process(self.user_id, self.process_uid,  self)

        # stdout_lines = []


    def check_status(self):

        now = time.time()


        retcode = self.child.poll()
        if retcode is not None:
            logging.info("Subprocess is done.")
            self.process_is_done = True

        # Handle the standard output from the child process
        if not self.child.stdout:
            self.stdout_is_close = True
            self.process_is_done = True

        # Start the countdown for the done_timeout
        if self.process_is_done and not self.completion_time:
            self.completion_time = now

        return retcode



    def interupt_child(self):
        self.force_stop(self.child.pid)

    @staticmethod
    def read_from_stream(stream, activity, std_queue=None, echo=False):
        for line in iter(stream.readline, b''):
            if std_queue:
                std_queue.put(line)
            activity['last'] = time.time()
            if echo:
                sys.stderr.write(line.decode('utf-8'))
                # logging.info(line.decode('utf-8'))
        stream.close()

    @staticmethod
    def force_stop(sub_proc, including_parent=True):
        """
        Stops the execution of process and of its children
        :param sub_proc a process with a pid attribute:
        :param including_parent:
        :return:
        """
        parent = psutil.Process(sub_proc.pid)
        logging.info("Killing the sub-processes using psutil.")
        for child in parent.children(recursive=True):
            child.kill()
        if including_parent:
            parent.kill()


class SCTLog(object):
    """ Store and retrieve information about a toolbox subprocess

        This class is somehow dangerous since it keeps growing and growing
        The garbage_collect method should be called in the server periodically
        TODO: Store the info in a database
    """

    _registered_process = {}

    def __init__(self, uid):

        self.uid = int(uid)

        if self._registered_process.get(self.uid):
            self._tr = self._registered_process.get(self.uid)[0]
            self._data = self._registered_process.get(self.uid)[1]
        else:
            raise LookupError('Process {} does not exist'.format(self.uid))


    @classmethod
    def register_process(cls, uid, pid, runner):
        """ Add new process info to the class

        :param pid: the process id
        :param uid: the user id
        :param runner: a runner object
        :return: cls(uid)
        """

        data = collections.defaultdict(list)
        data['registration_Time'] = time.time()
        # if cls._registered_process.get(uid):
        #     raise KeyError("process already registered{}".format(uid)) ## DEBUG
        cls._registered_process[int(uid)] = (runner, data)

        return cls(uid)

    @classmethod
    def all_uid(cls):
        return cls._registered_process.keys()

    def log_tail(self, maxline=1):
        """ Used to get a log feed line
        :maxline: maximjum number on line returned
        :return: new log line
        """
        nline = 0
        lines = []
        while not self._tr.stdout_queue.empty() and nline < maxline:
            lines.append(self._tr.stdout_queue.get_nowait())
            self._data['processed'].append(lines[-1])
            nline += 1
        return lines

    def old_log(self):
        """
        :return: all previously logged data
        """
        return self._data.get('processed')

    def running(self):
        """
        :return: True if process still running Flase otherwise
        """
        return self._tr.child.poll()

    def kill_process(self):
        self._tr.interupt_child()

    @classmethod
    def garbage_collect(cls):
        """
        This is the poor man's garbage collector
        :return:
        """
        for key, process in cls._registered_process.items():
            one_day = 86400
            if (time.time() - process[2]['registration_Time']) > one_day and not process[1]:
                cls._registered_process.pop(key, None)


class SCTExec(object):

    def __init__(self, name=None, options=None, help_str=None, section=None, registered_tool=None):
        """ Has the same variable than the models.models.RegisteredTool

        @TODO use input and output from __init__, not  cfg.INPUT_FILE_TAG
        and  cfg.OUTPUT_DIR_TAG
        :param name:
        :param options:
        :param help_str:
        """

        self.name = registered_tool.name if registered_tool else name
        self.options = registered_tool.options if registered_tool else options
        self.help_str = registered_tool.help_str if registered_tool else help_str
        self.section = registered_tool.section if registered_tool else section


    def _parse_options(self, options, name):
        """

        :param options:
        :return:
        """
        ret_dict = {}
        for o in options.values():

            value = o.get("value") if o.get("value") else o.get("default_value")

            if value:
                ret_dict[o["name"]] = value
                print (o["type_value"])
                if o["type_value"]==None: #Check for flags
                    ret_dict[o["name"]] = ""

            elif o["mandatory"]:
                raise IOError("option {} in {} is mandatory but not provided".format(o["name"], name))



        return ret_dict

    @property
    def cmd(self):
        """
        :return:
        string of the form
        "{EXEC_DIR_TAG}/exec.ext -i {INPUT_FILE_TAG} -o {OUTPUT_DIR_TAG} [--option other_options ...] "


        """
        opt = self._parse_options(self.options, self.name)

        opt = ' '. join(['{} {}'.format(k, v)
                        for k, v in opt.items()])


        return "{{{0}}}/{1}.py {2}".format(cfg.EXEC_DIR_TAG, self.name, opt)
        # return "echo 33 "


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import json

    logging.basicConfig(level=logging.DEBUG)

    engine = create_engine("sqlite:////home/poquirion/neuropoly/spinalcordtoolbox_web/server/db.sqlite")
    # engine = create_engine("sqlite:////Users/willispinaud/Dropbox/Amerique/Montreal/spinalcordtoolbox_web/server/db.sqlite")
    Session = sessionmaker(bind=engine)
    session = Session()

    pu = PluginUpdater(session=session, script_path="../../../spinalcordtoolbox/scripts", reload=False)
    # pu = PluginUpdater(session=session, script_path="/Users/willispinaud/Dropbox/Amerique/Montreal/spinalcordtoolbox/scripts", reload=True)

    #pu._load_plugins(None, "/Users/willispinaud/Dropbox/Amerique/Montreal/spinalcordtoolbox/scripts")



    # rt = session.query(models.RegisteredTool).filter(models.RegisteredTool.name == 'sct_propseg').first()
    # print(jsonpickle.dumps(rt))
    # plugins_path = cfg.SPINALCORD_BIN

    # tbr = ToolboxRunner(
    #     rt, plugins_path, '{}/t2.nii'.format(cfg.INPUT_PATH), cfg.OUTPUT_PATH)
    #
    # tbr.run()
