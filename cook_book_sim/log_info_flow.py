#
from cook_book_sim.log_deco import deco_logging
import numpy as np

# np.random.seed(777)
log = deco_logging()


def log_one():
    log(f'** log_one start **')
    for _ in range(2):
        log(f'log_one * {np.random.randint(1,11)}')
        # pass


def log_tow():
    # log('** log_tow start **')
    for _ in range(2):
        # log(f'log_tow * {np.random.randint(11,20)}')
        pass


if __name__ == '__main__':
    log_one()
    log_tow()
