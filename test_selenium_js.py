# -*- coding: utf-8 -*-
# This Python file uses the following encoding: utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()

#qq邮箱
# QQ mail
driver.get("https://mail.qq.com/cgi-bin/loginpage")

#多层框架定位
# frame positioning
driver.switch_to_frame("login_frame")

#g给用户输入框标红 （qq邮箱登录框不支持修改颜色以前快播貌似可以）
#g enters the frame red for the user QQ mailbox login box does not support modifying colors
js ="var q = document.getElementById(\"u\"); q.style.borde = \"1pw solid red\";"

#调用js
# use js
driver.execute_script(js)
time.sleep(2)

#qq邮箱登入的账号id
#qq mailbox login account ID
driver.find_element_by_id("u").send_keys("349543946")

driver.find_element_by_id("login_button").click()
time.sleep(3)

driver.quit()