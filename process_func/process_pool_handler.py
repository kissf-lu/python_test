from multiprocessing import Pool, Process
import time
import os

flag = False

def art_add(x, y, sleep):

    print(f'call pid {os.getpid()}')
    time.sleep(sleep)

    print(f'{sleep}',time.time())
    return x+y


def mk_handler():
    asc = 0
    def handler(result):
        nonlocal asc
        asc += 1
        print('[{}]-[{}] CallBack Got {}'.format(os.getpid(), asc, result))

    return handler

def mk_generator_handler():
    sequence = 0
    while True:
        result = yield  #yield 记住并每次返回send传入的result
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


def loop_process():
    def process_loop(res):
        asc = 0
        while asc <= 2:
            asc += 1
            print('[{}]-[{}] CallBack Got {}'.format(os.getpid(), asc, res))

    return process_loop


def main():
    # handler = mk_handler()
    result = []
    run_time = time.time()
    handler_loop = mk_generator_handler()
    next(handler_loop)  # next方法调用生成器的__next__方法，send方法会让生成器继续执行
    p_g = Process(target=art_add, args=(1,2, 3), )
    # with Pool(processes=6) as pl:
    #     print(f'top pid {os.getpid()}')
    #     for i in range(4):
    #         res = pl.apply_async(func=art_add,
    #                              args=(i, i+1, i*i, flag, run_time),
    #                              callback=handler_loop.send,
    #                              error_callback=None)
    #
    #         result.append(res)
    #     for res in result:
    #         print('Got {}'.format(res.get()))


if __name__ == '__main__':
    main()
