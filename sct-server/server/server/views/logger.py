__author__ = 'willispinaud'

import logging 

from cornice import Service
from ..controler import SCTLog

import string
from ..controler import SCTLog

logger = Service('logger',
                 '/logger',
                 'Get the running SCT log and return it to the client')

@logger.get()
def logger_get(request):
    '''
    :param request.uid: The user uid, it's used to find the process launched by the user
    :return: one line of the log
    '''

    uid = request.GET.get("uid")
    if uid is None:
        logging.info("User not logged")
        return "User not logged"

    try:
        info = SCTLog(uid)
    except LookupError:
        logging.info("No process for user {}".format(uid))
        return None

    if request.GET.get("old", None):
        logging.info("Returning old log")
        log = info.old_log()
    else:
        logging.info("Returning tail log")
        log = info.log_tail(maxline=10)

    return log
