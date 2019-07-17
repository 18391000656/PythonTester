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

    #上传文件
    def upload(self):
        self.driver.implicitly_wait(20)
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="form"]/span[1]/span').click()
        self.driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[2]/input').send_keys('D:\\PycharmProjects\\firstproject\\小猫.jpg')
        time.sleep(10)

    def close(self):
        time.sleep(3)
        self.driver.quit()