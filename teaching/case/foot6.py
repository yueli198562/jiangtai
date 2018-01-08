#coding:utf-8
'''云南省校园食品安全
前期准备数据：职业院校  1500万  100人  12个月'''
from selenium import webdriver
from setting.r_excel import *
from selenium.webdriver.support.ui import Select
import time
import os

base_dir = os.path.dirname(os.path.dirname(__file__)) # 返回当前文件所在目录的上级目录
base_dir=base_dir.replace("/","\\")
foot = base_dir + "\\number\\foot"  #找到excel数据配置文件
firefoxfile=base_dir+'\\photographa\\firefox.exe' #找到exe文件路径
photo_file=base_dir+'\\photographa\\p1.jpg'  #找到图片路径

driver=webdriver.Chrome()
# driver=webdriver.Firefox()
# driver=webdriver.Ie()
driver.maximize_window()
driver.get(B1)
driver.find_element_by_name("j_username").clear()
driver.find_element_by_name("j_username").send_keys(B2)
driver.find_element_by_name("j_password").clear()
driver.find_element_by_name("j_password").send_keys(B3)
driver.find_element_by_xpath('//*[@href="#"  and  @tabindex="3"]/img').click()


#点击左侧菜单云南省教育保险-在线投保-云南省校园视频安全责任
driver.switch_to_frame("nav")  #先切换frame表单
driver.find_element_by_xpath("//*[@id='menu']/li[8]/a").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='menu']/li[8]/ul/li[1]/a").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu']/li[8]/ul/li[1]/ul/div/li[2]/a").click()
driver.switch_to_default_content() #释放表单
#勾选须知
time.sleep(2)
driver.switch_to_frame("framecontent") #切换表单
checkbox=driver.find_elements_by_xpath('//*[@name="checkbox"]')
for i in checkbox:
    i.click()
driver.find_element_by_xpath("//*[@id='step1_ok']").click()
#投保机构查询页面
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='selectOrg']").click() #点击查询按钮
time.sleep(1)
driver.find_element_by_xpath("//*[@id='result']/tr[1]/td[1]/input").click() #选择机构
driver.find_element_by_xpath("//*[@id='ok']").click() #点击确定
#填写投保人信息页面
time.sleep(1)
driver.find_element_by_xpath("//*[@id='policyHolderInfo_email']").clear() #清空联系人邮箱
driver.find_element_by_xpath("//*[@id='policyHolderInfo_email']").send_keys(B4) #清空联系人邮箱
driver.find_element_by_id("step1_ok" ).click() #点击下一步
#选择职业院校
time.sleep(1)
driver.find_element_by_xpath('//*[@id="bxrType" and @value="31"]').click()
#上传被保险人信息页面
time.sleep(1)
s=driver.find_element_by_xpath(".//*[@id='jichubaofei']")
Select(s).select_by_visible_text("1500万元")
time.sleep(1)
driver.find_element_by_id('stuNum').send_keys(100)
time.sleep(1)
s1=driver.find_element_by_xpath("//*[@id='term']")
Select(s1).select_by_visible_text("12")
time.sleep(1)
driver.find_element_by_xpath('//*[@onclick="gotoStep3();return false;"]').click()
#保费计算页面 点击下一步
time.sleep(1)
driver.find_element_by_id('step3_ok').click()
#确认投保单页面
time.sleep(2)
driver.find_element_by_id('readAll').click()
driver.find_element_by_id('step4_ok').click()
#获取保单号
time.sleep(1)
Insure_single_number=driver.find_element_by_partial_link_text("NO").text
f=open(foot,"a+")
f.write("\n（职业院校  1500万  100人  12个月）："+Insure_single_number[4:].encode('utf-8'))
f.close()
driver.quit()
#-------上传单证-------
driver=webdriver.Firefox()
driver.get(B1)
driver.find_element_by_name("j_username").clear()
driver.find_element_by_name("j_username").send_keys(B2)
driver.find_element_by_name("j_password").clear()
driver.find_element_by_name("j_password").send_keys(B3)
driver.find_element_by_xpath('//*[@href="#"  and  @tabindex="3"]/img').click()
driver.switch_to_frame("nav") #切换表单
time.sleep(1)
driver.find_element_by_xpath("//*[@id='menu']/li[8]/a").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='menu']/li[8]/ul/li[3]/a").click()
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='menu']/li[8]/ul/li[3]/ul/li/a").click()
#投保单号查询页面
driver.switch_to_default_content() #退出上个表单
driver.switch_to_frame("framecontent") #切换表单
time.sleep(1)
driver.find_element_by_id("applicationFormCode").send_keys(Insure_single_number[4:])
#Insure_single_number[4:]
s2=driver.find_element_by_id("applicationType")
Select(s2).select_by_visible_text("校园食品安全责任险")
time.sleep(1)
driver.find_element_by_id("Search").click()
time.sleep(1)
driver.find_element_by_id("uploadCertification").click()
#上传单证页面
time.sleep(1)
driver.find_element_by_id("uploadFile").click()
time.sleep(1)
os.system(firefoxfile + " " + photo_file) #上传附件
time.sleep(1)
driver.find_element_by_xpath('//*[@onclick="uploadCertificate()"]').click()
driver.switch_to_alert().accept()  #弹出框点击确认
time.sleep(1)
driver.switch_to_alert().accept()  #弹出框点击确认

#-------审核单证------
driver.switch_to_default_content() #退出上个表单
driver.switch_to_frame("nav") #切换表单
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='menu']/li[8]/ul/li[3]/ul/li/a").click()
#投保单号查询页面
driver.switch_to_default_content() #退出上个表单
driver.switch_to_frame("framecontent") #切换表单
time.sleep(1)
driver.find_element_by_id("applicationFormCode").send_keys(Insure_single_number[4:])
s2=driver.find_element_by_id("applicationType")
Select(s2).select_by_visible_text("校园食品安全责任险")
time.sleep(1)
driver.find_element_by_id("Search").click()
time.sleep(1)
driver.find_element_by_id("checkCertification").click()
#审核页面点击 通过
driver.find_element_by_xpath('//*[@class="b4"]').click()
driver.switch_to_alert().accept()
driver.quit()