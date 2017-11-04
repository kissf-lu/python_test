#
import collections
import tqdm
import asyncio
import aiohttp
from aiohttp import web

from flags2_common import main, HTTPStatus, Result, save_flag

DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000


class FetchError(Exception):
    def __init__(self, country):
        self.country_code = country


async def get_url(base_url):
    # res = await aiohttp.request('GET', base_url)
    async with aiohttp.request('GET', base_url) as res:
        if res.status == 200:
            c_type = res.headers.get('Content-type', '').lower()
            if 'json' in c_type or base_url.endswith('json'):
                data = await res.json()
            else:
                data = await res.read()
            return data

        elif res.status == 404:
            raise web.HTTPNotFound()
        else:
            raise aiohttp.errors.HttpProcessingError(
                code=res.status, message=res.reason, headers=res.headers)


async def get_country(base_url, cc):
    url = '{}/{cc}/metadata.json'.format(base_url, cc=cc.lower())
    metadata = await get_url(url)
    return metadata['country']


async def get_flag(base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    return await get_url(url)


async def download_one(cc, base_url, semaphore, verbose):
    try:
        async with semaphore:
            image = await get_flag(base_url, cc)
        async with semaphore:
            country = await get_country(base_url, cc)
    except web.HTTPNotFound:
        status = HTTPStatus.not_found
        msg = 'not found'
    except Exception as exc:
        raise FetchError(cc) from exc
    else:
        country = country.replace(' ', '_')
        file_name = '{}-{}.gif'.format(country, cc)
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, save_flag, image, file_name)
        # save_flag(image, file_name)
        status = HTTPStatus.ok
        msg = 'ok'
    if verbose:  # <5>
        print(cc, msg)
    return Result(status, cc)


async def download_many_cor(cc_list, load_url, verbose, max_req):
    counter = collections.Counter()
    semaphore = asyncio.Semaphore(value=max_req)
    to_do = [download_one(cc, load_url, semaphore, verbose)
             for cc in sorted(cc_list)]
    future_iter = asyncio.as_completed(to_do)
    if not verbose:
        future_iter = tqdm.tqdm(future_iter, total=len(cc_list))
    for f in future_iter:
        try:
            res = await f
        except FetchError as exc:
            country_code = exc.country_code
            try:
                error_msg = exc.__cause__.args[0]
            except IndexError:
                error_msg = exc.__cause__.__class__.__name__
            if verbose and error_msg:  # <11>
                msg = '*** Error for {}: {}'
                print(msg.format(country_code, error_msg))
            status = HTTPStatus.error
        else:
            status = res.status
        counter[status] += 1

    return counter


def download_many(cc_list, url, verbose, max_req):
    loop = asyncio.get_event_loop()
    cor = download_many_cor(cc_list=cc_list,
                            load_url=url,
                            verbose=verbose,
                            max_req=max_req)

    counter = loop.run_until_complete(cor)
    loop.close()
    return counter


if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
