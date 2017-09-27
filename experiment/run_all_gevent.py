# -*- coding: utf-8 -*-
import sys
import time
import os

from gevent import monkey; monkey.patch_socket()
import gevent.monkey


# sys.path.append("../../../../../")
# from blackwidow.bin.run import Blasckwidow
#
ajk_list=['zc','lsj','tpy']
#
# def chen_start_remote(c):
#     Blasckwidow(channel="anjuke", city="qingdao", type="sell", jobtype="details", page_type="all", channel_son="%s" %c)
#
#
# def chen_start_local(c):
#     Blasckwidow(channel="anjuke", city="qingdao", type="sell", jobtype="details", page_type="all", run_type="test",
#                 channel_son="%s" % c)

def chen_test(c):
    print 'Blasckwidow(channel="anjuke", city="qingdao", type="sell", jobtype="details", page_type="all", channel_son=%s)' %c
    time.sleep(10)
    print 'Blasckwidow(channel="anjuke", city="qingdao", type="sell", jobtype="details", page_type="all",run_type="test", channel_son=%s)' %c
    # for num in range(10):
    #     print num
    #     time.sleep(0.5)


if __name__ == '__main__':
    # os.system(r"""ps -ef|grep run_all|grep -v grep|awk '{print "kill -9 "$2}'|sh""")
    # print "已经杀死旧的进程以备重启"
    # p = Pool(len(ajk_list))
    # for i in ajk_list:
    #     p.apply_async(chen_test, args=(i,))
    # p.close()
    # p.join()
    # tasks = [ gevent.spawn(chen_test, i) for i in ajk_list]
    # gevent.joinall(tasks)

    gevent.joinall([
        gevent.spawn(chen_test, 'zc'),
        gevent.spawn(chen_test, 'lsj'),
        gevent.spawn(chen_test, 'tpy'),
    ])
    # for i in ajk_list:
    #     chen_test(i)
    #     gevent.sleep(0)
    print 'All subprocesses done.'