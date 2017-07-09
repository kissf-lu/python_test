from simpy import Environment, Resource


def print_stats(res):
    print('%d of %d slots are allocated.' % (res.count, res.capacity))
    print('  Users:', res.users)
    print('  Queued events:', res.queue)


def user(env, res):
    yield env.timeout(2)
    print('in at', env.now)
    with res.request() as req:
        ack = yield req
        print(res.count, 'tag')
        print_stats(res)
        print('out')


if __name__  == '__main__':
    env = Environment()
    res = Resource(env, capacity=2)
    for i in range(5):
        env.process(user(env, res))
    # procs = [env.process(user(res)), env.process(user(res))]
    env.run()
