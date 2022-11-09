import smtplib
from datetime import datetime
from email.mime.text import MIMEText

recipients = ['mandeeptaneja2000@gmail.com']

def SendMail(message=None):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    message = MIMEText(message).as_string()
    server.login('zalutskiyperfecto@gmail.com','gtoaroaibldrtuih')
    for recipient in recipients :
        server.sendmail('zalutskiyperfecto@gmail.com',recipient,message)
    server.quit()