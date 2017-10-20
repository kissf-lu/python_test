#
"""
@author chois_lu
"""
__author__='chois'


import collections
import bisect


class SortedItems(collections.Sequence):
    """"""
    def __init__(self, init_val: list=None):
        """
        Args:
            init_val: list type . initial init_val

        """
        self._items = sorted(init_val) if init_val is not None else []

    def __getitem__(self, index):
        """"""
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        """"""
        bisect.insort(self._items, item)


class ItemsCC(collections.MutableSequence):
    """"""
    def __init__(self, init_val: list=None):
        self._items = init_val if init_val is not None else []

    def __len__(self):
        print('calling _len')
        return len(self._items)

    def __getitem__(self, index):
        print('calling _getitem')
        return self._items[index]

    def __setitem__(self, index, value):
        print('calling _setitem')
        self._items[index] = value

    def __delitem__(self, index):
        """"""
        print('calling _delitem')
        del self._items[index]

    def insert(self, index, value):
        print('calling insert')
        self._items.insert(index, value)


if __name__ == '__main__':
    """"""
    item2 = SortedItems([3,5,7,1,2])
    item3 = ItemsCC()
    print('isinstance Iterator:', isinstance(item2, collections.Iterator))
    print('isinstance Iterable:', isinstance(item2, collections.Iterable))
    

