# -*- coding: utf-8 -*-


# from numpy.random import choice
import random as rm
import simpy
MAX = 10


class Fab(object):
    """
    Fab Class Sim Fab iter
    """
    def __init__(self, max_f=3):
        """
        Arg:
           max_f: max num of iter
        param max_f: 
        """
        self.n = 0
        self.a = 0
        self.b = 1
        self.max = max_f

    def __str__(self):
        return str(self.__doc__)

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a+self.b
            self.n = self.n + 1
            return r
        raise StopIteration()


def fab(iter_max):
    n, a, b = 0, 0, 1
    while n < iter_max:
        yield b
        a, b, = b, a+b
        n += 1


def process_sim(env, while_max):
    n = 0
    while n < while_max:
        print('enter while num:', n, 'at', env.now)
        yield env.timeout(2.7)
        n += 1


class CarBcs(object):
    """
    
    """
    def __init__(self, env, max_car, car_arrive_time):
        self.env = env
        self.bcs_res = simpy.Resource(env, capacity=2)
        self.car_max = max_car
        self.car_arrive_t = car_arrive_time
        self.bcs = env.process(self.resource_bcs())

    def resource_bcs(self):
        """
        
        :param num_bcs: 
        :param bsc_resources: 
        :return: 
        """
        for i in range(self.car_max):
            print('%0d car arrive at %s' % (i,self.env.now))
            self.env.process(self.car(i, self.bcs_res))
            car_arrive_t = rm.uniform(self.car_arrive_t, 10)
            yield self.env.timeout(car_arrive_t)

    def car(self, name, bcs_source):
        """
        
        :return: 
        """
        with bcs_source.request() as rq:
            yield rq
            print('%s charging at %s' % (name, self.env.now))
            charge_dur = rm.uniform(10, 30)
            yield self.env.timeout(charge_dur)
            print('%s charge end at %s' % (name, self.env.now))

    def run(self):
        self.env.run()

if __name__ == '__main__':
    rm.seed(7)
    env = simpy.Environment()
    bsc = CarBcs(env, 5, 2)
    bsc.run()

