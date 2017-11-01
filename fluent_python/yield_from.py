#


def gen_child():
    while True:
        rec = yield
        print(f'receive: {rec}')
        if rec is None:
            break
    print('Ending Gen of Child')
    return rec


def gen_proxy():
    while True:
        result = yield from gen_child()
        print(f'father receive: {result}')

# def main():
#     gen = gen_proxy()
#     next(gen)
#     gen.send
#     pass


# if __name__ == '__main__':
#     main()
