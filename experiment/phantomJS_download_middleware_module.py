from scrapy import downloadermiddlewares
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

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
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)")
        chen_opener = webdriver.PhantomJS(desired_capabilities=dcap,
                                       executable_path = '../../../../plugin/phantomjs')

        # 接受一个网址，返回js渲染后的源码
        chen_opener.get(request.url)
        content = chen_opener.page_source.encode('utf-8')

        chen_opener.close()
        chen_opener.quit()

        print 'already cross selenium'

        # return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
        return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
