#coding=utf-8
from selenium import webdriver
import time

#访问百度
# get Baidu
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

#通过id元素定位
#element positioning by id
driver.find_element_by_id("kw").send_keys(u"是不是selenium")
driver.find_element_by_id("su").click()
time.sleep(3)

#将页面滚动条拖到底部
# would drag the scroll bar at the bottom of the page
js="var q=document.body.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)


#将滚动条移动到页面的顶部
# would drag the scroll bar at the top of the page
js="var q=document.body.scrollTop=0"
driver.execute_script(js)
time.sleep(3)

driver.quit()