#coding=utf8

from HTMLTestRunner import HTMLTestRunner
import unittest,time
from setting.send_email import *


discover=unittest.defaultTestLoader.discover("./case",pattern="foot1.py")

if __name__=="__main__":
    runner = unittest.TextTestRunner()
    runner.run(discover)
    sed_mail("E:\JK-JT\workspace\Teaching and insurance network\teaching\number\foot.txt")  # 发送邮件









