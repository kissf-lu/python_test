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
import random as rd

NUM_PACKAGE = 10


def put_package(env, queue, package):
    """"""
    print('in at-------------->', env.now)
    yield queue.put(package)
    print(f"put package {package.item['id']} at {env.now}")
    yield env.timeout(rd.randint(4,4))


def put_package_queue(env, id, res, queue):
    """"""
    with res.request() as req:
        yield req
        print('package', id, 'come at', env.now)
        package = PriorityItem(priority=env.now, item={'id': id, 'priority_time': env.now})
        yield env.process(put_package(env, queue, package))


def get_package(env, queue):
    """"""
    while True:
        get_package = yield queue.get()
        if get_package.item['priority_time'] <= env.now:
            print('----->get package', get_package.item['id'], get_package.item['priority_time'], 'at', env.now)


def main_run():
    """"""
    env = Environment()
    priority_store = PriorityStore(env=env)
    res_port = Resource(env=env, capacity=2)
    for i in range(NUM_PACKAGE):
        env.process(put_package_queue(env=env, id=i, res=res_port, queue=priority_store))
    #env.process(get_package(env, priority_store))
    env.run()


if __name__ == '__main__':
    print('run ---------------------------------------- ')
    main_run()
    print('end ----------------------------------------')
