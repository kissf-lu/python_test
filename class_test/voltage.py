# -*- coding: utf-8 -*-


class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        # print(f'v: {self.voltage}')
        self.current = 0
        print(f'c : {self.current}')


class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0
        self._current = 0

    # # This makes it possible to create read-only properties easily using property() as a decorator
    @property
    def voltage(self):
        return self._voltage
    #
    @voltage.setter
    def voltage(self, voltage):
        print('setter')
        self._voltage = voltage
        self.current = self._voltage / self.ohms
        print(f'set current: {self.current}')

    # @property
    # def current(self):
    #     print('return_c')
    #     return self._current

    # @current.setter
    # def current(self, current):
    #     self._current = current

def run_resistor():
    r1 = VoltageResistance(5e3)
    # print(r1.voltage)
    # r1.voltage = 10
    print(r1.__dict__)
    # print(r1.voltage)
    # print(r1.voltage)
    # r1.voltage = 20
    # print(r1.current, r1.voltage)


if __name__ == '__main__':
    run_resistor()