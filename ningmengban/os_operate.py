# -*- coding: utf-8 -*-
# @Time     : 2019/6/27 17:05
# @Author   : ZhangLi
# @File     : os_operate.py

import os

# print(os.sep)            #主要用于系统路径的分隔符
# print(os.name)           #指示你正在使用的平台
# print(os.getenv("Path")) #读取环境变量的值
# print(os.getcwd())       #获取当前的路径

# dirs = "D:\\Program Files (x86)"
# if os.path.exists(dirs):  #判断文件或目录是否存在
#     #列出该路径下的所有文件
#     files = os.listdir(dirs)  #返回指定目录下的文件和目录名
#     print(files)
#
#     fullpath = os.path.join(dirs,files[0]) #拼接路径与文件名
#     print(fullpath)
#     if os.path.isfile(fullpath):  #判断是否为文件
#         print("我是一个文件")
#     elif os.path.isdir(fullpath): #判断是否为目录
#         print("我是一个目录")
#

#示例二
# my_dir = "D:\\Program Files (x86)\\Test\\offer\\111"
# #判断目录是否存在-不存在就创建
# if not os.path.exists(my_dir):
#     #os.mkdir(my_dir)  #只能创建一层目录不存在
#     os.makedirs(my_dir)#创建多层目录不存在
#
# #判断目录是否存在-存在就删除
# if os.path.exists("D:\\Program Files (x86)\\Test\\offer"):
#     os.rmdir("D:\\Program Files (x86)\\Test\\offer")  #只能删除空目录
#
'''
编写一个程序
1.能在当前目录下查找文件名包含指定字符串的文件
2.并打印出绝对路径
'''
sub_str = "app"
cur_dir = os.getcwd()
files = os.listdir(cur_dir)
for item in files:
    print(item)
    if os.path.isfile(os.path.join(cur_dir,item)):
        #看看文件名是否包含指定的字符串
        if item.find(sub_str) !=-1:
            # 然后输出
            print(os.path.join(cur_dir,item))
