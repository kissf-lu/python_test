from simpy import Environment, Resource


def print_stats(user_id, res, user_done):
    print('%d of %d slots are allocated.' % (res.count, res.capacity))
    print('  Users:', res.users)
    print('  Queued events:', res.queue)
    user_done.succeed(value=f'user {user_id} ok!')


def user(env, user_id, res):
    with res.request() as req:
        user_done = env.event()
        yield req
        yield env.timeout(1)
        print_stats(user_id, res, user_done)
        event_re = yield user_done
        print(event_re)
    # print('out with----------------------------', env.now)


if __name__  == '__main__':
    env = Environment()
    res = Resource(env, capacity=2)
    user_list = {i: env.process(user(env, i, res)) for i in range(3)}
    print(user_list[0].is_alive)
    env.run()
