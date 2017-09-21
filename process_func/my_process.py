from multiprocessing import Process, Manager, Pool
import time
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    time.sleep(2)
    info(f'function f {name}')
    print('hello', name)

def f10(name):
    time.sleep(10)
    info(f'function f {name}')
    print('hello', name)

def f5(name):
    time.sleep(5)
    info(f'function f {name}')
    print('hello', name)

def run():
    # info('main line')
    result = []
    # with Pool(processes=3) as pool:
    pool = Pool(processes=3)
    for i in range(3):
        res = pool.apply_async(func=f, args = (f'{i}',))
        result.append(res)

    pool.close()
    pool.join()

    for i in result:
        print(i.get())
    # p1 = Process(target=f, args=('bob1',))
    # p2 = Process(target=f10, args=('bob2',))
    # p3 = Process(target=f5, args=('bob3',))
    # p1.start()
    # p2.start()
    # p3.start()
    # p1.join()
    # p2.join()
    # p3.join()

if __name__ == '__main__':
    run()


