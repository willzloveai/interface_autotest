
import smtplib,os,string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import configparser as cparser
from logger import Log

#获取当前文件路径
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\','/')
file_path = base_dir + "/configuration/email_config.ini"


cf = cparser.ConfigParser()
cf.read(file_path)

smtpserver = cf.get("emailconf","smtpserver")
user = cf.get("emailconf","user")
password = cf.get("emailconf","password")
sender = cf.get("emailconf","sender")
receiver = cf.get("emailconf","receiver")
cc = cf.get("emailconf","cc")
subject = cf.get("emailconf","subject")
subtype = cf.get("emailconf","subtype")
#str转list
cc = list(cc.split(','))
receiver = list(receiver.split(','))

class SendEmail:
    def __init__(self):
        # 发送邮件服务器
        self.smtpserver = smtpserver
        # 发送邮箱用户/密码
        self.user = user
        self.password = password
        # 发送邮箱
        self.sender = sender
        # 接收邮箱
        self.receiver = receiver
        #抄送
        self.cc = cc
        #标题
        self.subject = subject
        #发送方式
        self.subtype = subtype
        #SMTP初始化
        self.smtp = smtplib.SMTP()
        #打印日志
        self.log = Log()

    #连接服务器connect
    def __Connect(self,smtpserver):
        try:
            self.smtp.connect(self.smtpserver)
            return True
        except Exception as e:
            self.log.error("[SendEmail:]you got wrong server connect %s"%e)

    #登陆login
    def __Login(self,username,password):
        try:
            self.smtp.login(username,password)
        except Exception as e:
            self.log.error("[SendEmail]username or password is wrong %s"%e)

    #退出quit
    def __Quit(self):
        self.smtp.quit()

    #整合发送邮件
    def __SendEmail(self,sender,receviver,message):
        self.smtp.sendmail(sender,receviver,message)

    #读取报告
    def __GetFile(self,fp):
        try:
            f = open(fp,'rb')
            filepath =f.read()
            return filepath
            f.close()
        except Exception as e:
            self.log.error('[SendEmail]you got wrong filepath %s'%e)


    #发送测试报告
    def sendemail(self,file_new):
        try:
            mail_body = self.__GetFile(file_new)
            if self.subtype == 'html'or self.subtype == 'plain':#发送html或者text格式的邮件
                msg = MIMEText(mail_body, self.subtype, 'utf-8')
                msg['Subject'] = Header(self.subject, 'utf-8')
                msg['From'] = Header(self.sender, 'utf-8')
                msg['To'] = ",".join(self.receiver)
                msg['cc'] = ",".join(self.cc)
            elif self.subtype == 'base64':
                #附件部分
                disposition = 'attachment;filename="' + file_new[3:] + '\"'
                att = MIMEText(mail_body, 'base64', 'utf-8')
                att['Content-Type'] = 'application/octet-stream'
                att['Content-Disposition'] = disposition
                #正文部分
                txt = MIMEText("您好！具体内容见附件",'plain','utf-8')

                msg = MIMEMultipart('related')
                msg['Subject'] = Header(self.subject, 'utf-8')
                msg['From'] = Header(self.sender, 'utf-8')
                msg['To'] = ",".join(self.receiver)
                msg['cc'] = ",".join(self.cc)
                msg.attach(att)
                msg.attach(txt)
            else:
                raise IOError('you got wrong subtype')
        except Exception as e:
            self.log.error('[SendEmail]%s'%e)
        else:
            # 连接发送邮件
            if self.__Connect(self.smtpserver) == True:
                self.__Login(self.user, self.password)
                #存在多个收件人时候进行需要拆分
                self.__SendEmail(self.sender,self.receiver,msg.as_string())
                self.__Quit()

#测试函数
if __name__ == '__main__':
    em = SendEmail()

    file = 'E:\\MyInterface\\pyrequest\\report\\2017-08-02 11_49_22_result.html'
    em.sendemail(file)
