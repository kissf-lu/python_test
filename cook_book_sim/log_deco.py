# user/bin/python3
"""
Info:
    Code Day: 10/21/2017
    Author: kissf
@ hyssg.lu.com
"""
from functools import wraps
import logging


def logged(
        *, level_log: int=None, user: str='ROOT', if_file_out: bool=False):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """
    level_log = level_log if level_log is not None else logging.INFO
    log_name = user if user is not None else 'ROOT'

    format_ = '<%(asctime)s><%(name)s>: %(message)s'
    logging.basicConfig(format=format_, level=level_log)
    formatter = logging.Formatter(format_)
    logger = logging.getLogger(log_name)
    if if_file_out:
        file_handler = f'{user}_LOG.log'
        fh = logging.FileHandler(file_handler)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    def decorate(func):
        @wraps(func)
        def wrapper(**kwargs):
            if level_log is logging.DEBUG:
                return logger.debug

            elif level_log is logging.CRITICAL:
                return logger.critical
            # 不是以上情况，就输出INFO级别Log
            # 添加回传的logger 对象至 logger字典
            try:
                kwargs['loggers'] = logger
            except KeyError:
                raise ValueError('loggers value is forbid initial!')

            return func(**kwargs)
        return wrapper
    return decorate


@logged(user='SIM', if_file_out=False)
def deco_logging(**kwargs):
    """
    
    Param kwargs: 
        loggers: logging obj from decorators return value . 
    Return:
         logger obj
    """

    re_loggers = kwargs['loggers'].info

    return re_loggers
