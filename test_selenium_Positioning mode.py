#coding=utf-8

from selenium import webdriver
import time
import requests
browser = webdriver.Chrome()

browser.get("http://www.baidu.com")
time.sleep(2)

#########百度输入框的定位方式##########
########## Baidu input box positioning #########

#通过tag name方式定位 (由于input有多个第一个不是文本输入框不能输入)
# through tag name positioning (since the input has more than one, the first is not a text input box and cannot be entered)
browser.find_elements_by_tag_name("input")

#通过id方式定位
# through ID positioning
browser.find_element_by_id("kw").send_keys("selenium")

#通过name方式定位
# through name positioning
browser.find_element_by_name("wd").send_keys("selenium")

#通过class name 方式定位
# Positioning by class name
browser.find_element_by_class_name("s_ipt").send_keys("selenium")

#通过CSS方式定位
# Positioning by Css
browser.find_element_by_css_selector("#kw").send_keys("selenium")

#通过xpath方式定位
# Positioning by xpath
browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")

############################################

browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()