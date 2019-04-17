# -*- coding: utf-8 -*-
"""
__author__ = 'peter'
__mtime__ = '2019-04-17'
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
import datetime
import decimal


class ReturnFunc(object):

    @staticmethod
    def _handler(x):
        """
        处理函数
        :param x:
        :return:
        """
        if isinstance(x, datetime.datetime):
            return x.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(x, decimal.Decimal):
            return float(x)

    @staticmethod
    def visit_success(code=1001, msg='成功', data=None):
        """
        查询成功父方法
        :param code:
        :param msg:
        :param data:
        :return:
        """
        res = {'code': code, 'msg': msg, 'data': data}
        return res

    @staticmethod
    def visit_fail(code=4001, msg='失败'):
        """
        查询失败父方法
        :param code:
        :param msg:
        :return:
        """
        res = {'code': code, 'msg': msg}
        return res

    def list_success(self, page=None):
        """
        查询列表成功
        :param page:
        :return:
        """
        res = self.visit_success(code=1002, msg='查询成功！', data=None)
        res['page'] = page
        return res

    def retrieve_success(self, extra_data=None):
        """
        查询详情成功
        :param extra_data:
        :return:
        """
        res = self.visit_success(code=1003, msg='查找成功！', data=None)
        res['extra_data'] = extra_data
        return res
