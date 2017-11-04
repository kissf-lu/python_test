import asyncio
import itertools as it
from collections import namedtuple
import time
import sys


SPIN_TIME = 2
Event = namedtuple('Event', 'id status')


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
    return 'cancel'


async def wait_sus(t):
    """"""
    # print('waiting ...')
    await asyncio.sleep(t)

    return 77


async def super_spin(loop):
    spinner = asyncio.ensure_future(spin('thinking'))
    await wait_sus(SPIN_TIME)
    spinner.cancel()
    spinner2 = asyncio.ensure_future(spin('thinking2'))
    result = await wait_sus(SPIN_TIME)
    spinner2.cancel()
    return spinner


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(super_spin(loop))
    loop.close()
    print(f'Answer at {time.time()}, result: {result.result()}')


if __name__ == '__main__':
    main()
