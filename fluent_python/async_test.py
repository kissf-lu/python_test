#
import asyncio
import os
from types import coroutine


class AsyncIteratorWrapper:
    def __init__(self, obj):
        self._it = iter(obj)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            value = next(self._it)
        except StopIteration:
            raise StopAsyncIteration
        return value

class AsyncIterable:
    def __aiter__(self):
        return self

    async def __anext__(self):
        data = await self.fetch_data()
        if data:
            return data
        else:
            raise StopAsyncIteration

    async def fetch_data(self):
        pass


@coroutine
def async_run(it_st):
    # cc = AsyncIteratorWrapper('ABC')
    for i in it_st:
        print(i)
        # await asyncio.sleep(1)
    # raise StopAsyncIteration


async def super_async():
    await(async_run('ABC'))
    await (async_run('EFA'))
        # print('OMG asynchronicity!')



async def read_base(file, mode):
    with open(file=file, mode=mode if mode else 'r') as file_io:
        for l in file_io:
            print(l)


async def read_await_base(file_dir):
    with open(file=file_dir, mode='r') as fio:
        for l in fio:
            print(l)


async def read_txt():
    asyncio.ensure_future(
        read_await_base('17-future/country/country_codes.txt'))


def main_async():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(read_txt())

    loop.close()


@coroutine
def generator_coroutine():
    yield 1


async def native_coroutine():
    await generator_coroutine()

def main():
    cc = native_coroutine().send(None)
    return cc


if __name__ == '__main__':
    main_async()
    # print(main())
