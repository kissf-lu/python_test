from multiprocessing import Process, Manager
import os

def f(d, l):
    print('c_p id ',os.getppid(), 'c id ', os.getpid())
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':

    print('parent id ', os.getpid())
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)
