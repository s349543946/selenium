#-*-coding=utf-8

from selenium import webdriver

import os,time

driver= webdriver.Chrome()
#进入百度搜索设置页面
#Enter Baidu search settings page
driver.get("https://www.baidu.com/gaoji/preferences.html")




#设置每页搜索结果为50条
# set page search results for 50
m=driver.find_element_by_name("NR")
m.find_element_by_xpath("//option[@value='50']").click()
time.sleep(2)


#保存设置的信息
# save settings information
driver.find_element_by_xpath("//input[@value='保存设置']").click()
time.sleep(2)
#处理弹窗信息
#Processing popups information
driver.switch_to_alert().accept()


#进入百度页面
# into Baidu page
driver.get("https://www.baidu.com/")

#跳转到百度首页后，进行搜索表（一页应该显示50条结果）
# jump to the Baidu home page, search table (a page should show 50 results)
driver.find_element_by_id("kw").send_keys("selenium")

driver.find_element_by_id("su").click()
time.sleep(3)

#driver.quit()