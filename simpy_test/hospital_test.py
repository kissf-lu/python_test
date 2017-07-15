# -*- coding: utf-8 -*-

"""
======================================================================================================
                                                     杭州HUB仿真项目

                                    项目启动日期：2017年7月6日
                                    项目启动标识：AIRPORT OF EZHOU'S PROJECT  -- HZ
                                    ===========================================
                                    代码创建日期：2017年7月6日
                                    代码创建工程师：卢健
                                    代码版本：1.0
                                    版本更新日期：2017年7月6日
                                    版本更新工程师：卢健

                                    代码整体功能描述：汇流点机器测试单元
                                                      1、用于测试cross类模块；


=====================================================================================================
"""

from simpy import Environment
from simpy import PriorityStore
from simpy import PriorityItem
from simpy import Resource
from simpy_test.hospital import Hospital
import random as rd
from numpy.random import choice


RANDOM_SEED = 42
PACKAGE_RES = 2  # 每次生成包裹的数量
QUEUE_RES = 2
NUM_PORT_OUT = 1
NUM_PORT_IN = 2
NUM_PEOPLE = 2
NUM_PACKAGES = 10  # 本次数据的
MACHINE_ID = 'h1'
INPUT_QUEUE_ID = []
OUTPUT_QUEUE_ID = []
INPUT_QUEUE_DIC = {}
OUTPUT_QUEUE_DIC = {}
rd.seed(RANDOM_SEED)


def packages(env, generator_package_res, generator_queue_res):
    """"""
    for num in range(NUM_PACKAGES):
        env.process(machine_package(env=env, package_name=num,
                                    generator_package_res=generator_package_res,
                                    generator_queue_res=generator_queue_res))


def machine_package(env, package_name,
                    generator_package_res,
                    generator_queue_res):
    """"""
    with generator_package_res.request() as req:
        yield req
        env.process(machine_queue_input(env, generator_queue_res, package_name))
        yield env.timeout(1)


def machine_queue_input(env, generator_queue_res, package_id):
    """"""
    # print('package', package_id, 'come', 'at', env.now)
    with generator_queue_res.request() as req:
        yield req
        id_queue = str(choice(INPUT_QUEUE_ID))
        id_package = ''.join([id_queue, '_', str(package_id)])
        package_items = {'package_id': id_package, 'package_gen_time': env.now}
        yield env.timeout(rd.randint(5, 5))
        print('<----package', package_id, 'was pushed into queue', id_queue,
              'at', env.now)
        INPUT_QUEUE_DIC[id_queue].put(PriorityItem(priority=env.now,
                                                   item=package_items))


def cross_sim():
    """
    cross module test: Cross 模块测试单元
    """
    env = Environment()
    INPUT_QUEUE_ID.extend(
        [''.join([MACHINE_ID, '_in', str(i)]) for i in range(NUM_PORT_IN)]
    )
    OUTPUT_QUEUE_ID.extend(
        [''.join([MACHINE_ID, '_out', str(i)]) for i in range(NUM_PORT_OUT)]
    )

    for id in INPUT_QUEUE_ID:
        INPUT_QUEUE_DIC.update({id: PriorityStore(env=env)})
    for id in OUTPUT_QUEUE_ID:
        OUTPUT_QUEUE_DIC.update({id: PriorityStore(env=env)})

    generator_queue_res = Resource(env=env, capacity=QUEUE_RES)
    generator_package_res = Resource(env=env, capacity=PACKAGE_RES)

    packages(env=env,
             generator_package_res=generator_package_res,
             generator_queue_res=generator_queue_res)
    hospital = Hospital(env=env,id_h=MACHINE_ID,
                        hospital_capacity=NUM_PEOPLE,
                        input_dic=INPUT_QUEUE_DIC,
                        output_dic=OUTPUT_QUEUE_DIC)
    env.run()


if __name__ == '__main__':
    print('run!')
    cross_sim()
    print('end')
