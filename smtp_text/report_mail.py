# coding:utf-8
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email_send():

    def read_ini(self):
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "smtp_text\\qq.ini")
        a = open(file_path, "r")
        s = a.readline()
        a.close()
        s1 = s.split("|")
        # for i in s1:
            # if i != "":
                # sl = i
        return s1

    def email_send(self, email_title, user, to,pwd,body):
        msg = MIMEMultipart()
        msg["Subject"] = email_title
        msg["From"] = user
        msg["To"] = to
        msg.attach(body)
        s = smtplib.SMTP_SSL("smtp.qq.com")
        s.login(user, pwd)
        s.sendmail(user, to, msg.as_string())
        s.quit()
        return "发送成功"

    def get_email_body(self,report_path):
        b = open(report_path,"r")
        mail_body = b.read()
        b.close()
        body = MIMEText(mail_body, "html", "utf-8")
        return body

if __name__ == "__main__":

    e = Email_send()
    user = "1372526521@qq.com"
    to = "ju_limeng@126.com"
    email_title = "测试一下发送邮件功能"
    email_text = "hello"
    pwd = e.read_ini()
    print pwd
    p1 = pwd[1]
    txt = e.email_send(email_title, user, to, email_text, p1)
