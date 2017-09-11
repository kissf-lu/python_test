# -*- coding: utf-8 -*-


import json


class ToDict(object):

    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):

        if isinstance(value, self.__class__):
            return value.to_dict()

        # 字典类型遍历
        elif isinstance(value, dict):
            return self._traverse_dict(value)

        # 列表类型遍历
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]

        #
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)

        else:
            return value


class JsonMixin(object):
    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        return cls(**kwargs)

    def to_json(self):
        return json.dumps(self.to_dict())


class BinaryTree(ToDict):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTreeWithParent(BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None):
        super().__init__(value, left=left, right=right)
        self.parent = parent

    def _traverse(self, key, value):
        if isinstance(value, self.__class__) and key == 'parent':
            return value.value
        else:
            return super()._traverse(key, value)

def func_dic(name_func):
    """hello"""
    name = name_func
    def pr(name):
        """"""
        print(name)
        pass
    pr(name)
    pass

to_dic = BinaryTreeWithParent(10)
print(
    hasattr(
        BinaryTreeWithParent, '__name__'
    ),
    isinstance(to_dic, BinaryTreeWithParent)
)
print(
    hasattr(func_dic('ok'), '__module__'), '\n',
    func_dic.__name__
)

from functools import wraps
# if __name__ == '__main__':
    # to_dic = BinaryTree(10)
    # print(hasattr(to_dic, '__dict__'), ToDict.__dict__)