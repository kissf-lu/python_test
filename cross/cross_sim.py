# -*- coding: utf-8 -*-

"""
作者：kissf lu
日期：2017/7/7
说明：杭州项目，汇流点类模块 仿真测试

"""

from simpy import Environment
from simpy import PriorityStore
from simpy import PriorityItem
from simpy import Resource
from cross import Cross
import random as rd
from numpy.random import choice


RANDOM_SEED = 42
NUM_PORT_ABLE = 2
NUM_PACKAGES = 10
QUEUE_GENERATOR_GAP = 10
INPUT_QUEUE_ID = ['x1_in1', 'x1_in2']
INPUT_QUEUE_DIC = {}
OUTPUT_QUEUE = None
CROSS_ID = 'x1'
NUM_RUN_TIME = 5
rd.seed(RANDOM_SEED)


def machine_package(env, generator_queue_res):
    """"""
    for i in range(NUM_PACKAGES):
        env.process(machine_queue_input(env, generator_queue_res, i))


def machine_queue_input(env, generator_queue_res, package_id):
    """"""
    with generator_queue_res.request() as req:
        yield req
        id_queue = str(choice(INPUT_QUEUE_ID))
        id_package = ''.join([id_queue, '_', str(package_id)])
        package_items = {'package_id': id_package, 'package_gen_time': env.now}
        print('put package', id_package, 'into queue', id_queue, 'at', env.now)
        yield INPUT_QUEUE_DIC[id_queue].put(PriorityItem(priority=env.now, item=package_items))
        # print('queue', id_queue,'info:', INPUT_QUEUE_DIC[id_queue].items) rd.randint(2, 30)
        yield env.timeout(2)


def cross_sim():
    """
    cross module test: Cross 模块测试单元
    """
    env = Environment()
    INPUT_QUEUE_DIC.update({'x1_in1': PriorityStore(env=env), 'x1_in2': PriorityStore(env=env)})
    generator_queue_res = Resource(env=env, capacity=NUM_PORT_ABLE)
    for i in range(NUM_PACKAGES):
        env.process(machine_queue_input(env, generator_queue_res, i))
    #  env.process(machine_package(env=env, generator_queue_res=generator_queue_res))
    OUTPUT_QUEUE = PriorityStore(env)
    cross = Cross(env=env, id_x=CROSS_ID, input_dic=INPUT_QUEUE_DIC, out_put=OUTPUT_QUEUE)
    env.run()


if __name__ == '__main__':
    print('run!')
    cross_sim()
    print('end')
