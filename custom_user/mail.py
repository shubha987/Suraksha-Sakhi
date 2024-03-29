import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(name, dest, link):
    server = smtplib.SMTP('smtp.gmail.com', 587)   #Gmail SMTP port (TLS)
    server.starttls()
    server.login('surakshasakhi372@gmail.com', 'trxk cvqo xbzz rbyh')
    email_html = open('templates/email.html')
    email_body = email_html.read().format(name=name, link=link)
    msg = MIMEMultipart()
    msg['Subject'] = 'EMERGENCY'
    msg.attach(MIMEText(email_body, 'html'))
    msg['From'] = formataddr(("RESCUE", "surakhshasakhi372@gmail.com"))
    server.sendmail('surakshasakhi372@gmail.com', dest, msg.as_string())
    server.quit()
   