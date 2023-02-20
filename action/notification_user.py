from action.send_sms import SendSms
from action.send_email import SendMail

class NotificationUser:

    def __call__(self):
        self.__notification()

    def __init__(self, phone, email, subject_message_for_email, text_message):
        self.phone = phone
        self.email = email
        self.subject_message_for_email = subject_message_for_email
        self.text_message = text_message

    def __notification(self):
        notification_sms = SendSms(self.phone, self.text_message)
        notification_sms()
        notification_email = SendMail(self.email)
        notification_email(self.subject_message_for_email, self.text_message)

    def notification_email(self):
        notification_email = SendMail(self.email)
        notification_email(self.subject_message_for_email, self.text_message)