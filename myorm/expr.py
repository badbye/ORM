# !/usr/bin/env python
#  -*- coding: utf-8 -*-
'''
Created on 16/1/19 下午2:31

@author: yalei
'''

class Expr(object):
    def __init__(self, model):
        self.table = model.__table__
        self.values = model.values

    def insert(self):
        insert_temp = 'INSERT INTO TABLE {tb_name}({tb_keys}) VALUES ({tb_values})'
        sql = insert_temp.format(tb_name = self.table,
                                 tb_keys = ','.join(self.values.keys()),
                                 tb_values = ','.join(self.values.values())
                                 )
        return sql

    def update(self, **kwargs):
        update_temp = 'UPDATE {tb_name} SET {assignment} WHERE {condition}'
        sql = update_temp.format(tb_name = self.table,
                                 condition = self.parse_dict(self.values, sep = ' and '),
                                 assignment = self.parse_dict(kwargs)
                                 )
        return sql

    def parse_dict(self, dct, sep = ','):
        if len(dct) == 1:
            return '%s = %s' %(dct.keys()[0], dct.values()[0])
        elif len(dct) > 1:
            return sep.join('%s=%s'%(k, v) for k,v in dct.iteritems())
        return None

    def select(self):
        select_temp = ''
        sql = ''
        return sql



'''
insert:

insert into table %s(%s) values (%s) %(self.__table__, )
'''
