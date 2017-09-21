import time
import _thread


def timer(no, interval):
    cnt = 0
    while cnt < 10:
        print(
        'Thread:(%d) Time:%s\n' % (no, time.ctime()))
        time.sleep(interval)
        cnt += 1
        _thread.exit_thread()


def run():  # Use thread.start_new_thread() to create 2 new threads
    _thread.start_new_thread(timer, (1, 1))
    _thread.start_new_thread(timer, (2, 2))


if __name__ == '__main__':
    run()