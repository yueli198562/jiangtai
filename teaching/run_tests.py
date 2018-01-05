#coding=utf8

from HTMLTestRunner import HTMLTestRunner
import unittest,time

test_dir="./case" #指定测试用例为当前文件夹下的case目录
discover=unittest.defaultTestLoader.discover(test_dir,pattern="foot*.py")

if __name__=="__main__":
    now=time.strftime("%y-%m-%d %H_%M_%S") #获取当前格式化日期
    filename="./test_report/"+now+"_result.html" #测试报告路径
    f=open(filename,"wb")
    runner=HTMLTestRunner(stream=f,title="235245",description="23452345")    
    runner.run(discover)
    f.close()











