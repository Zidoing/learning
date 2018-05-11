#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 26/02/2018.


class _const:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "can change % s" % name

        if not name.isupper():
            raise self.ConstCaseError, "uppper case %s " % name

        self.__dict__[name] = value


import sys

sys.modules[__name__] = _const


if __name__ == '__main__':
    print sys.modules

    import constant
    constant.COmpany = "IBM"
    print dir(constant) 
    constant.COmpany = "IBxM"
    print constant
    print dir(constant)
    print constant.COmpany