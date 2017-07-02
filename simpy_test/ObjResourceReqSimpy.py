# -*- coding: utf-8 -*-
from simpy import Environment, Interrupt, Resource
import time


class Car(object):
    def __init__(self, car_env):
        self.car_env = car_env
        self.action = car_env.process(self.run_car())

    def run_car(self):
        """
        
        :return: 
        """
        while True:
            print('Start parking and charging at %d' % self.car_env.now)
            charge_duration = 5
            # We yield the process that process() returns
            # to wait for it to finish
            try:
                yield self.car_env.process(self.charge(charge_duration))
            except Interrupt:
                # When we received an interrupt, we stop charging and
                #  switch to the "driving" state
                print('Was interrupted. Hope, the battery is full enough ...')
            # The charge process has finished and
            # we can start driving again.
            print('Start driving at %d' % self.car_env.now)
            trip_duration = 2
            yield self.car_env.timeout(trip_duration)

    def charge(self, duration):
        yield self.car_env.timeout(duration)

    def driver(self):
        yield self.car_env.timeout(4)
        self.action.interrupt()


def car_req(env, name, bcs, driving_time, charge_duration):
    # Simulate driving to the BCS
    yield env.timeout(driving_time)
    # Request one of its charging spots
    print('%s arriving at %d' % (name, env.now))
    with bcs.request() as req:
        yield req
        #  Charge the battery
        print('%s starting to charge at %s' % (name, env.now))
        yield env.timeout(charge_duration)
        print('%s leaving the bcs at %s' % (name, env.now))


def resource_run(env):
    begin_t = time.time()
    car_arrive_gap = 0
    bcs = Resource(env, capacity=2)
    for i in range(6):
        car_arrive_time = car_arrive_gap
        env.process(car_req(env, 'Car %d' % i, bcs, car_arrive_time, 5))
    env.run()
    run_t =time.time() - begin_t
    print(run_t)


if __name__ == '__main__':
    env = Environment()
    resource_run(env)
    # car = Car(env)
    # # env.process(car.driver())
    # # car.driver()
    # # env.run(until=50)