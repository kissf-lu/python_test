# 
"""
data migration module
"""
# ======================= sys import ==============
import time
import os
from random import randint
from simpy import Environment
# ======================= local import =============
from .config import SimConfig
from .data_sch import Packages


def sync_clock(env, val: Packages):
    yield env.timeout(val.timestamp)
    pac = Packages(
        parcel_id=val.parcel_id,
        small_id=val.small_id,
        timestamp=env.now)
    print(
        f"pid: {os.getpid()}, "
        f"get value: {pac}")


def random_delay(env, val):
    _delay_val = randint(5, 10)
    yield env.timeout(_delay_val)
    pac = Packages(
        parcel_id=val.parcel_id,
        small_id=val.small_id,
        timestamp=env.now)

    print(
        f"pid: {os.getpid()}, "
        f"{pac} random delay time {_delay_val}")


def mhs_run(env, val):
    yield env.process(sync_clock(env, val))
    env.process(random_delay(env,val))


def f_run(q):
    SimConfig.NAME_SIM = 'Consum'
    print(
        f"pid: {os.getpid()}, "
        f"sim name {SimConfig.NAME_SIM}:")
    env = Environment()
    while True:
        _val = q.get()
        if _val is None:
            break
        env.process(mhs_run(env, _val))
    env.run()
