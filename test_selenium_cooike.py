#coding=utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.youdao.com")

#向cookie的name 和value添加会话信息。
#Add session information to value's name and cookie.
driver.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbb'})

#遍历cookies中的name 和value信息打印，当然还有上面添加的信息
# to traverse the cookies name and value information print, of course, Contain the above added information
for cookie in driver.get_cookies():
    print "%s -> %s" % (cookie['name'], cookie['value'])


# 下面可以通过两种方式删除cookie
# You can delete cookie in two ways
# 删除一个特定的cookie它的cookiename是key-aaaaaaa
#Deletes a particular cookie whose cookiename is key-aaaaaaa
driver.delete_cookie("key-aaaaaaa")
# 删除所有cookie
# Delete all cookie
driver.delete_all_cookies()

time.sleep(2)
driver.close()