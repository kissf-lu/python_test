# -*- coding: utf-8 -*-


class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0
        print(f'0: {self.current}')


class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0
        self._current = 0
        print(f'1: {self._current}')

    # This makes it possible to create read-only properties easily using property() as a decorator
    @property
    def voltage(self):
        print(f'p return: {self._voltage}')
        return self._voltage

    # @property
    # def current(self):
    #     print('return_c')
    #     return self._current

    @voltage.setter
    def voltage(self, voltage):
        print('setter',voltage)
        self._voltage = voltage
        self.current = self._voltage / self.ohms
        print(f'set current: {self.current}')

    # @current.setter
    # def current(self, current):
    #     self._current = current

def run_resistor():
    r1 = VoltageResistance(5e3)
    r1.voltage = 10
    r1.voltage = 20
    # print(r1.current, r1.voltage)


if __name__ == '__main__':
    run_resistor()