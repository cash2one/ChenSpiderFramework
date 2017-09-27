#! /usr/bin/env python
# coding:utf-8

class globaler():
    def start(self):#初始化
        global _global_dict
        _global_dict = {}


    def set_value(self, key,value):
        """ 定义一个全局变量 """
        _global_dict[key] = value


    def get_value(self, key, defValue=None):
        try:
            return _global_dict[key]
        except KeyError:
            return defValue

# gol = globaler()
# gol.start()
# gol.set_value('CODE','UTF-8')
# gol.set_value('PORT',80)
# gol.set_value('HOST','127.0.0.1')