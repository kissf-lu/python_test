import asyncio
import itertools as it
from collections import namedtuple
import time
import sys


SPIN_TIME = 7
Event = namedtuple('Event', 'id status')


def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in it.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))


def wait_sus(t):
    """"""
    yield from asyncio.sleep(t)

    return 77


def super_spin(loop):
    spinner = loop.create_task(spin('thinking'))
    result = yield from wait_sus(SPIN_TIME)
    spinner.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(super_spin(loop))
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()
