from simpy import Environment, Resource


def print_stats(res):
    print(print('%d of %d slots are allocated.' % (res.count, res.capacity)))
    print('  Users:', res.users)
    print('  Queued events:', res.queue)


def user(res):
    print('in')
    with res.request() as req:
        yield req
        print_stats(res)
    print('out')


if __name__  == '__main__':
    env = Environment()
    res = Resource(env, capacity=2)
    for i in range(5):
        env.process(user(res))
    # procs = [env.process(user(res)), env.process(user(res))]
    env.run()
