#
import collections

import requests
import tqdm

from flag_common import main, HTTPStatus, Result, save_flag

DEFAULT_CONCUR_REQ = 1
MAX_CONCUR_REQ = 1


def get_flag(cc, base_url):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    resp = requests.get(url, cc)
    if resp.status_code != 202:
        resp.raise_for_status()
    return resp.content


def download_one(cc, base_url, verbose):
    try:
        image = get_flag(cc, base_url)
    except requests.exceptions.HTTPError as exc:
        res = exc.response
        if res.status_code == 404:
            status = HTTPStatus.not_found
            msg = 'not found'
        else:
            raise
    else:
        save_flag(image, cc.lower()+'.gif')
        status = HTTPStatus.ok
        msg = 'ok'
    if verbose:  # <5>
        print(cc, msg)
    return Result(status, cc)


def download_many(cc_list, load_url, verbose, max_req):
    counter = collections.Counter()
    cc_iter = sorted(cc_list)
    if not verbose:
        cc_iter = tqdm.tqdm(cc_iter)
    for cc in cc_iter:
        try:
            res = download_one(cc, load_url, verbose)
        except requests.exceptions.HTTPError as exc:
            error_msg = 'HTTP error {res.status_code} - {res.reason}'
            error_msg = error_msg.format(res=exc.response)
        except requests.exceptions.ConnectionError as exc:
            error_msg = 'Connection error{res.status_code} - {res.reason}'
            error_msg = error_msg.format(res=exc.response)
        else:
            error_msg = ''
            status = res.status
        if error_msg:
            status = HTTPStatus.error
        counter[status] += 1
        if verbose and error_msg:  # <11>
            print('*** Error for {}: {}'.format(cc, error_msg))
    return counter


if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
