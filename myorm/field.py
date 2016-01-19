# !/usr/bin/env python
#  -*- coding: utf-8 -*-
'''
Created on 16/1/18 下午6:50

@author: yalei
'''

import time

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


class CharField(Field):
    def __init__(self, val = ''):
        Field.__init__(self, val)
        self.val = str(val)

    def parse2db(self):
        if self.val == None:
            return 'NULL'
        else:
            return "'%s'" %self.val

class LongTextField(Field):
    def __init__(self, val = ''):
        Field.__init__(self, val)
        self.val = str(val)

    def parse2db(self):
        if self.val == None:
            return 'NULL'
        else:
            return "'%s'" %self.val

class IntegerField(Field):
    def __init__(self, val = 0):
        Field.__init__(self, val)
        self.val = int(val)

class FloatField(Field):
    def __init__(self, val = 0.0):
        Field.__init__(self, val)
        self.val = float(val)

class BooleanField(Field):
    def __init__(self, val = False):
        Field.__init__(self, val)
        self.val = int(val) == 0

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
        self.val = time.strptime(val, '%Y-%m-%d')

    def parse2db(self):
        if self.val == None:
            return 'NULL'
        else:
            return "'%s'" %time.strftime('%Y-%m-%d', self.val)



# d = DateField(time.localtime())
