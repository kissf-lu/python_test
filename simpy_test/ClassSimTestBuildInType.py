# -*- coding: utf8 -*-


class BIClass:
    """
    test build in class 
    """
    def __init__(self):
        """init moduel just init"""

    def class_generator(self, arg=None):
        """class self generator"""
        print("Entry generator fuc()")
        try:
            yield 0
            try:
                yield 1
                1/0
                yield 2
            except ZeroDivisionError:
                yield 3
                yield 4
                # raise
            1/0
        except ZeroDivisionError:
            yield 5
        yield 6
        try:
            print(arg)
        finally:
            print("Don`t forget to clean up when 'close()' is called")
            yield 7

    def print_out(self):
        """ print functions"""
        g_func = self.class_generator(1)
        # for g in g_func:
        #    print(g)
        print(list(g_func))
        # print(dir(self))
        # print(self.__doc__)
        # print(self.__dict__)
        print(self.__module__)
        print(self.__init__.__doc__)


if __name__ =='__main__':
    build_in_1 = BIClass()
    build_in_1.print_out()
    # print(build_in_1.__doc__)
    # print(build_in_1.__init__.__doc__)

