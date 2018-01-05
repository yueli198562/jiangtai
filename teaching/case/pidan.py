#coding:utf-8
#批单管理 批单录入申请
driver=webdriver.Firefox()
driver.get(B1)
driver.find_element_by_name("j_username").clear()
driver.find_element_by_name("j_username").send_keys(B2)
driver.find_element_by_name("j_password").clear()
driver.find_element_by_name("j_password").send_keys(B3)
driver.find_element_by_xpath('//*[@href="#"  and  @tabindex="3"]/img').click()
driver.switch_to_frame("nav") #切换表单
driver.find_element_by_xpath("//*[@id='menu']/li[8]/a").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='menu']/li[8]/ul/li[4]/a").click() #点击投保管理
driver.find_element_by_xpath("//*[@id='menu']/li[8]/ul/li[4]/ul/div[1]/li/a").click() #点击投保单录入申请
#投保单查询页面
driver.switch_to_default_content() #退出上个表单
driver.switch_to_frame("framecontent") #切换表单
driver.find_element_by_id("applicationFormCode").send_keys("YNSP5900002017101850766")
s3=driver.find_element_by_id("applicationType")
Select(s3).select_by_visible_text("校园食品安全责任险")
driver.find_element_by_id("Search").click() #点击查询
time.sleep(1)
driver.find_element_by_id("sendNoteBtn").click()
#投保单录入界面
driver.find_element_by_id("studentAmount").send_keys(3)
driver.find_element_by_id("endorReason").send_keys("sdfsdfsdfsdf")
driver.find_element_by_id("submit_log").click()
