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


from simpy import Environment
from simpy import Store
from cross import Cross


class PackageGenerator(object):
    def __init__(self, env=Environment, num_package=None, interval_time=None):
        """"""
        self.env=env
        self.num_package = num_package
        self.interval_time = interval_time
        self.package_cls = None   #  为后续采用Package类预留


    def package_produce(self):
        """"""

