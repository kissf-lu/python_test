from multiprocessing import Process, current_process
import time
import sys

def daemon():
    print ('Starting:', current_process().name)
    time.sleep(2)
    print ('Exiting :', current_process().name)

def non_daemon():
    print ('Starting:', current_process().name)
    print ('Exiting :', current_process().name)

if __name__ == '__main__':
    workers = []
    d_work = Process(
        name='daemon', target=daemon)
    d_work.daemon = True
    workers.append(d_work)
    # ======================
    n_work = Process(
        name='non-daemon', target=non_daemon)
    n_work.daemon = False
    workers.append(n_work)

    d_work.start()
    time.sleep(1)
    n_work.start()

    for w in workers:
        w.join()
