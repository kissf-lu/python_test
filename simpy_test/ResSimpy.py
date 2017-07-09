from simpy import Environment, Resource


def print_stats(res):
    print('%d of %d slots are allocated.' % (res.count, res.capacity))
    print('  Users:', res.users)
    print('  Queued events:', res.queue)


def user(env, res):
    with res.request() as req:
        print('req----->:', req)
        yield req
        print(f'{ack}  uer obj is--->', res.users[0])
        print_stats(res)
        print('out at', env.now)
        yield env.timeout(2)


if __name__  == '__main__':
    env = Environment()
    res = Resource(env, capacity=2)
    for i in range(5):
        env.process(user(env, res))
    env.run()
