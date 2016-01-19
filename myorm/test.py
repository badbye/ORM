# !/usr/bin/env python
#  -*- coding: utf-8 -*-
'''
Created on 16/1/19 上午10:45

@author: yalei
'''


from field import *
from model import Model
from expr import Expr

class User(Model):
    __table__ = 'user'
    id = IntegerField()
    char = CharField()
    date = DateField()
    def __repr__(self):
        return '<[id]: %s; [char]: %s; [date]: %s>' %(self.id, self.char, self.date)

class Hi(Model):
    __table__ = 'hi'
    hi = IntegerField()
    def __repr__(self):
        return '<hi: %s>' %self.hi


# hi = Hi(hi = 123)
# hi_expr = Expr(hi)
# print hi_expr.insert()
# print hi_expr.update(hi = 456)
#
# print '-' * 100
#
user = User()

print '-' * 100
user_expr = Expr(user)
print user_expr.insert()
print user_expr.update(id = 456)

print '-' * 100
print user.date
user.date = None
print user.date
user_expr = Expr(user)
print user_expr.insert()
print user_expr.update(id = 456)