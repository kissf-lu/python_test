# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print('get', instance.__dict__)
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value
        print('set', instance.__dict__)

    def __delete__(self, instance):
        del instance.__dict__[self.name]

from collections import namedtuple

class Point:
    """
    """
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        """ integer class discrip
        Arg:
            x: ::type int
            y: ::type int
        """
        self.x = x
        self.y = y


if __name__ == '__main__':
    p = Point(2,3)
    print(p.x)
