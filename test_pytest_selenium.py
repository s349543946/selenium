# -*- coding:utf-8 -*-
# This Python file uses the following encoding: utf-8

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# 引入unittest 包
# import  unittest,time,re
import pytest
from  selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException



class TestBaidu:
    # setup 用于设置初始化的部分
    # setup is used to set the initialization section
    def setup(self):
        self.driver = webdriver.Chrome()
        # 超时重连
        # Timeout reconnection
        self.driver.implicitly_wait(30)
        # 设置浏览路径
        # Set browse path
        self.base_url = "http://www.baidu.com"
        # 脚本运行错误打印到这个列表中
        # Script run error print to this list
        self.verificationErrors = []
        # 是否继续接受下一下警告
        # Would  like to proceed with the next warning
        self.accept_next_alert = True

    # 测试脚本
    # Test script
    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("seleniumide")
        driver.find_element_by_id("kw").click()

    # 用来查找页面元素是否存在
    # Used to find if the page element exists
    def is_elemet_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    # 对弹窗异常处理
    # Exception handling of popups
    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException, e:
            return False
        return True

    # 关闭警告和对文本框的处理
    # Close warnings and handle text boxes
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    # 清理工作如退出浏览器等
    # Cleanup tasks such as exiting browsers, etc.
    def teardown(self):
        self.driver.quit()
        # 对前面verificationErrors方法获得的列表进行比较如果不为空则打印列表报错信息
        # Compare the list obtained by the previous verificationErrors method, and print the list if you are not empty
        assert self.verificationErrors == []


if __name__ == "__main__":
    pytest.main("test_pytest_selenium.py")


