#! /usr/bin/env python
# coding:utf-8

from global_manager import globaler

gol = globaler()
gol.start()
gol.set_value('CODE','UTF-8')
gol.set_value('PORT',80)
gol.set_value('HOST','127.0.0.1')