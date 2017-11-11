import time
from functools import wraps
def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        # self, *args = args
        start = time.time()
        result = func(*args, **kwargs)
        time.sleep(1)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper



@timethis
def ping():
    """"""
    print("ping 000!")
    return


if __name__ == '__main__':
    ping()
    print(ping.__name__, ping.__dict__)
