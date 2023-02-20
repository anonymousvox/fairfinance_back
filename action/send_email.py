from __future__ import annotations
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.user_config import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST, EMAIL_PORT
import smtplib


class SendMail:

    __slots__ = ("password", "login", "host", "port", "message_from", "recipients")

    def __call__(self, subject, message):
        self.__send_mail(subject, message)

    def __init__(self, recipients: (str | list)):
        """
        param: recipients: str or list -user/users from message
        """
        self.password = EMAIL_HOST_PASSWORD
        self.login = EMAIL_HOST_USER
        self.host = EMAIL_HOST
        self.port = str(EMAIL_PORT)
        self.message_from = self.login
        self.recipients = recipients

    def __get_dsn(self):
        return ": ".join([self.host, self.port])

    def __get_server(self):
        server = smtplib.SMTP(self.__get_dsn())
        server.starttls()
        server.login(self.login, self.password)
        return server

    def __get_msg(self, subject: str, message: str):
        msg = MIMEMultipart()
        msg['From'] = self.message_from
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        return msg

    def __send_mail(self, subject: str, message: str):
        """
        param: subject - subject for message
        param: message - body message
        """
        msg = self.__get_msg(subject, message)
        server = self.__get_server()
        if isinstance(self.recipients, list):
            [server.sendmail(self.message_from, message_to, msg.as_string()) for message_to in self.recipients]
        else:
            server.sendmail(self.message_from, self.recipients, msg.as_string())
