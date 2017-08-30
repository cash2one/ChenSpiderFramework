#! /usr/bin/env python
# -*- coding:utf-8 -*-


__author__ = 'Chen Yansu'

'''
一个邮件系统
只要传题目和正文，即可发送邮件
'''


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


class Send_mail(object):

    def __init__(self, the_subject, the_content):
        self.from_addr = 'chenyu_pub@sina.com'
        self.to_addr = 'chenyu_pub@sina.com'
        self.password = '123456123456'
        self.smtp_server = 'smtp.sina.com'

        self.msg = MIMEText('%s' % the_content, 'plain', 'utf-8')
        self.msg['Subject'] = Header(u'%s' % the_subject, 'utf-8').encode()

        self.msg['From'] = self._format_addr(u'陈严肃的自动发送邮件 <%s>' % self.from_addr)
        self.msg['To'] = self._format_addr(u'陈严肃 <%s>' % self.to_addr)

    # def the_msg(self, the_subject, the_content):
    #     self.msg = MIMEText('%s' % the_content, 'plain', 'utf-8')
    #     self.msg['Subject'] = Header(u'%s' % the_subject, 'utf-8').encode()

    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((\
            Header(name, 'utf-8').encode(),\
            addr.encode('utf-8') if isinstance(addr, unicode) else addr))

    def send_start(self):
        server = smtplib.SMTP(self.smtp_server, 25)  # SMTP协议默认端口是25
        server.set_debuglevel(1)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, [self.to_addr], self.msg.as_string())
        server.quit()


# if __name__ == "__main__":
#     ssss = Send_mail(the_subject='the_thrid_test', the_content='It is good')
#     ssss.send_start()


