"""
dicript cls module
"""


class DisReload(object):
    """class doc"""
    __index = 0

    def __init__(self):
        """init"""
        self._val = "name_{}".format(self.__class__.__index)
        self.__class__.__index += 1

    def __set__(self, instance, value):
        """set val"""
        if value > 10:
            raise ValueError("too large value!")
        else:
            setattr(instance, self._val, value)

    def __get__(self, instance, owner):
        """get doc"""
        return getattr(instance, self._val)


class ReloadData(object):
    weight = DisReload()

    def __init__(self, weight):
        self.weight = weight


if __name__ == "__main__":
    pass
