# -*- coding: utf-8 -*-


from simpy import Environment
from test import Config
from tool.items import Pipeline
from test.logic_test import LogicTest


class CrossSimConfig(Config):
    # RANDOM_SEED = 57
    # 包裹生成的数量
    NUM_PACKAGES = 50
    # INTERVAL_TIME = 10
    TYPE_PIP_LINE = Pipeline
    # 产生package机器ID列表，本次杭州仿真模型一般一个机器只有一个入口队列
    ID_LAST_MACHINE = ['last_1', 'last_2']
    # 测试机器ID列表
    ID_TEST_MACHINE = ['cross1_1', 'cross1_2']
#     # 根据测试机器后面可能去的机器ID列表
    ID_NEXT_MACHINE = ['next_1']
    # 测试机资源数
    CAPACITY_RESOURCE = None  # 如果测试机器内部无资源调用，设置为None，否则设置资源数(如人力)
    # 测试机单资源处理时延
    PROCESS_TIME = None  # 如果测试机器没有处理货物延时，设置为None，否则设置为对应延时

if __name__ == '__main__':
    env = Environment()
    t1 = LogicTest(env, str, CrossSimConfig)
    t1.generator()
    print(t1.path)
    pk = env.process(t1.packages_generator())
    env.run(until=50)

