from scrapy import downloadermiddlewares
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import ProxyType

import os

from lxml import etree


'''
用法：
粘贴到DownloadMiddleware中
在settings.py(zhuge是run.py)中注册
'''


class phantomJS_headless(object):

    @classmethod
    def process_request(cls, request, spider):
        some_proxy_IP = 'proxy_IP'
        ua = "UA"


        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "%s" %ua)

        # 关闭加载图片
        dcap["phantomjs.page.settings.loadImages"] = False
        # 设置代理 1
        service_args = ['--proxy = %s' %some_proxy_IP , '--proxy-type=socks5']

        chen_opener = webdriver.PhantomJS(desired_capabilities=dcap,
                                       executable_path = '../../../../plugin/phantomjs',
                                          service_args=service_args)

        # 添加代理 2
        the_proxy = webdriver.Proxy()
        the_proxy.proxy_type = ProxyType.MANUAL
        the_proxy.http_proxy = '代理'
        the_proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
        #


        # 接受一个网址，返回js渲染后的源码
        chen_opener.get(request.url)
        content = chen_opener.page_source.encode('utf-8')

        chen_opener.close()
        chen_opener.quit()

        print 'already cross selenium'

        # return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
        return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)