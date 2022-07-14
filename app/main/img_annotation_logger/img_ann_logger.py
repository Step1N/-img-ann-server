import logging
import logging.config
import os
from http.client import HTTPConnection

PROJECT_ROOT = os.getcwd()


def log_configuration():
    HTTPConnection.debuglevel = 0
    conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),  "logger.conf")
    file_name = os.path.abspath(os.path.join(PROJECT_ROOT, "ImgAnnLogger.log"))
    logging.config.fileConfig(conf_path,  defaults={'logfilename': file_name})
    logger = logging.getLogger("ImgAnnLogger")

    return logger


def get_app_logger():
    return log_configuration()

