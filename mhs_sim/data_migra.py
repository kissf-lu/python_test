# 
"""
data migration module
"""
# ======================= sys import ==============
import os
import time
from random import randint
from simpy import Environment
# ======================= local import =============
from mhs_sim.config import SimConfig
from mhs_sim.data_sch import Packages


def sync_clock(env, val):
    # print(f"mhs time: {env.now}, last sim time: {val.timestamp}")
    if env.now <= val.timestamp:
        yield env.timeout(val.timestamp-env.now)
    else:
        yield env.timeout(0)
    # pac = Packages(
    #     parcel_id=val.parcel_id,
    #     small_id=val.small_id,
    #     path=val.path,
    #     timestamp=env.now)


def random_delay(env, val):
    _delay_val = randint(5, 10)
    yield env.timeout(_delay_val)
    pac = Packages(
        parcel_id=val.parcel_id,
        small_id=val.small_id,
        path=val.path,
        timestamp=env.now)

    # print(
    #     f"mhs pid: {os.getpid()}, "
    #     f"{pac} random delay time {_delay_val}")


def mhs_run(env, q_data):
    begin = 0
    see_time = [1, 10, 100, 1000, 5000, 100000]
    while True:
        _val = q_data.get()
        if _val is None:
            # 使其他进程退出
            q_data.put(None)
            break
        # ============== 
        begin += 1
        if begin in see_time:
            print(
                ("pid: {0}, "
                "Consum {1} at <{2}>"
                "".format(os.getpid(), begin, time.time())))

        yield env.process(sync_clock(env, _val))
        # env.process(random_delay(env, _val))
    # print(
    #     f"pid: {os.getpid()}, "
    #     f"Consum end at <{time.time()}>")


def f_run(q):
    SimConfig.NAME_SIM = 'Consum'

    # print(
    #     f"pid: {os.getpid()}, "
    #     f"{SimConfig.NAME_SIM} run at <{time.time()}>")

    env = Environment()
    env.process(mhs_run(env, q))
    env.run()


if __name__ == "__main__":
    pass
