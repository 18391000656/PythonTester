# -*- coding: utf-8 -*-
# @Time     : 2019/6/26 17:08
# @Author   : ZhangLi
# @File     : mail.py

import yagmail
#连接服务器
mail = yagmail.SMTP("2949897907@qq.com","tednhctcxzkrdfaa","smtp.qq.com",465)
#准备正文内容
content ='''
好久不见，你还好吗。。
我喜欢你很久了，你喜欢我吗？？
如果你也喜欢我，那么我们十一去旅游吧。
'''
#发送邮件
mail.send(["ZLbluesea0656@163.com","zhangli2@yitong.com.cn"],
          "点开你喜欢我，不点开我喜欢你",
          content,
          "D:\\PycharmProjects\\firstproject\\小猫.jpg")