__author__ = 'willispinaud'

from pyramid.view import view_config
from ..models import models
from cornice.resource import resource, view
from cornice import Service
from .. import cfg
from .. import controler
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import jsonpickle

import inspect
import importlib
import logging

def access_info(route):
    def new_route(request, *args, **kwargs):
        logging.info("access to {} by {} from {}".format(route.__name__, request.authenticated_userid, request.client_addr))
        route(request, *args, **kwargs)
    return new_route


sctoolbox = Service('sctoolbox',
                 '/sctoolbox',
                 'communication with the toolbox')

@sctoolbox.get(renderer='string')
#@access_info
def sctoolbox_get(request):
    '''
    :param request:
    :return: Return a list of all the sctools which have a get_parser
    '''
    # logging.info("access to {} route".format(inspect.stack()[1][3]))

    session = request.db
    rt = session.query(models.RegisteredTool).all()
    return jsonpickle.dumps(rt)

@sctoolbox.post()
@access_info
def sctoolbox_post(request):
    '''
    :param request.uid: User uid
    :param request.args: Args selected by the usergit pull
    :param request.tool_name: the tool selected by the user
    :return:
    '''

    session = request.db
    plugins_path = cfg.SPINALCORD_SCRIPTS
    try:
        uid = request.json_body['uid']
        options = request.json_body['args']
        tool_name = request.json_body['tool_name']

        rt = session.query(models.RegisteredTool).filter(models.RegisteredTool.name == tool_name).first()

        # update the RT object with user value
        for o in rt.options.values():
            for i in options:
                if o.get("order") == int(i):
                    o["value"] = options[i]

    except KeyError:
        rt = jsonpickle.loads(request.body.decode('utf-8'))



    if rt:
        try:
            process = controler.SCTLog(uid)
            if process._tr.check_status() is None:
                logging.warning("process {} is still running, waiting for it to end".format(process._tr.rt.name))
                return "Process is still running"
        except LookupError:
            pass
        tbr = controler.ToolboxRunner(
        controler.SCTExec(registered_tool=rt),
        plugins_path, user_id=uid, process_uid=None)

    tbr.run()

    return {}



plugin_update =  Service('plugin_update',
                 '/plugin_update',
                 'update the sct list')

@plugin_update.get()
@access_info
def plugin_update_get(request):
    '''
    :param request:
    :return: Return a list of all the sctools which have a get_parser
    '''

    session = request.db
    controler.PluginUpdater(session=session, script_path=cfg.SPINALCORD_SCRIPTS, reload=True)
    #controler.PluginUpdater(session=session, script_path=cfg.SPINALCORD_SCRIPTS, reload=False) #DEBUG
    return "Ok"

