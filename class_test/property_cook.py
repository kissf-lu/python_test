#


class Person(object):
    def __init__(self, name):
        self._name = name

    # Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


if __name__ == '__main__':
    p1 = Person('any')

    print(f"person name {p1.name}")
    p1.name = 'can'
    print(f"rename {p1.name}")
