#
"""多进程测试
"""
# ======================= sys import =================
import os
import time
from multiprocessing import Process, Pool, Queue, Manager
from simpy import Environment
# ======================== local import ==============
from mhs_sim.config import SimConfig
from mhs_sim.sim_data import f_gen, gen_pac
from mhs_sim.data_migra import f_run


def ctl_mul_pro():
    """
    """
    # print(f"ctl center of {SimConfig.NAME_SIM} start at {time.time()}")
    process_list = list()
    q = Queue()


    # env = Environment()
    # env.process(gen_pac(env, q))
    # env.run()

    process_list.append(Process(
        target=f_gen,
        args=(q,)))
    process_list.append(Process(
        target=f_run,
        args=(q,)))
    # process_list.append(Process(
    #     target=f_run,
    #     args=(q,)))
    
    for mul_p in process_list:
        mul_p.start()
    for mul_p in process_list:
        mul_p.join()


def ctl_pool():
    """
    """
    SimConfig.NAME_SIM = 'Sim'
    # print(f"sim name {SimConfig.NAME_SIM} start!")
    pl_val = []
    q = Manager().Queue()
    env = Environment()
    with Pool() as pl:
        pl_val.append(pl.apply_async(
            f_gen,
            (q, env)
        ))
        pl_val.append(pl.apply_async(
            f_run,
            (q,)
        ))
        pl_val.append(pl.apply_async(
            f_run,
            (q,)
        ))
        for re_val in pl_val:
            re_val.get()


def api_port(msg):
    """
    api for web sim
    """
    # print(f"main api pid: {os.getpid()}, {msg}")
    # ctl_pool()
    ctl_mul_pro()


if __name__ == '__main__':
    start = time.time()
    api_port(msg='multiprocess go!')
    print(
        "run time: {0},  at {1}".format(time.time() - start, time.time()))
