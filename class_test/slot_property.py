#


class Person(object):
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def last_name(self):
        try:
            return self._last_name
        except AttributeError as attr:
            raise AttributeError("you haven't init last_name")

    # Setter function
    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._last_name = value

    # Deleter function (optional)
    @last_name.deleter
    def last_name(self):
        raise AttributeError("Can't delete attribute")


p1 = Person('chois')
p1.last_name = 'lu'

print(p1.first_name, p1.last_name)
