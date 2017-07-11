# This Python file uses the following encoding: utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

#创建谷歌浏览器
# Create a new instance of the Chorme driver
driver = webdriver.Chrome()

#跳转至百度页面
# go to the baidu home page
driver.get("http://www.baidu.com")

# 找到页面元素name是wd的控件（就是百度搜索框）
# find the element that's name attribute is wd (the baidu search box)
inputElement = driver.find_element_by_name("wd")
#输入搜索内容
# type in the search
inputElement.send_keys("Cheese!")

#提交搜索控件元素内容
# submit the form (although google automatically searches now without submitting)
inputElement.submit()

#打印网页名字
# the page is ajaxy so the title is originally this:
print driver.title

try:
    # 我们在10秒内每隔500毫秒搜索一次看是否找到页名为Chess！的页面
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("Cheese!"))

    # 你会看到"Chess！ -b百度搜索"
    # You should see "Cheese! - 百度搜索"
    print driver.title

finally:
    driver.quit()