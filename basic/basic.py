# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class Basic_login_out():

    def open(self, path, url):
        '''打开浏览器'''
        print "打开浏览器"
        profile = webdriver.FirefoxProfile(path)
        driver = webdriver.Firefox(profile)
        # driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(30)
        return driver

    def open_lonin(self, driver):
        '''打开登录页面'''
        print "打开登录页面"
        driver.find_element_by_link_text("登录").click()

    def login(self, driver, username, password):
        '''登录'''
        print "开始登录"
        driver.find_element_by_id("username").clear()
        print "输入帐号"
        driver.find_element_by_id("username").send_keys(username)
        print "输入密码"
        driver.find_element_by_id("password").send_keys(password)
        print "点击登录"
        driver.find_element_by_class_name("logging").click()
        d1 = driver.find_element_by_link_text("AngesZhu")
        return d1

    def out(self, driver):
        '''登出'''
        print "等待2秒，开始登出"
        time.sleep(1)
        print "等待1秒，开始登出"
        time.sleep(1)
        print "开始登出"
        move_place = driver.find_element_by_class_name("curr-icon-img")
        ActionChains(driver).move_to_element(move_place).perform()
        driver.find_element_by_class_name("icon-signout").click()
        print "确定退出登录"
        a = driver.switch_to.alert
        a.accept()
        time.sleep(2)
        d2 = driver.find_element_by_class_name("logging")
        return d2
