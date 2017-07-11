# -*- coding: utf-8 -*-
# This Python file uses the following encoding: utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

driver = webdriver.Chrome()
driver.get("file:///C:/Users/nokia/Desktop/level_locate.html.html")

#点击Link1链接(弹出下拉列表框)
#Click the Link1 text link (pop-up drop-down list box)
driver.find_element_by_link_text('Link1').click()

#找到id为dropdown1的父元素
#Find the parent element of ID for dropdown1
WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_id('dropdown1').is_displayed())

# 在父亲元件下找到link为Action的子元素
# Find the child element of link for Action under the parent element
menu = driver.find_element_by_id('dropdown1').find_element_by_link_text('Action')

#鼠标定位到子元素上
#The mouse is positioned on the child element
webdriver.ActionChains(driver).move_to_element(menu).perform()
time.sleep(2)



