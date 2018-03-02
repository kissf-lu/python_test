#
from simpy import Environment
from random import Random,expovariate,uniform
import sys
import os
import time
from multiprocessing import Process, Pool, Queue, Manager
# ======================== local import ==============
from mhs_sim.config import SimConfig
from mhs_sim.sim_data import gen_pac, f_gen
from mhs_sim.data_migra import mhs_run


class Processor(object):
    def __init__(self):
        self.data_queue = Queue()
        # self.env = Environment(initial_time=0)

    def simulate(self):
        
        process_list = list()
        process_list.append(Process(
            target=self.gen_sim
        ))
        # process_list.append(Process(
        #     target=self.sonsum_sim
        # ))
        for mul_p in process_list:
            mul_p.start()
        for mul_p in process_list:
            mul_p.join()

    def gen_sim(self):
        """"""
        self.env = Environment(initial_time=0)
        self.env.process(gen_pac(self.env, self.data_queue))
        # # self.env.process(mhs_run(self.env, self.data_queue))
        self.env.run()

    def sonsum_sim(self):
        # self.env.process(gen_pac(self.env, self.data_queue))
        self.env.process(mhs_run(self.env, self.data_queue))
        self.env.run()

if __name__ == "__main__":
    pp = Processor()
    pp.simulate()
