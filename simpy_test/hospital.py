# -*- coding: utf-8 -*-

"""
==================================================================================================================================================
                                                     杭州HUB仿真项目

                                    项目启动日期：2017年7月6日
                                    项目启动标识：AIRPORT OF EZHOU'S PROJECT  -- HZ
                                    ===========================================
                                    代码创建日期：2017年7月6日
                                    代码创建工程师：卢健
                                    代码版本：1.0
                                    版本更新日期：2017年7月6日
                                    版本更新工程师：卢健

                                    代码整体功能描述：医院区模块，
                                                    1、完成医院区的货物处理逻辑；



==================================================================================================================================================
"""


from simpy import Resource
from simpy import PriorityItem
from numpy.random import choice


class Hospital(object):
    def __init__(self, env, id_h, hospital_capacity: int=1,
                 input_dic: dict=None, output_dic: dict=None):
        """
        init class self args:
        Args:
            env: A simpy.Environment instance.
            id_h: Hospital machine id.
            hospital_capacity: The number of hospital resource(the same
            as the serving number of people)
            input_dic: input queue dic: {'queue1': PriorityStore, ...},.
            output_dic: output queue dic: {'queue1': PriorityStore, ...}.
        """
        self.env = env
        self.di_h = id_h
        self.hospital_capacity = hospital_capacity
        self.input_dic = input_dic
        self.output_dic = output_dic
        self.hospital_process = self._get_package_queue()

    def _get_package_queue(self):
        """
        获取输入队列功能单元
        """
        if self.input_dic:
            #  根据input_dic={}中key, value 对的数目， 分别创建process
            for queue_id, get_package_queue in self.input_dic.items():
                self.env.process(self._get_packages(queue_id,
                                                    get_package_queue))
        else:
            raise RuntimeError('Please Initial input port Queue '
                               'for Cross instance First!')

    def _get_packages(self, queue_id, get_package_queue):
        """
        """
        while True:
            packages = yield get_package_queue.get()
            # 判断取没取到货物
            if packages:
                self.env.process(self._resource_hospital(packages))

    def _resource_hospital(self, packages):
        """"""
        people_res = Resource(self.env, self.hospital_capacity)
        with people_res.request() as req:
            yield req
            self.env.process(self._put_packages_into_out_queue(packages))

    def _put_packages_into_out_queue(self, package):
        """
        """
        if self.output_dic:
            yield self.env.timeout(900)
            queue_id = str(choice(list(self.output_dic.keys())))
            print(f"------->package {package.item['package_id']}",
                  'was push into', queue_id, 'at', self.env.now)
            self.output_dic[queue_id].put(
                PriorityItem(priority=self.env.now, item=package))
