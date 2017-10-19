#
from cook_book_sim.decorator import log_out
import numpy as np

np.random.seed(777)


log = log_out()


def log_one():
    for _ in range(2):
        log(f'log_one * {np.random.randint(1,11)}')
    log('log_one end!')


def log_tow():
    for _ in range(2):
        log(f'log_tow * {np.random.randint(11,20)}')
    log('log_tow end!')


if __name__ =='__main__':
    log_one()
    log_tow()
