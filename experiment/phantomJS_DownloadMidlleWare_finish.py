
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from scrapy.http import HtmlResponse
from selenium import webdriver
import re
import base64
import os


#架构：
# 主函数　process_request
# (1) 路径模块：set_path:更改self.the_phantomjs使用新路径
# (2) phantomJS设置：新增字典self.dcap的key更改浏览器设置
# (3) 代理模块：接受代理中间件带来的信息加代理，传出self.service_args,如果屏蔽代理，需要在主函数（４）中注释掉self.service_args字段
# (4) 配置生效模块：通常用来停用代理
# (5) 信息模块：解除注释输出相关信息
# (6) js渲染,可以考虑得到chen_opener句柄获取浏览器拟人操作
# (7) 返回scrapy框架固定格式的参数

class phantomJS_headless(object):

    # (３)代理模块：
    def get_proxy(self,request):
        # 提取－转码
        proxy_auth_Basic_and_base64 = request.headers["Proxy-Authorization"]
        proxy_auth_base64 = re.findall("Basic (.+)", proxy_auth_Basic_and_base64)
        proxy_auth = base64.b64decode(proxy_auth_base64[0])

        # selenium代理参数设定
        self.service_args = [
            "--proxy-type=http",
            "--proxy=%s" % request.meta["proxy"],
            "--proxy-auth=%s" %proxy_auth
        ]
        return self.service_args

    # （１）路径模块：设定phantomjs路径
    def set_path(self):
        self.the_phantomjs = str(os.path.expandvars('$HOME')) + '/phantomjs/phantomjs'
        # if os.path.exists(the_phantomjs) is True:
        #     print "检测到phantomjs！"
        # else:
        #     print "phantomjs不存在!"
        #     os._exit()
        if os.path.exists(self.the_phantomjs) is False:
            print "phantomjs不存在!"
            os._exit()

    # (２) phantomJS设置
    def set_dcap(self,request):
        self.dcap = dict(DesiredCapabilities.PHANTOMJS)
        self.dcap["phantomjs.page.settings.loadImages"] = False
        self.dcap["phantomjs.page.settings.userAgent"] =request.headers['User-Agent']
        return self.dcap

    # 主函数
    def process_request(self, request, spider):

        # （１）路径模块：设定phantomjs路径
        self.set_path()

        # (２) phantomJS设置
        self.set_dcap(request)

        # (３)代理模块：
        self.get_proxy(request)

        # (4)配置生效模块：
        chen_opener = webdriver.PhantomJS(desired_capabilities=self.dcap,
                                       executable_path = self.the_phantomjs,
                                        service_args = self.service_args)
        # (5)信息模块
        # print("将使用headers:%s" % request.headers)
        # print("将使用ua:%s" % request.headers['User-Agent'])
        # print "将使用代理:%s"%self.service_args

        # (6)处理模块：接受一个网址，返回js渲染后的源码
        try:
            chen_opener.get(request.url)
            content = chen_opener.page_source.encode('utf-8')
        finally:
            chen_opener.close()
            chen_opener.quit()

        print '已经进行JS渲染！'

        # （７）返回参数
        return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
