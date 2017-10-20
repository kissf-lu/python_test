# -*- coding: utf-8 -*-
from collections.abc import Iterator, Iterable, Generator

CHUNK_SIZE = 100


class StrItr(object):
    def __init__(self, str_s=''):
        self.str_s = str_s

    def rec(self, size):
        num = 0
        num +=1
        if num<=size:
            ite = [s for s in self.str_s]
            return iter(ite)



def reader2(s):
    for chunk in s.rec(CHUNK_SIZE):
        print(chunk)
        # process_data(data)

if __name__ == '__main__':
    s = StrItr('abcdefg')
    print(isinstance(s.rec(6), Iterator))