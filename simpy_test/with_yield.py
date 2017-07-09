

import collections
import random
import simpy


RANDOM_SEED = 42
TICKETS = 50  # Number of tickets per movie
SIM_TIME = 8  # Simulate until


def moviegoer(env, movie, num_tickets, theater):
    """A moviegoer tries to by a number of tickets (*num_tickets*) for
    a certain *movie* in a *theater*.

    If the movie becomes sold out, she leaves the theater. If she gets
    to the counter, she tries to buy a number of tickets. If not enough
    tickets are left, she argues with the teller and leaves.

    If at most one ticket is left after the moviegoer bought her
    tickets, the *sold out* event for this movie is triggered causing
    all remaining moviegoers to leave.

    """
    with theater.counter.request() as my_turn:
        # 顾客每隔1秒会来排队申请服务生资源（售票员）， 每一个客户对应一个process的处理事件
        # 资源池被动的根据顾客请求 按照 my_turn 服务资源(售票员)的能力(个数)， 提供给顾客几个服务
        # 每个顾客的process 都会加入 request 的queue队列资源池中, 等待正在被服务的user 顾客释放出
        # user的服务资源，以便获取服务。
        # 每个顾客的服务都是独立的进行的，受限的是服务的资源，只有有资源，顾客才能获得服务
        # 所以上一个顾客的服务时延会影响下一个顾客的服务时间。在同一时间点，越早的process会越先出
        # 现在服务的行中。
        print('*-', movie, 'request process at-->', env.now)
        yield my_turn
        # 申请得到资源的process开始处理事务
        print('**-', movie, 'request obtain process at-->', env.now)
        if movie == 'Kill Process':
            # Kill Process 电影多占用2秒处理时间
            # 每个yield 的 env 都对应每一个process
            yield env.timeout(2)
        # 所有电影都必须有1秒处理时间才能释放资源
        yield env.timeout(1)
        print('***-', movie, ' release process--at', env.now)


def customer_arrivals(env, theater):
    """Create new *moviegoers* until the sim time reaches 120."""
    while True:
        yield env.timeout(1)
        movie = random.choice(theater.movies)
        num_tickets = random.randint(1, 6)
        # print(movie, 'need', num_tickets, 'at', env.now)
        if theater.available[movie]:
            env.process(moviegoer(env, movie, num_tickets, theater))

Theater = collections.namedtuple('Theater', 'counter, movies, available, '
                                            'sold_out, when_sold_out, '
                                            'num_renegers')

# Setup and start the simulation
print('Movie renege')
random.seed(RANDOM_SEED)
env = simpy.Environment()

# Create movie theater
counter = simpy.Resource(env, capacity=1)
movies = ['Python Unchained', 'Kill Process', 'Pulp Implementation']
available = {movie: TICKETS for movie in movies}
sold_out = {movie: env.event() for movie in movies}
when_sold_out = {movie: None for movie in movies}
num_renegers = {movie: 0 for movie in movies}
theater = Theater(counter, movies, available, sold_out, when_sold_out,
                  num_renegers)

# Start process and run
env.process(customer_arrivals(env, theater))
env.run(until=SIM_TIME)
