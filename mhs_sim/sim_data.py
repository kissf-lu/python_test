# 
"""
sim module
"""
# ======================= sys import ==============
from simpy import Environment
# import os
import time
# ======================= local import =============
from .config import SimConfig
from .data_sch import Packages


def gen_pac(env, data_q):
    """"""
    see_time = [1, 10, 100, 1000, 5000, SimConfig.PACKAGES_NUM]
    begin = 0
    for p in range(SimConfig.PACKAGES_NUM):
        record = Packages(
            parcel_id=p,
            small_id=p,
            path = ['c', 'd'],
            timestamp=env.now)
        begin += 1
        if begin in see_time:
            print(
                'gen package {0} at {1}'.format(p+1, time.time()))
        data_q.put(record)
        yield env.timeout(1)
    data_q.put(None)
    print(
        "gen package end at <{0}>".format(time.time()))


def f_gen(q):
    env = Environment()
    # print(
    #     f"pid: {os.getpid()}, "
    #     f"gen data start at <{time.time()}>:")
    env.process(gen_pac(env, q))
    env.run()


if __name__ == "__main__":
    pass