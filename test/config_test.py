# -*- coding: utf-8 -*-


class Config(object):
    RANDOM_SEED = 42
    NUM_PACKAGES = 10
    INTERVAL_TIME = 10
    ID_PIP_LINE = 'store'

class PackageGenerator(Config):
    def __init__(self):
        self.num = Config.NUM_PACKAGES
        self.interval_time = Config.INTERVAL_TIME


class PipLine(Config):
    ID = Config.ID_PIP_LINE


class TestMachine(Config):
    ID = ['m1_1', 'm1_2', 'm1_3', 'm1_4']
    CAPACITY_RESOURCE = 2
    PROCESS_TIME = 10

class NextMachine(Config):
    ID = ['secondary_1', 'secondary_2', 'cross_1', 'cross_2', 'cross_3']

class Cross(Config):
    """"""
    random_seed = Config.RANDOM_SEED


class PresortConfig(Config):
    """"""


class UnLoadConfig():
    """"""

config_test = {
    'cross_config': Cross,
    'presort_config': PresortConfig
}
