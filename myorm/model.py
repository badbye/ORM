# !/usr/bin/env python
#  -*- coding: utf-8 -*-
'''
Created on 16/1/18 下午4:06

@author: yalei
'''


from field import *

class MetaModel(type):
    def __new__(cls, clsname, bases, dct):
        attrs = {}
        structure = []
        values = []
        for key, val in dct.iteritems():
            if isinstance(val, Field):
                attrs[key] = val.val
                structure.append((key, val.__class__))
                values.append((key, val.parse2db()))
            else:
                attrs[key] = val
        attrs['structure'] = dict(structure)
        return super(MetaModel, cls).__new__(cls, clsname, bases, attrs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

class Model(dict):
    __metaclass__ = MetaModel

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
        self.__slots__ = self.structure.keys()

    # def parse2db(self):
    #     res = {}
    #     for key, field in self.structure.iteritems():
    #         res[key] = field(self.__getattr__(key)).parse2db()
    #     return res

    def __str__(self):
        res = 'Table Structure:\n'
        res += '\n'.join('%10s: %s'%(k, v.__name__) for k, v in self.structure.iteritems())
        return res

    __repr__ = __str__



