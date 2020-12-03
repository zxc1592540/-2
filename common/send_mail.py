import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class email:

    def send_report(self):
       print('ok')
       sender='2020641828@qq.com'
       receiver='1870237243@qq.com'
       message=MIMEMultipart()
       MIMEText('测试报告', 'plain', 'utf-8')
       message['From']=Header('李子实', 'utf-8')
       message['To']=Header('开发人员', 'utf-8')
       message['Object']=Header('接口自动化测试报告', 'utf-8')
       message.attach(MIMEText('该邮件是自动化接口测试报告，请查阅附件', 'plain', 'utf-8'))
       att1= MIMEText(open("D:\\pycharm\\MyRequests\\report\\result.html",'rb').read(), 'base64', 'utf-8')
       att1["Content-Type"] = 'application/octet-stream'
       att1["Content-Disposition"] = 'attachment; filename="result.html"'
       message.attach(att1)
       print('ok')
       try:
          smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
          smtpObj.set_debuglevel(1)
          smtpObj.login('2020641828@qq.com', 'dqmphuehhazfbaai')
          smtpObj.sendmail(sender, receiver, message.as_string())
          print("邮件发送成功")
       except smtplib.SMTPException:
           print("Error: 无法发送邮件")











