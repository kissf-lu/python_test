# -*- coding: utf-8 -*-

import simpy
import random as rm


def generator_pack(env, pack_queue):
    i = 0
    while True:

        pack = simpy.PriorityItem(env.now, {'id':env.now, 'name': i})
        yield pack_queue.put(pack)
        print('%d package was put at %d' % (i, env.now))
        #  print('all packages num: ', len(issues.items))
        random_time = rm.randint(3,6)
        yield env.timeout(random_time)
        i += 1


def consumer_pack(env, pack_queue):
    while True:
        package = yield pack_queue.get()
        yield env.timeout(1)
        print('consumer time:', env.now, 'package id:', package.item['id'],  'package name ', package.item['name'])


if __name__ == '__main__':
    rm.seed(42)
    env = simpy.Environment()
    queue = simpy.PriorityStore(env)
    _ = env.process(generator_pack(env, queue))
    _ = env.process(consumer_pack(env, queue))
    env.run(until=10)