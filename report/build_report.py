# coding:utf-8
import os
import time
from common import HTMLTestRunner

class BuildReport:

    def new_report(self, report_path):
        self.rp = open(report_path, "wb")
        runner = HTMLTestRunner.HTMLTestRunner(self.rp, u"基础功能测试报告", u"测试平台登录、退出功能")
        return runner

    def report_file(self):
        path = os.path.dirname(os.path.realpath(__file__))
        now = time.strftime("%y-%m-%d %H_%M_%S")
        report_path = os.path.join(path, "TestResult"+now+".HTML")
        return report_path

    def close_file(self):
        self.rp.close()
