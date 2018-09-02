# coding:utf-8
import os
import sys
import unittest

from report.build_report import BuildReport
from smtp_text.report_mail import Email_send

reload(sys)
sys.setdefaultencoding('utf8')


class BasicsFunction():

    def testcase_import(self):
        # 获取当前脚本文件夹
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print "当前脚本所在的文件夹为：%s"%dir_path
        # 加载所有的用例
        dis = unittest.defaultTestLoader.discover(start_dir=dir_path, pattern="test*.py")
        return dis

    def run_case(self, dis):
        # 执行
        BR = BuildReport()
        report_path = BR.report_file()
        runner = BR.new_report(report_path)
        runner.run(dis)
        BR.close_file()
        return report_path

    def send_email(self, report_path):
        e = Email_send()
        user = "1372526521@qq.com"
        to = "ju_limeng@126.com"
        email_title = "测试报告"
        body = e.get_email_body(report_path)
        pwd = e.read_ini()
        p1 = pwd[1]
        e.email_send(email_title, user, to, p1, body)
        return "发送邮件成功"


if __name__ == "__main__":
        b = BasicsFunction()
        dis = b.testcase_import()
        path = b.run_case(dis)
        b.send_email(path)
