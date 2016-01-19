# !/usr/bin/env python
#  -*- coding: utf-8 -*-
'''
Created on 16/1/18 下午6:50

@author: yalei
'''

import time
import warnings


class Field():
    def __init__(self, val = None):
        self.val = val

    def __str__(self):
        return str(self.val)

    def  __unicode__(self):
        return self.val

    def parse2db(self):
        if self.val == None:
            return 'NULL'
        else:
            return str(self.val)

    def _warn(self):
        if self.val != None:
            msg = 'Can not convert [%s] to %s, return None' %(self.val ,self.__class__.__name__)
            warnings.warn(msg)
            self.val = None

class CharField(Field):
    def __init__(self, val = ''):
        Field.__init__(self, val)
        if val == None:
            self.val = None
        else:
            try:
                self.val = str(val)
            except:
                self._warn()

    def parse2db(self):
        if self.val == None:
            return 'NULL'
        else:
            return "'%s'" %self.val

class LongTextField(Field):
    def __init__(self, val = ''):
        Field.__init__(self, val)
        if val == None:
            self.val = None
        else:
            try:
                self.val = str(val)
            except:
                self._warn()

    def parse2db(self):
        if self.val == None:
            return 'NULL'
        else:
            return "'%s'" %self.val

class IntegerField(Field):
    def __init__(self, val = 0):
        Field.__init__(self, val)
        try:
            self.val = int(val)
        except:
            self._warn()

class FloatField(Field):
    def __init__(self, val = 0.0):
        Field.__init__(self, val)
        try:
            self.val = float(val)
        except:
            self._warn()

class BooleanField(Field):
    def __init__(self, val = False):
        Field.__init__(self, val)
        try:
            self.val = int(val) == 0
        except:
            self._warn()

    def parse2db(self):
        if self.val == None:
            return 'NULL'
        elif self.val:
            return 1
        else:
            return 0

class DateField(Field):
    def __init__(self, val = '2016-01-01'):
        Field.__init__(self, val)
        try:
            if self.val == None:
                pass
            else:
                self.val = time.strptime(val, '%Y-%m-%d')
        except:
            self._warn()

    def parse2db(self):
        if self.val == None:
            return 'NULL'
        try:
            return "'%s'" %time.strftime('%Y-%m-%d', self.val)
        except:
            self._warn()
            return None


# d = DateField(time.localtime())
# d = CharField(None)
# print d.val
# print d.parse2db()
#
# d = IntegerField({1: 2, 3:4})
# print d.val
# print d.parse2db()