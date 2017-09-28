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
import sys
import os

from pyvirtualdisplay import Display


class firefox_selenium():

    # 绑定类参数，在实例化时需要传入(建议使用key=value传值模式)：
    # chrome的路径：chrome_dirver_path
    def __init__(self, dp):
        self.dirver_path = dp

    # 将初始化selenium使chrome_headless生效
    # 返回值self.chen_opener为入口
    def link_selenium(self):

        firefox_profile = webdriver.FirefoxProfile()
        # 禁用图片加载
        firefox_profile.set_preference('permissions.default.image', 2)  # 某些firefox只需要这个
        # 禁用css加载
        firefox_profile.set_preference('permissions.default.stylesheet', 2)
        # 禁用flash加载
        firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
        # 禁用js，不建议使用。
        # firefox_profile.set_preference('javascript.enabled', 'false')

        self.chen_opener = webdriver.Firefox( executable_path = self.dirver_path, firefox_profile=firefox_profile)
        return self.chen_opener


    # 模拟登录
    # 接口：
    # the_url: 登录页面url，如果弹出窗口，可以xpath抓链接，通常可以单独访问的
    # username: 账户名/邮箱/手机号等
    # password: 密码
    # username_X: 账户名/邮箱/手机号框的Xpath
    # password_X: 密码框的Xpath
    # login_X: 页面登录按钮，适合弹窗窗口
    # second_click_X: 有的登录页面需要切换窗口
    # iframe_name：有的登录窗口是iframe定位的

    # def cookies_get(self, the_url, username, password, login_X, username_X, password_X, confirm_button_X):
    def cookies_get(self, the_url, username, password, username_X, password_X, confirm_button_X, **kw):

        # self.chen_opener.set_page_load_timeout(20)
        self.chen_opener.get(the_url)
        time.sleep(0.5)

        # 点击进入登录窗口
        if "login_X" in kw:
            WebDriverWait(self.chen_opener, 10).until(EC.element_to_be_clickable((By.XPATH,kw["login_X"]))).click()
            time.sleep(0.5)

        # 如果是iframe框架，切换进入
        if "iframe_name" in kw:
            time.sleep(0.5)
            self.chen_opener.switch_to.frame(kw['iframe_name'])

        # 二次点击
        if "second_click_X" in kw:
            WebDriverWait(self.chen_opener, 10).until(EC.element_to_be_clickable((By.XPATH, kw["second_click_X"]))).click()

            # 拟人操作，因为人类不可能在打开新窗口后立即输入数据。
        time.sleep(3)

        # 获取登录信息框
        username_input = self.chen_opener.find_element_by_xpath(username_X)
        password_input = self.chen_opener.find_element_by_xpath(password_X)

        # 发送信息
        username_input.send_keys(username)
        password_input.send_keys(password)

        # 点击登录按钮
        WebDriverWait(self.chen_opener, 10).until(EC.element_to_be_clickable((By.XPATH,confirm_button_X))).click()
        time.sleep(1)


        if "login_X" in kw:
            try:
                self.chen_opener.find_element_by_xpath(kw["login_X"])
                print "登录失败，可能遭遇验证码！"
                self.chen_opener.quit()
                os._exit()
            except:
                print "页面发生变化，登录成功！正在为您获取cookies。(如若失败，可能遭遇反爬)"

        time.sleep(2)
        cookie = self.chen_opener.get_cookies()

        print "cookie is :"
        print cookie



if __name__ == '__main__':

    # display = Display(visible=0, size=(900, 800))
    # display.start()

    test1 =firefox_selenium(dp='/home/chenyu/chensf/geckodriver')
    test1.link_selenium()
    try:
        # 链接形式
        # test1.cookies_get(the_url="http://sh.lianjia.com/chengjiao",
        #                   username = "13071131373", password="qazwsx1234", username_X="//input[@id='user_name']",
        #                 password_X="//input[@id='user_password']", confirm_button_X="//a[@class='login-user-btn']", login_X="//a[@id='cj_yaodai_loginUrl']")

        # 直接输入
        # the_dict = {
        #     "the_url":"https://passport.lianjia.com/cas/login?service=http://user.sh.lianjia.com/index/ershou",
        #     # "login_X":
        #     "username" : "13071131373",
        #     "password" : "qazwsx1234",
        #     "username_X":"//input[@id='username']",
        #     "password_X":"//input[@id='password']",
        #     "confirm_button_X":"//button[@class='actDoSubmit basisyle btnStyle']"
        #
        # }
        # test1.cookies_get(** the_dict)

        # 百度测试(逻辑上成功，但是遭遇验证码！)：
        # the_dict = {
        #     "the_url":"https://www.baidu.com/s?ie=UTF-8&wd=%E7%99%BE%E5%BA%A6",
        #     "login_X":"//div[@id='u']//a[@name='tj_login']",
        #     "username" : "123",
        #     "password" : "1234",
        #     "username_X":"//input[@id='TANGRAM__PSP_10__userName']",
        #     "password_X":"//input[@id='TANGRAM__PSP_10__password']",
        #     "confirm_button_X":"//input[@id='TANGRAM__PSP_10__submit']",
        # }
        # test1.cookies_get(** the_dict)

        # 安居客
        the_dict = {
            "the_url":"https://login.anjuke.com/login/form",
            "second_click_X":"//*[@id='pwdTab']",
            # 二次点击时遭遇iframe，去源代码搜索iframe，找到iframe的名称
            "iframe_name":"iframeLoginIfm",
            "username" : "18513122061",
            "password" : "test12345",
            "username_X":"//input[@id='pwdUserNameIpt']",
            "password_X":"//input[@id='pwdIpt']",
            "confirm_button_X":"//input[@id='pwdSubmitBtn']",
        }
        test1.cookies_get(** the_dict)

        # 房天下
        # the_dict = {
        #     "the_url":"http://esf.cd.fang.com/loginnew1.aspx",
        #     # "login_X":"//a[@id='list_D01_02']",
        #     # # 有的时候会遭遇二次点击，即进了登录页面要从注册切换到登录
        #     # "second_click_X":"//*[@id='pwdTab']",
        #     # # 二次点击时遭遇iframe，去源代码搜索iframe，找到iframe的名称
        #     # "iframe_name":"iframeLoginIfm",
        #     "username" : "18513122061",
        #     "password" : "test12345",
        #     "username_X":"//*[@id='txt_username']",
        #     "password_X":"//*[@id='txt_password']",
        #     "confirm_button_X":"//input[@onclick='check(); return false;']",
        # }
        # test1.cookies_get(** the_dict)

        # 我爱我家
        # the_dict = {
        #     "the_url": "http://bj.5i5j.com/regLogin/login",
        #     # "login_X":"//a[@id='list_D01_02']",
        #     # # 有的时候会遭遇二次点击，即进了登录页面要从注册切换到登录
        #     # "second_click_X":"//*[@id='pwdTab']",
        #     # # 二次点击时遭遇iframe，去源代码搜索iframe，找到iframe的名称
        #     # "iframe_name":"iframeLoginIfm",
        #     "username": "18513122061",
        #     "password": "test12345",
        #     "username_X": "//*[@id='username']",
        #     "password_X": "//*[@id='password']",
        #     "confirm_button_X": "//button",
        # }
        # test1.cookies_get(**the_dict)



    finally:
        try:
            test1.chen_opener.quit()

            # display.stop()
            print '-----------------*-------------------'
            print '---***SELENIUM CLOSED SUCCESS!***---'
        except:
            print '!!!!!HORRIBLE! ClOSE FAIL! IF YOU DONT OPEN SELENIUM, IGNORE THIS MESSAGE!!!!!'
