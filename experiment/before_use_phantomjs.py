#! /usr/bin/env python
# coding:utf-8

import os

# def before_use():
#     if os.path.isfile("phantomjs") is True:
#         print "phantomjs 已经解压！"
#     else:
#     	os.system('tar -xzvf phantomjs-2.1.1-linux-x86_64.tar.gz ')
#         print "解压完成"
#     	os.system('mv ./phantomjs*/bin/phantomjs ./')
#     	print "成功！可以使用PhantomJS抓取JS渲染的文件了！"


def before_use():
    the_phantomjs = str(os.path.expandvars('$HOME')) +'/phantomjs/phantomjs'
    if os.path.exists(the_phantomjs) is True:
        print "phantomjs 已经存在！"
        os.system("rm -rf ~/phantomjs/phantomjs*/")
    else:
        print "hehe"
        if os.path.exists('~/phantomjs/') is False:
            os.system("mkdir ~/phantomjs/")
        os.system("wget -P ~/phantomjs/ https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2")
        os.system('tar -jxvf ~/phantomjs/phantomjs-2.1.1-linux-x86_64.tar.bz2 -C ~/phantomjs ')
        print "解压完成"
        os.system('mv ~/phantomjs/phantomjs*/bin/phantomjs ~/phantomjs')
        print "成功！可以使用PhantomJS抓取JS渲染的文件了！"




if __name__ == '__main__':
    print "欢迎使用PhantomJS渲染JavaScript!"
    before_use()
