import timeit
import random


if __name__ == "__main__":
    popend = timeit.Timer("x.pop()","from __main__ import x")
    x = list(range(2000000))
    print(popend.timeit(number=1000))
