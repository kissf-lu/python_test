# -*- coding: utf-8 -*-


"""
==================================================================================================================================================
                                                     杭州HUB仿真项目

                                    项目启动日期：2017年7月6日
                                    项目启动标识：AIRPORT OF EZHOU'S PROJECT  -- HZ
                                    ===========================================
                                    代码创建日期：2017年7月6日
                                    代码创建工程师：谈和，元方，赵鹏，卢健
                                    代码版本：1.0
                                    版本更新日期：2017年7月11日
                                    版本更新工程师：卢健

                                    代码整体功能描述：预分拣模块，
                                                      1、完成预分拣模块的货物处理逻辑；



==================================================================================================================================================
"""


from tool import Package
from random import choice


class LogicTest(object):
    """"""

    def __init__(self, env, test_cls, config):
        self.env = env
        self.test_cls = test_cls
        self.config = config
        self.pipline = {}
        self.pipline_dic = {}
        self.path = []

    def _path_gen(self):
        """"""
        for o in self.config.ID_LAST_MACHINE:
            tmp1 = []
            for t in self.config.ID_TEST_MACHINE:
                tmp1.append((o, t))  # (''.join([o,'_', t]))
                tmp2 = []
                for d in self.config.ID_NEXT_MACHINE:
                    tmp2.append((t, d))  # (''.join([t, '_', d]))
                    self.path.append((o, t, d))
                self.pipline_dic[t] = tmp2
            self.pipline_dic[o] = tmp1

    def _pipline_generator(self):
        for v in self.pipline_dic.values():
            self.pipline.update({it: self.config.TYPE_PIP_LINE for it in v})

    def generator(self):
        """"""
        self._path_gen()
        self._pipline_generator()

    def packages_generator(self):
        """"""
        for num in range(self.config.NUM_PACKAGES):
            yield self.env.timeout(self.config.INTERVAL_TIME)
            package = Package(self.env, None, str(num), choice(self.path))
            package.pop_mark()
            print(package.next_pipeline)
            pipline_value = self.pipline[
                package.next_pipeline](self.env, 10,package.next_pipeline)
