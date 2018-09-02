# coding:utf-8
from basic.basic import Basic_login_out
import unittest
import time


class test_Login_out(unittest.TestCase):
    '''基本功能测试类'''

    @classmethod
    def setUpClass(cls):
        '''打开浏览器'''
        cls.path = r"C:\Users\zhumengtong\AppData\Roaming\Mozilla\Firefox\Profiles\cmdzoesn.default"
        cls.url = "http://www.csdn.net/"
        cls.basic = Basic_login_out()
        cls.driver = cls.basic.open(cls.path, cls.url)

    def test_01_login(self):
        '''登录功能测试'''
        try:
            self.basic.open_lonin(self.driver)
            username = "AngesZhu"
            password = "tong521.."
            r = self.basic.login(self.driver, username, password)
            self.assertTrue(r, msg="Error:Login Error")
        except Exception as le:
            print "Login error:%s" % le

    def test_02_out(self):
        '''登出功能测试'''
        self.basic.open_lonin(self.driver)
        username = "AngesZhu"
        password = "tong521.."
        r = self.basic.login(self.driver, username, password)
        time.sleep(5)
        r = self.basic.out(self.driver)
        self.assertTrue(r, msg="Error:out Error")

    @classmethod
    def tearDownClass(cls):
        print "10秒后退出浏览器"
        time.sleep(10)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

