from functools import wraps
import logging



def logged(*, level_str=None, user: str = 'root', file_handler=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """
    KYE_LEVEL = {'INFO': logging.INFO,
                 'ERRO': logging.ERROR,
                 'DEBUG': logging.DEBUG}

    if level_str is None:
        level = logging.INFO
    else:
        try:
            level = KYE_LEVEL[level_str]
        except KeyError:
            raise KeyError('logging level key')

    log_name = user
    logger = logging.getLogger(log_name)
    format_ = '<%(asctime)s><%(name)s>: %(message)s'
    logging.basicConfig(format=format_, level=level)

    if file_handler is not None and len(file_handler)>0:
        fh = logging.FileHandler(file_handler)
        formatter = logging.Formatter(format_)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if level_str is 'INFO':
                return logger.info

            elif level_str is 'DEBUG':
                return logger.debug

            return func(*args, **kwargs)

        return wrapper

    return decorate


# Example use log
@logged(level_str='INFO', user='sim', file_handler='test_log_ss.log')
def log_out(log=logging):
    loggers = log.info
    return loggers



# if __name__ == '__main__':
#     log = log_out()
#     for i in range(10):
#         log(f'INFO {i} out')
