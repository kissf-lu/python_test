from simpy import Environment, Resource


def print_stats(res):
    print('%d of %d slots are allocated.' % (res.count, res.capacity))
    print('  Users:', res.users)
    print('  Queued events:', res.queue)


def user(env, res):
    with res.request() as req:
        yield req
        print('req----->:', req, env.now)
        print('uer obj is--->', res.users[0], 'at', env.now)
        yield env.timeout(1)
        print_stats(res)
        print('out at', env.now)

    yield env.timeout(2)
    print('out with----------------------------------------------------', env.now)


if __name__  == '__main__':
    env = Environment()
    res = Resource(env, capacity=2)
    for i in range(6):
        env.process(user(env, res))
    env.run()
