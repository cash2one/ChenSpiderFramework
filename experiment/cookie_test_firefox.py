#! /usr/bin/evn python
#coding:utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

import time
from lxml import etree



# 需要有chrome有头浏览器和chromedriver

# 已经实现的功能：
# 1.显式等待
# 2.隐式等待
# 3.点击获取链接
# 4.获取渲染后的页面
# 可以实现但并未实现的功能
# 1.滑动验证破解

class firefox_selenium():

    # 绑定类参数，在实例化时需要传入(建议使用key=value传值模式)：
    # chrome的路径：chrome_dirver_path
    def __init__(self, dp):
        self.dirver_path = dp

    # 将初始化selenium使chrome_headless生效
    # 返回值self.chen_opener为入口
    def link_selenium(self):
        # dcap = dict(DesiredCapabilities.PHANTOMJS)
        # dcap["phantomjs.page.settings.userAgent"] = (
        #     "Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)")
        # self.chen_opener = webdriver.PhantomJS(desired_capabilities=dcap, executable_path = self.dirver_path )
        self.chen_opener = webdriver.Firefox( executable_path = self.dirver_path )
        return self.chen_opener


    # 模拟登录
    def cookies_get(self, the_url, username, password):
        # self.chen_opener.get(the_url)

        # 登录页面
        # login_url = self.chen_opener.find_element_by_xpath("//a[@id='cj_yaodai_loginUrl']/@href")

        self.chen_opener.get(the_url)

        # 获取登录信息框
        # username_input = self.chen_opener.find_element_by_xpath("//input[@id='username']")
        # password_input = self.chen_opener.find_element_by_xpath("//input[@id='password']")
        username_input = self.chen_opener.find_element_by_id("username")
        password_input = self.chen_opener.find_element_by_id("password")

        print password_input
        print username_input

        # 发送信息
        username_input.send_keys(username)
        password_input.send_keys(password)

        enter_button = self.chen_opener.find_element_by_xpath("//button")
        enter_button.click()

        time.sleep(1)
        cookie = self.chen_opener.get_cookies()

        print "cookie is :"
        print cookie



if __name__ == '__main__':
    test1 =firefox_selenium(dp='/home/chenyu/chensf/geckodriver')
    test1.link_selenium()
    try:
        test1.cookies_get(the_url="https://passport.lianjia.com/cas/login?service=http://user.sh.lianjia.com/index/ershou",
                          username = "13071131373", password="qazwsx1234")

    finally:
        try:
            test1.chen_opener.quit()
            print '-----------------*-------------------'
            print '---***SELENIUM CLOSED SUCCESS!***---'
        except:
            print '!!!!!HORRIBLE! ClOSE FAIL! IF YOU DONT OPEN SELENIUM, IGNORE THIS MESSAGE!!!!!'
