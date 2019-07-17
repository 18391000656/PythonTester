# -*- coding: utf-8 -*-
# @Time     : 2019/6/23 13:54
# @Author   : ZhangLi
# @File     : appclass.py

from appium import webdriver
import time

desired_caps = {}
#安卓设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.ibox.calculators'
desired_caps['appActivity'] = 'com.ibox.calculators.CalculatorActivity'

desired_caps['noReset'] = 'true'  #若用自己微信时请加上，不然会清空微信的所有信息（会还原app最初的状态）
#app里面可以输入中文
desired_caps['unicodeKeyboard'] = 'true'
desired_caps['resetKeyboard'] = 'true'


#与Appium服务器连接上，告诉appium要操作那个设备上那个应用程序
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
time.sleep(5)

#计算8+5
driver.find_element_by_id("com.ibox.calculators:id/digit8").click()
driver.find_element_by_id("com.ibox.calculators:id/plus").click()
driver.find_element_by_id("com.ibox.calculators:id/digit5").click()
driver.find_element_by_id("com.ibox.calculators:id/equal").click()

time.sleep(5)
driver.quit()
#验证，比对是否为是13
