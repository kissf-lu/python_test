# -*- coding: utf-8 -*-
import simpy


def clock(environment, name, tick):
    while 1:
        print(name, environment.now)
        yield environment.timeout(tick)


def clock_run():
    env_clock = simpy.Environment()
    env_clock.process(clock(env_clock, 'fast', 0.5))
    env_clock.process(clock(env_clock, 'slow', 1))
    env_clock.run(until=2)


def car(env_car):
    while 1:
        print("Start parking at %d" % env_car.now)
        parking_duration = 3
        yield env_car.timeout(parking_duration)

        print("Start driving car at %d" % env_car.now)
        trip_duration = 5
        yield env_car.timeout(trip_duration)


def car_run():
    env_car = simpy.Environment()
    env_car.process(car(env_car))
    env_car.run(until=50)

if __name__ == '__main__':
    clock_run()
    car_run()