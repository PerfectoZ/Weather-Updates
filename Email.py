from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()

smtp.login('immortalgrenadiers@gmail.com','vevmifylquwgjonk')

recipients = ['mandeeptaneja2000@gmail.com']

def pack(subject="",text="",img=None,attachment=None):
    msg = MIMEMultipart()
    msg['Subject']=subject
    msg.attach(MIMEText(text))
    if img is not None :
        if type(img) is not list :
            img = [img]
        for i,one_img in enumerate(img) :
            img_data = open(one_img, 'rb').read()
            msg.attach(MIMEImage(img_data,name="Img_"+str(i)))
    if attachment is not None :
        if type(attachment) is not list :
            attachment = [attachment]
        for i,one_attachment in enumerate(attachment) :
            with open(one_attachment,'rb') as f :
                file = MIMEApplication(f.read(),name="Attachment_"+str(i))
            file['Content-Disposition'] = f'attachment'
            filename="File "+str(i)
            msg.attach(file)
    return msg

def SendMail(message=None):
    msg = pack("Weather Updates",message)
    smtp.sendmail(from_addr="immortalgrenadiers@gmail.com",to_addrs=recipients,msg=msg.as_string())
    smtp.quit()
