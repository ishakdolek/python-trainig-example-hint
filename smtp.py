import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj=MIMEMultipart()

mesaj["FROM"] ="x@x.com"
mesaj["To"]="t@y.com"
mesaj["Subject"]="Test For Test"

yazi="Test for Test"


mesaj_govdesi=MIMEText(yazi,"plain")
mesaj.attach(mesaj_govdesi)
try:
    mail=smtplib.SMTP("smtp.gamil.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("kullaıcı adı","password")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    mail.close()
except expression as identifier:
    sys.stderr.write("Bir sorun oluştu!")
    sys.stderr.flush()