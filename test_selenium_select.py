# This Python file uses the following encoding: utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("file:///C:/Users/nokia/Desktop/select.html")

sel = driver.find_element_by_xpath("//select[@id='status']")
Select(sel).select_by_value('0')  #未审核 Not audited
Select(sel).select_by_value('1')  #初审通过 First instance
Select(sel).select_by_value('2')  #复审通过 Review through
Select(sel).select_by_value('3')  #审核不通过 Audit not through