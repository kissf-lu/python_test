import asyncio
import itertools as it
from collections import namedtuple
import time
import sys


SPIN_TIME = 7
Event = namedtuple('Event', 'id status')


#@asyncio.coroutine
async def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in it.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))


#@asyncio.coroutine
async def wait_sus(t):
    """"""
    await asyncio.sleep(t)

    return 77

@asyncio.coroutine
def super_spin():
    spinner = asyncio.async(spin('thinking'))
    yield from wait_sus(SPIN_TIME)
    spinner.cancel()
    spinner2 = asyncio.async(spin('thinking2'))
    result = yield from wait_sus(SPIN_TIME)
    spinner2.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(super_spin())
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()
