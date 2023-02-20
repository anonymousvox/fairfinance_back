import requests
from config.user_config import SMS_LOGIN, SMS_PASSWORD

class SendSms:

    def __init__(self, phone: str, text_message: str):
        self.phone = phone
        self.text_message = text_message

    def __call__(self):
        self.__send()

    def __send(self):
        response = requests.request('POST', 'http://api.smstraffic.ru/multi.php',
                             data='login={login}&password={password}&phones={phone}&message={text_message}&rus=5'
                                    .format(
                                        login=SMS_LOGIN,
                                        password=SMS_PASSWORD,
                                        phone=self.phone,
                                        text_message=self.text_message.encode('utf-8')
                                    ),
                             headers={'content-type': 'application/x-www-form-urlencoded'})
        return response.json