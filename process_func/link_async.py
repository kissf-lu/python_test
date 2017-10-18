from queue import Queue
from functools import wraps
from multiprocessing import Pool as pl

class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args
        print('Async')

def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        print('args:',*args)
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                p=pl(processes=1)
                a = f.send(result)
                p.apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper

def add(x, y):
    return x + y

@inlined_async
def run():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello ', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Goodbye')

if __name__ == '__main__':
    run()