"""
@author: chois
"""


class Person(object):
    """class docstring"""
    def __init__(self, first_name):
        """
        preson docstring
        """
        self.first_name = first_name
        self._last_name = None

    # Getter function
    @property
    def last_name(self):
        """
        last name of people
        """
        try:
            return self._last_name
        except AttributeError:
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


CLU = Person('chois')
CLU.last_name = 'lu'

print(CLU.first_name, CLU.last_name)
