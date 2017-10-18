#
from cook_book_sim.decorator import log_out

log = log_out()


def log_one():
    log('log_one *1')
    log('log_one *2')


def log_tow():
    log('log_tow *1')
    log('log_tow *2')


if __name__ =='__main__':
    log_one()
    log_tow()