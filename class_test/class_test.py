# -*- coding: utf-8 -*-
""" module doc

"""

from os.path import realpath, join, split


class SaveConfig:
    """config set"""
    DATA_DIR = join(
        split(split(split(realpath(__file__))[0])[0])[0], 'data')

class BaseName(object):
    """A class ::base class"""
    def __init__(self, name):
        self.name = name

class NameB(BaseName):
    """B class doc"""
    def __init__(self, name):
        """"init doc"""
        super().__init__(name)
        self.name *= 2

class NameC(BaseName):
    """C class doc"""
    def __init__(self, name):
        super().__init__(name)
        self.name += 5

    def __repr__(self):
        return f"NameC value is {self.name}"

class NameD(NameB, NameC):
    """from B C class"""
    def __init__(self, name):
        """D class"""
        super().__init__(name)

    def __repr__(self):
        return f"value is {self.name}"

def run():
    """test run ccript api"""
    name_thr = NameD(6)
    name_c = NameC(7)
    print(name_thr)
    print(name_c)

if __name__ == '__main__':
    run()
