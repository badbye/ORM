# !/usr/bin/env python
#  -*- coding: utf-8 -*-
'''
Created on 16/1/18 下午4:31

@author: yalei
'''

import MySQLdb

class MysqlDB():
    autocommit = True
    conn = None

    @classmethod
    def connect(cls, **db_config):
        config = {}
        config['host'] = db_config.get('host', 'localhost'),
        config['port'] = db_config.get('port', 3306),
        config['user'] = db_config.get('user', 'root'),
        config['passwd'] = db_config.get('password', ''),
        config['db'] = db_config.get('database', 'test'),
        config['charset'] = db_config.get('charset', 'utf8')
        cls.cli = MySQLdb.connect(**config)
        cls.cli.autocommit(cls.autocommit)

    @classmethod
    def get_connection(cls):
        if not cls.conn or not cls.conn.open:
            cls.connect()
        try:
            cls.conn.ping()
        except MySQLdb.OperationalError:
            cls.connect()
        return cls.conn

    @classmethod
    def executes(cls, *args):
        cursor = cls.get_connection().cursor()
        cursor.execute(*args)
        return cursor

    def __del__(self):
        if self.conn and self.conn.open:
            self.conn.close()


# MysqlDB().connect({})
'''
MetaClass: 创建class的class
'''

class Field():
    pass


class MetaModel(type):
    def __new__(cls, clsname, bases, attrs):
        __table__ = cls.__table__
        for key, val in attrs.iteritems():
            if isinstance(val, Field):
                pass
        attrs['__table__'] = __table__
        return type.__new__(cls, clsname, bases, attrs)



class Model(dict):
    __metaclass__ = MetaModel

    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value