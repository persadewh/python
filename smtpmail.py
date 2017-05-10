#!/usr/local/bin/python3

import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

#
mail_host='****'
mail_user='****'
mail_password='****'

sender = "****"
receiver = "****"


#mail_content = "测试"
mail_content = "<a href=''>测试</a>"

#message = MIMEText(mail_content,'plain','utf-8')
#message = MIMEText(mail_content,'html','utf-8')
message = MIMEMultipart()


message['From'] = Header('ray','utf-8')#发件人显示
message['To'] = Header('测试','utf-8')#收件人显示

subject = 'Python SMTP Mail Test'

message['Subject'] = Header(subject,'utf-8')#主题

#attachments
att1 = MIMEText(open('test.txt','rb').read(),'base64','utf-8')
att1['Content-Type']='application/octet-stream'
att1['Content-Disposition']='attachment;filename="test.txt"'


message.attach(MIMEText(mail_content,'html','utf-8'))
message.attach(att1)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_password)
    smtpObj.sendmail(sender,receiver,message.as_string())
    print('send success')
except smtplib.SMTPException:
    print('send failure')