# coding=utf-8
# !/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class SendEmail:


    def send_mail(self, user_list, sub, content):
        email_host = "smtp.163.com"
        sendAddr = "17689551930@163.com"
        password = "niuqun123"
        msg = email.mime.multipart.MIMEMultipart()
        msg['from'] = sendAddr
        msg['to'] = ";".join(user_list)
        msg['subject'] = sub
        content = content
        txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
        msg.attach(txt)

        # 添加附件地址
        part = MIMEApplication(open(r'/Users/edz/Desktop/python_requese/data/data_test_api.xlsx', 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename="线上抓取指标统计表(1).xlsx")  # 发送文件名称
        msg.attach(part)

        smtp = smtplib.SMTP()
        smtp.connect(email_host, '25')
        smtp.login(sendAddr, password)
        smtp.sendmail(sendAddr, user_list, str(msg))
        print("发送成功！")
    def send_main(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        # 90%
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)

        user_list = ['maopeng@zile.ai']
        sub = "接口自动化测试报告"
        content = "此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" % (
        count_num, pass_num, fail_num, pass_result, fail_result)
        self.send_mail(user_list, sub, content)


if __name__ == '__main__':
    sen = SendEmail()
    sen.send_main([1, 2, 3, 4], [2, 3, 4, 5, 6, 7])

