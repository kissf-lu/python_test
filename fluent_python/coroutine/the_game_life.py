#
from collections import namedtuple
import itertools as it


ALIVE = 'O'
EMPTY = '_'
TICK = object()
Query = namedtuple('Query', 'y x')
Transition = namedtuple('Transition', 'y x state')


class Grid(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY]*self.width)

    def __str__(self):
        str_rows = [' '.join(self.rows[i]) for i in range(self.height)]
        return '\n'.join(str_rows)

    def query(self, y, x):
        return self.rows[y%self.height][x%self.width]

    def assign(self, y, x , state):
        self.rows[y%self.height][x%self.width] = state


def count_neighbors(y, x):
    n_ = yield Query(y+1, x+0)
    ne = yield Query(y+1, x+1)
    e_ = yield Query(y+0, x+1)
    se = yield Query(y-1, x+1)
    s_ = yield Query(y-1, x+0)
    sw = yield Query(y-1, x-1)
    w_ = yield Query(y+0, x-1)
    nw = yield Query(y+1, x-1)
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count


def game_logic(state, neighbors):
    if state is ALIVE:
        if neighbors < 2:
            return EMPTY
        elif neighbors > 3:
            return EMPTY
    else:
        if neighbors == 3:
            return ALIVE
    return state


def step_cell(y, x):
    state = yield Query(y, x)
    neighbors = yield from count_neighbors(y, x)
    next_state = game_logic(state, neighbors)
    yield Transition(y, x, next_state)


def sim(height, width):
    while True:
        for y in range(height):
            for x in range(width):
                yield from step_cell(y, x)
        yield TICK
        # print('ok')


def live_a_generation(grid, sim):
    progeny = Grid(grid.height, grid.width)
    item = next(sim)
    while item is not TICK:
        if isinstance(item, Query):
            state = grid.query(item.y, item.x)
            item = sim.send(state)
        else:
            progeny.assign(item.y, item.x, item.state)
            item = next(sim)
    return progeny


class ColumnPrinter(object):
    def __init__(self):
        self.columns = []

    def __str__(self):
        str_print = zip(*[self.columns[i].split('\n')
                          for i in range(len(self.columns))])
        return


if __name__ == '__main__':
    grid = Grid(5, 9)
    grid.assign(0, 2, ALIVE)
    grid.assign(1, 4, ALIVE)
    grid.assign(2, 2, ALIVE)
    grid.assign(2, 3, ALIVE)
    grid.assign(2, 4, ALIVE)
    columns = ColumnPrinter()
    sim = sim(grid.height, grid.width)
    for _ in range(5):
        # print('in')
        columns.columns.append(str(grid))
        # print(columns.columns)
        grid = live_a_generation(grid, sim)
    # for r in columns.columns
    str_print = zip(*[columns.columns[i].split('\n')
                      for i in range(grid.height)])
    # print(list(str_print))
    for r in str_print:
        str_ = '|'.join(r)
        print(str_)
