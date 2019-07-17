# -*- coding: utf-8 -*-
# @Time     : 2019/6/28 16:20
# @Author   : ZhangLi
# @File     : cookie.py

from selenium import webdriver
import time
#访问一个谷歌浏览器
driver = webdriver.Chrome()
#访问一个网址
driver.get("http://www.baidu.com")

#用字典来存储cookie
cookie_1 = {"name":"BAIDUID","value":"B0B032156E4E6F152A43466A8208644A:FG=1"}
cookie_2 = {"name":"BDUSS","value":"W5-VFZyekxUelkxR0tMOWpib2Q0c090bk5VT1NTRGdYUVVHSGhubGZaTlYtenhkRVFBQUFBJCQAAAAAAAAAAAEAAABE4NRUsK7QprXEQmx1ZXNlYQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFVuFV1VbhVdZ"}

#利用cookie来登录
time.sleep(5)
driver.add_cookie(cookie_1)
driver.add_cookie(cookie_2)
#再去访问一次网址
driver.get("http://www.baidu.com")

time.sleep(5)
driver.quit()