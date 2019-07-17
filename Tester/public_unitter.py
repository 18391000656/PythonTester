# -*- coding: utf-8 -*-
# @Time     : 2019/6/30 15:32
# @Author   : ZhangLi
# @File     : public_unitter.py

import unittest
import time
from selenium import webdriver

#相当于做了一个测试用例
class TestLigin(unittest.TestCase):

    #初始化操作
    def setUp(self):
        #驱动谷歌浏览器
        self.driver = webdriver.Chrome()
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        print("setup")

    #一条测试用例
    def test_login(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
        driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
        driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("18391000656")
        driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("645222zhangli.")
        driver.find_element_by_id("TANGRAM__PSP_10__submit").click()

    #销毁，关闭，释放资源
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
        print("teardown")

#程序的入口
if __name__ == '__main__':
    #调用所有test开头的方法
    unittest.main()
