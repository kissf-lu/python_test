# 
"""
sim module
"""
# ======================= sys import ==============
from simpy import Environment
import os
# ======================= local import =============
from .config import SimConfig
from .data_sch import Packages


def _gen_pac(env, data_q):
    for p in range(5):
        record = Packages(
            parcel_id=p,
            small_id=p, 
            timestamp=env.now)
        data_q.put(record)
        yield env.timeout(1)


def f_gen(q):
    env = Environment()
    SimConfig.NAME_SIM ='gen'
    print(f"simpy gen at {env.now}")
    print(
        f"pid: {os.getpid()}, "
        f"sim name {SimConfig.NAME_SIM}, "
        f"gen data start at {env.now}:")
    env.process(_gen_pac(env, q))
    env.run()

    q.put(None)
