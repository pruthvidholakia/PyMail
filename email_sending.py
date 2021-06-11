import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders


msg = MIMEMultipart()
msg['From'] = 'A'                         #A = enter your email address
msg['To'] = 'B'                           #B = receivers email address
msg['Subject'] = 'Check It Out'
msg.attach(MIMEText('Check This Image'))
file = open('C', 'rb')                    #C = img location
msg.attach(MIMEImage(file.read()))


filename = "quebank.pdf"
attachment = open("quebank.pdf", "rb")
p = MIMEBase('application', 'octel-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment;filename=%s"%filename)
msg.attach(p)



server = smtplib.SMTP('smtp.gmail.com',587)     #'smtp.mail.yahoo.com',587   'smtp.mail.outlook.com',587
server.starttls()
server.login('A', 'pass')                      #A = enter your email address, pass = your email password 
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
