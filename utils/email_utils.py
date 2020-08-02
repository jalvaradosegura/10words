import smtplib
from email.message import EmailMessage


class SimpleEmail:

    def __init__(self, sender, receivers, subject, body):
        self.sender = sender
        self.receivers = receivers
        self.subject = subject
        self.body = body

    @property
    def email(self):
        msg = EmailMessage()
        msg.set_content(self.body)
        msg['Subject'] = self.subject
        msg['From'] = self.sender
        msg['To'] = [*self.receivers.split(',')]
        return msg


class EmailSender:

    email_class = SimpleEmail

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def create_email(self, receivers, subject, body):
        self.email = self.email_class(
            sender=self.user,
            receivers=receivers,
            subject=subject,
            body=body
        ).email

    def send_email(self):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(self.user, self.password)
            server.send_message(self.email)

        except Exception as e:
            print(e)
        finally:
            server.close()
