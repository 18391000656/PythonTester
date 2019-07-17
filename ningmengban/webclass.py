# -*- coding: utf-8 -*-
# @Time     : 2019/6/23 12:49
# @Author   : ZhangLi
# @File     : webclass.py

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

ele = driver.find_element_by_id("kw")

ele.send_keys("selenium")

driver.find_element_by_id("su").click()

time.sleep(3)
driver.quit()
