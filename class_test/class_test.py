# -*- coding: utf-8 -*-


from os.path import realpath, join, split


class SaveConfig:

    DATA_DIR = join( split(split(split(realpath(__file__))[0])[0])[0], 'data')

class A(object):
    def __init__(self, name_a):
        print('enter A')
        self.name = name_a
        print('leave A')


class B(A):
    def __init__(self,name_a):
        print('enter B')
        super().__init__(name_a)
        print('leave B')
    and_d = '\nrr'


class C(A):
    def __init__(self, name_a):
        print('enter C')
        super().__init__(name_a)
        print('leave C')


class D(B, C):
    def __init__(self, name_a):
        print('enter D')
        super().__init__(name_a)
        print('leave D')

    @property
    def add_name(self):
        return f"name sub is :{self.name}"

if __name__ == '__main__':
        sub_d = D('A')
        # bb = B('A')
        # name = sub_d.add_name
        # print(name, bb.and_d)