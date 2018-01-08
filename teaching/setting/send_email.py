#coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# 定义发送邮件函数，传入一个html文件地址
def sed_mail(new_html):
    # 发件服务器地址
    email_host = 'smtp.qq.com'
    # 发件人用户名和密码
    email_user = '857519423@qq.com'
    email_pwd = 'WOAINI627'
    # 收件人邮箱，如果多个邮箱中间用逗号隔开
    milelist = 'yueli@jiangtai.com'  # 收件人邮箱，如果多个邮箱中间用逗号隔开

    # 构造附件1
    att1 = MIMEText(open(new_html, 'rb').read(), 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="foot.txt"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字

    # 邮件内容
    msg = MIMEMultipart()
    msg['Subject'] = '测试投保单号'  # 邮件主题
    msg['From'] = email_user  # 发件人邮箱
    msg['To'] = milelist  # 收件人邮箱
    # 添加附件
    msg.attach(att1)
    # 添加正文
    msg.attach(MIMEText('附件为最新的投保单号',"utf-8"))

    # 连接邮件服务器，传入发件服务器地址和端口号
    smtp = smtplib.SMTP(email_host, port=25)
    # 登陆发件人邮箱
    smtp.login(email_user, email_pwd)
    # 参数分别是发件人，收件人，第三个是把发送邮件的内容变成字符串
    smtp.sendmail(email_user, milelist, msg.as_string())
    # 发送完毕后退出smtp
    smtp.quit()

