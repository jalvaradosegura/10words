import os
import smtplib
from email.message import EmailMessage


def send_email(message):
    gmail_user = os.environ.get('EMAIL_USER')
    gmail_password = os.environ.get('EMAIL_PASSWORD')

    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = '10 palabras aleatorias'
    msg['From'] = os.environ.get('EMAIL_USER')
    msg['To'] = [*os.environ.get('RECEIVERS').split(',')]

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.close()
    except Exception as e:
        print(e)
