from simpy import Environment, Resource


def print_stats(res):
    print('%d of %d slots are allocated.' % (res.count, res.capacity))
    print('  Users:', res.users)
    print('  Queued events:', res.queue)


def user(env, res, name):
    """
    
    """
    with res.request() as req:
        #  每个req的yield迭代两个list: server queue, waiting queue,
        #  每次服务队列迭代server queue 获取在一次
        yield req
        print(name, 'uer obj is--->', res.users[0], 'at', env.now)
        #  capacity个request都延迟1秒才能释放资源，
        #  with内的yield timeout 用于阻塞正在服务的request一段时间才释放，
        #  释放后被阻塞的waiting request 立即获得服务资源
        yield env.timeout(5)
        print(name, 'out with', env.now)
    #  with外的yield timeout不会阻塞waiting request获得服务资源,
    #
    yield env.timeout(2)
    print(name, 'out process_func at',env.now)


def multi_process(env, res):
    num = 0
    while True:
        # yield env.timeout(1)
        env.process(user(env, res, num))
        num += 1
        if num >= 10:
            break


if __name__  == '__main__':
    env = Environment()
    res = Resource(env, capacity=5)
    #  env.process_func(multi_process(env, res))
    multi_process(env, res)
    env.run(until=15)
