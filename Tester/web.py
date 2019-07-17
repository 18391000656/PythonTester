# -*- coding: utf-8 -*-
# @Time     : 2019/7/16 15:45
# @Author   : ZhangLi
# @File     : web.py

from selenium import webdriver
import time
class Web:
    def __init__(self):
        #打开浏览器
        self.driver = webdriver.Chrome()

    def close(self):
        time.sleep(3)
        self.driver.quit()