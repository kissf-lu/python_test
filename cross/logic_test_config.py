
from simpy import Environment
from simpy import Store
from random import choice


class Config(object):

    env = Environment()

    # 随机种子配置
    RANDOM_SEED = 42
    # package生成器配置信息
    NUM_PACKAGES = 10   # 生成package数量/个
    INTERVAL_TIME = 10  # 生成package间隔/s
    # 包裹传送带类型：pipline 类/simpy.Store/simpy.PriorityStore
    TYPE_PIP_LINE = Store(env)  #配置传送带的类型


class CrossTest(Config):
    ID_LAST_MACHINE = ['r1']
    ID_TEST_MACHINE = ['m1_1', 'm1_2', 'm1_3', 'm1_4']
    # 根据测试机器后面可能去的机器ID配置
    ID_NEXT_MACHINE = ['secondary_1', 'secondary_2', 'cross_1', 'cross_2',
                       'cross_3']
    CAPACITY_RESOURCE = None  # 如果测试机器内部无资源调用，设置为None，否则设置资源数(如人力)
    PROCESS_TIME = 10
