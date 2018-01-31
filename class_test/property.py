# -*- coding: utf-8 -*-

from decimal import Decimal


########################################################################
class Fees(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.fee = None

    @property
    def fee(self):
        """
        The fee property - the getter
        """
        return self._fee

    # ----------------------------------------------------------------------
    @fee.setter
    def fee(self, value):
        """
        The setter of the fee property
        """
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value
        else:
            raise ValueError("no such fee expected!")

    @fee.deleter
    def fee(self):
        """"""
        del self._fee


from decimal import Decimal

########################################################################
class Feess(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        print('enter init')
        self._fee = None

    #----------------------------------------------------------------------
    def get_fee(self):
        """
        Return the current fee
        """
        return self._fee

    #----------------------------------------------------------------------
    def set_fee(self, value):
        """
        Set the fee
        """
        print('enter setter')
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value

    fee = property(get_fee, set_fee)



if __name__ == '__main__':
    # c = Parrot
    # c.voltage=10
    # print(c.voltage)
    # print(c.mro())
    # -------------------
    # f = Fees()
    # f.fee='2'
    # print(f.fee)
    # del (f.fee)
    fee=Feess()
    fee.fee='8'
    print(fee.fee)