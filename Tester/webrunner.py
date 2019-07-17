# -*- coding: utf-8 -*-
# @Time     : 2019/7/16 15:55
# @Author   : ZhangLi
# @File     : webrunner.py

from Tester.web import Web #导入Web这个类

#打开浏览器
web = Web()

#上传文件
web.upload()

web.close()
