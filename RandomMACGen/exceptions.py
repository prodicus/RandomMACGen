# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-05-19 09:46:25
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-05-19 10:32:46
# @MIT License
# @http://tasdikrahman.me

class MACGenError(Exception):
    """A MACGen related error
    Will be the parent class for the other exceptions
    """

    def __call__(self, *args):
        return self.__class__(*(self.args + args))


class NegativeInput(MACGenError):
    """Raised when the input of devices passed is less than 0"""
