#! /usr/bin/env python
# coding:utf-8


"""
本程序可能需要sudo运行！
"""

import os

def add_centOS_repo():
    # f = open('/home/chenyu/junk/google-chrome.repo', 'w')
    f = open('/etc/yum.repos.d/google-chrome.repo', 'w')
    yum_chrome_information = \
r'''[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
~ '''
    f.write(yum_chrome_information)
    f.close()


def intall_chrome():
    os.system('sudo yum -y install google-chrome-stable --nogpgcheck')



if __name__ == "__main__":
    print '本程序可能需要sudo运行！'
    add_centOS_repo()
    intall_chrome()
