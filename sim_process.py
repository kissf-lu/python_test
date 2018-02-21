#
"""多进程测试
"""
# ======================= sys import =================
import os
import time
from multiprocessing import Process, Pool, Queue, Manager 
# ======================== local import ==============
from mhs_sim.config import SimConfig
from mhs_sim.sim_data import f_gen
from mhs_sim.data_migra import f_run


def ctl_mul_pro():
    """
    """
    SimConfig.NAME_SIM = 'Sim'
    print(f"ctl center of {SimConfig.NAME_SIM} start!")
    process_list = list()
    q = Queue()
    process_list.append(Process(
        target=f_gen,
        args=(q,)))
    process_list.append(Process(
        target=f_run,
        args=(q,)))
        
    for mul_p in process_list:
        mul_p.start()
    for mul_p in process_list:
        mul_p.join()


def ctl_pool():
    """
    """
    SimConfig.NAME_SIM = 'Sim'
    print(f"sim name {SimConfig.NAME_SIM} start!")
    pl_val = []
    q = Manager().Queue()
    with Pool() as pl:
        pl_val.append(pl.apply_async(
            f_gen,
            (q,)
        ))
        pl_val.append(pl.apply_async(
            f_run,
            (q,)
        ))
        for re_val in pl_val:
            re_val.get()


def api_port(msg: str):
    """
    api for web sim
    """
    print(f"main api pid: {os.getpid()}, {msg}")
    ctl_pool()


if __name__ == '__main__':
    start = time.time()
    api_port(msg='multiprocess go!')
    print(f"run time: {time.time() - start}")
