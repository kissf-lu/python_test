import threading
import itertools as it
from collections import namedtuple
import time
import sys


SPIN_TIME = 7
Event = namedtuple('Event', 'id status')


class Single(object):
    go =True


def spin(msg, event):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in it.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        time.sleep(.1)
        if not event.go:
            break
    write(' ' * len(status) + '\x08' * len(status))


def wait_sus(t):
    """"""
    time.sleep(t)
    return 77


def super_spin():
    event = Single()
    spinner = threading.Thread(target=spin, args=('thinking', event))
    spinner.start()
    result = wait_sus(SPIN_TIME)
    event.go=False
    spinner.join()
    return result


def main():
    result =super_spin()
    print('Answer:', result)


if __name__ == '__main__':
    main()
