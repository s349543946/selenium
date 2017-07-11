# This Python file uses the following encoding: utf-8
#运行前需要有个页面登录百度账号成功
#Before running, you need to have a page login, Baidu account success
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 添加Cookie, Cookie信息由抓包工具Fiddler获得
# Add Cookie, Cookie information obtained by the Fiddler capture tool
driver.add_cookie({'name':'BAIDUID', 'value': '15EA1B77B2256A786C92C2F29850BA3B:FG=1'})
driver.add_cookie({'name':'BDUSS', 'value': 'N6c2pmeGR1MU9XY29nWnQ2UG1SdHlxbFRtQVRwU21BQ2ZYZER4Mlo4dWhpWVpaSUFBQUFBJCQAAAAAAAAAAAEAAACBNmEYczM0OTU0Mzk0NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKH8Xlmh~F5Zan'})
# 刷新页面
# Refresh page
driver.refresh()

# 获取登录用户名并打印
# Get login user name and print
usename = driver.find_element_by_class_name("user-name").text
print  usename

# 关闭浏览器
# Close browser
driver.quit()

