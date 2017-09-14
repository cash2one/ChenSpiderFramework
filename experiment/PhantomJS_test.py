#! /usr/bin/evn python
#coding:utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

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

class chrome_headless():

    # 绑定类参数，在实例化时需要传入(建议使用key=value传值模式)：
    # chrome的路径：chrome_dirver_path
    def __init__(self, dp):
        self.dirver_path = dp

    def link_selenium(self):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)")
        self.chen_opener = webdriver.PhantomJS(desired_capabilities=dcap, executable_path = self.dirver_path )
        return self.chen_opener


    # 接受一个网址，返回js渲染后的源码
    def chen_js_get(self, the_url):
        self.chen_opener.get(the_url)
        self.js_response = self.chen_opener.page_source
        self.chen_opener.close()
        return self.js_response




    # 显式等待页面跳转
    # 获取the_url链接的内容，指定秒后获取id为content的某值
    # 传入参数:
    # 指定秒：wait_time
    # 获取链接：the_url
    # 想要获取的元素xpath表达式：want_X
    def explicit_wait_X(self, wait_time, the_url, want_X):
        self.chen_opener.get(the_url)
        time.sleep(wait_time)
        the_value = self.chen_opener.find_element_by_xpath(want_X).text
        print the_value
        self.chen_opener.close()
        return the


    # 隐式等待xpath版
    # 当获取到wait_X的元素时，获取want_X的text()值
    # 传入参数：
    # 原始url: the_url
    # 等待出现的元素：wait_X
    #
    def implicit_wait_X(self, the_url, wait_X, want_X):
        self.chen_opener.get(the_url)
        try:
            element = WebDriverWait(self.chen_opener, 10).until(
                EC.presence_of_element_located((By.XPATH, wait_X)))
        finally:
            the_value = self.chen_opener.find_element_by_xpath(want_X).text
            print the_value
            self.chen_opener.close()
            return the_value


    # 模拟点击，获取点击后的链接
    # 传入参数：
    # 原始url: the_url
    # 将要点击的元素：want_X
    def js_click_for_get_url(self, the_url, want_X):
        self.chen_opener.get(the_url)
        need_click = self.chen_opener.find_element_by_xpath(want_X)
        need_click.click()

        want_url = self.chen_opener.current_url
        print want_url
        self.chen_opener.close()
        return want_url



    # 所见即所得，只要你在浏览器看到什么，它就能抓到什么，哪怕源码里没有的
    # 以已经经过js渲染，开销巨大，慎用。
    def js_get_we_see(self, the_url, want_X):
        self.chen_js_get(the_url)
        s = etree.HTML(self.js_response)
        x = s.xpath(want_X)
        the_value = []
        for child in x:
            the_value.append(child)
        for i in the_value:
            print i
        return the_value



if __name__ == '__main__':
    # test1 = chrome_headless(dp='/home/chenyu/chensf/chromedriver')
    test1 = chrome_headless(dp='/home/chenyu/chensf/phantomjs')
    test1.link_selenium()
    try:
        # 显示等待测试
        # test1.explicit_wait_X(the_url='http://pythonscraping.com/pages/javascript/ajaxDemo.html',
        #                     want_X= "//*[@id='content']", wait_time= 3)

        #　隐式等待测试
        # test1.implicit_wait_X(the_url='http://pythonscraping.com/pages/javascript/ajaxDemo.html',
        #                       wait_X = "//*[@id='loadedButton']", want_X ="//*[@id='content']")

        # 点击跳转链接测试
        # test1.js_click_for_get_url(the_url='http://www.wxfcw.cn/newhouse/201709/872975/photos.html',
        #                want_X = "//span[text()='效果图']")

        # js　渲染后的元素获取测试
        test1.js_get_we_see(the_url='http://www.wxfcw.cn/newhouse/201709/872975/photos.html#caid=24',
                         want_X='//li//img/@src')
        # test1.js_get_we_see(the_url='http://www.wxfcw.cn/archive.php?aid=873056#g=1',
        #                  want_X=u"//dl/dt[text()='户型居室:']//following-sibling::dd[1]/text()")

    finally:
        try:
            test1.chen_opener.quit()
            print '-----------------*-------------------'
            print '---***SELENIUM CLOSED SUCCESS!***---'
        except:
            print '!!!!!HORRIBLE! ClOSE FAIL! IF YOU DONT OPEN SELENIUM, IGNORE THIS MESSAGE!!!!!'
