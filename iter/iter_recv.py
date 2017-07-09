# -*- coding: utf-8 -*-


CHUNK_SIZE = 100


class StrItr(object):
    def __init__(self, str_s=''):
        self.str_s = str_s

    def rec(self, size):
        num = 0
        num +=1
        if num<=size:
            ite = [s for s in self.str_s]
            return next(ite)



def reader2(s):
    for chunk in iter(lambda: s.rec(CHUNK_SIZE), b''):
        print(chunk)
        # process_data(data)

if __name__ == '__main__':
    s = StrItr('abcdefg')
    reader2(s)