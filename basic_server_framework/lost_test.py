# -*- coding: utf-8 -*-

__author__ = 'Chen Yu'

'''
检测失败的详情数量
用法：在主方法下测试

'''

# TODO(chenyansu): 封装
# TODO(chenyansu) 对象的三个方法: 计数， 记录，抽样

import redis
import json

class test_tool(object):

    def __init__(self, key_name):
        self.num = 0

    # 链接redis
    def link_redis():
        chenpool = redis.ConnectionPool(host='r-2zefc71473d249c4.redis.rds.aliyuncs.com', port=6379,
                                        password='zhugeZHAOFANG1116', db=0)
        # pool= redis.ConnectionPool(host='127.0.0.1', port=6379, password='', db=0)
        global chenred
        chenred = redis.Redis(connection_pool=chenpool)
        print 'link to redis sueccess!'




    # 计数
    def chen_start(self, key_name):
        list_len =  chenred.llen(key_name)
        for i in range(list_len):
            self.chen_get(i)

            # 这里有两个问题
            # 抓到为空的和尝试失败的
            # 现在已经累计计数
        def chen_get(i):
            chen_value = chenred.lindex(key_name, i)
            # 转换json为dict
            chen_value = chen_value.decode('utf-8')
            chen_dict = json.loads(chen_value)

            print i
            print chen_dict['data']['source_url']

            try:
                print chen_dict['data']['house_title']

                if chen_dict['data']['house_title'] == '':
                    print 'find lost+' + chen_dict['data']['source_url']
                    # chenred.lpushx(key_name+'_lost', chen_dict['source_url'])
                    global num
                    num = num +1
                    print 'lost_numbers is ' + str(num)
            except:
                print i
                print 'find some error : Maybe because is outnumer 100 times try'
                print 'find lost+' + chen_dict['data']['source_url']
                global num
                num = num + 1
                print 'lost_numbers is '+str(num)
                chen_get(i + 1)
        chen_get(i)



if __name__ == "__main__":

    print 'start!'
    link_redis()
    chen_start('changchun-Anjuke')
    print 'total_lost_numbers is ' + str(num)



