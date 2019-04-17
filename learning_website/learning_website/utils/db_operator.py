# -*- coding: utf-8 -*-
"""
__author__ = 'peter'
__mtime__ = '2019-03-05'
# Follow the master,become a master.
             ┏┓       ┏┓
            ┏┛┻━━━━━━━┛┻┓
            ┃    ☃      ┃
            ┃  ┳┛   ┗┳  ┃
            ┃     ┻     ┃
            ┗━┓       ┏━┛
              ┃       ┗━━━━┓
              ┃ 神兽保佑     ┣┓
              ┃　永无BUG！   ┏┛
              ┗┓┓┏━━━┳┓┏━━━┛
               ┃┫┫   ┃┫┫
               ┗┻┛   ┗┻┛
"""
import pymysql
from learning_website.settings import dev


class MysqlHelper:
    def __init__(self):
        self._user = dev.user
        self._password = dev.passwd
        self._charset = 'utf8'
        self._port = dev.port
        self._host = dev.host
        self._db_name = dev.db
        self._conn = self.connect_mysql()
        if self._conn:
            self._cursor = self._conn.cursor()

    def connect_mysql(self):
        """
        连接数据库
        :return:
        """
        conn = pymysql.connect(host=self._host,
                               user=self._user,
                               passwd=self._password,
                               db=self._db_name,
                               port=self._port,
                               cursorclass=pymysql.cursors.DictCursor,
                               charset=self._charset,
                               )
        return conn

    def close(self):
        """
        关闭数据库连接
        :return:
        """
        self._cursor.close()
        self._conn.close()

    def execute(self, *args, params=None):
        """
        执行多条sql
        :param params:
        :param args:
        :return:
        """
        if params is None:
            params = []
        effect = 0
        for sql in args:
            num = self._cursor.execute(sql, params)
            effect += num
        self._conn.commit()
        self.close()
        return effect

    def select_multi(self, *args, params=None):
        """
        查询语句，可以执行多条查询
        :param args:
        :param params:
        :return: 返回元祖res：结果，num查询出行数
        """
        if params is None:
            params = []
        i = 1
        res = {}
        for sql in args:
            num = self._cursor.execute(sql, params)
            sql_results = self._cursor.fetchall()
            res['result%s' % i] = sql_results
            res['effect%s' % i] = num
            i += 1
        self.close()
        return res

    def select(self, sql, act='all',params=None):
        """
        查询语句方法
        :param act:
        :param sql:
        :param params:
        :return: 返回元祖res：结果，num查询出行数
        """
        global res
        if params is None:
            params = []
        if act == 'all':
            num = self._cursor.execute(sql, params)
            sql_results = self._cursor.fetchall()
            res = {
                'result': sql_results,
                'effect': num
            }
        self.close()
        return res


