# -*- coding: utf-8 -*-



from simpy import Environment
from simpy import Store


__all__ = ['Config']


class Config(object):

    env = Environment()

    # 随机种子配置
    RANDOM_SEED = 42
    # 机器树的层数
    NODE_LAYERS = 3
    # package生成器配置信息
    NUM_PACKAGES = 10   # 生成package数量/个
    INTERVAL_TIME = 1  # 生成package间隔/s
    # 包裹传送带类型：pipline 类/simpy.Store/simpy.PriorityStore
    TYPE_PIP_LINE = Store(env)  # 配置传送带的类型
    # 测试机器类设置
    # CLASS_TEST_MACHINE = None
    ID_LAST_MACHINE = ['last_machine_1']
    ID_TEST_MACHINE = ['test_machine_1', 'test_machine_2', 'test_machine_3', 'test_machine_4']
    # 根据测试机器后面可能去的机器ID配置
    ID_NEXT_MACHINE = ['next_machine_1', 'next_machine_2', 'next_machine_3', 'next_machine_4']

    def __init__(self):
        pass

    @staticmethod
    def init_app(app):
        pass