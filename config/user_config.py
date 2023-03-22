DB_DSN = 'ppu:ppu@localhost:5432/ff'

SMS_LOGIN = 'c1000102985'
SMS_PASSWORD = 'VLd4XF3b'

EMAIL_HOST_USER = 'team@fairfin.ru'
EMAIL_HOST_PASSWORD = 'ff168ff168'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = '587'

URL_PALTFORM = ''
URL_HASH_PASSWORD = ''
SECRET_HASH_PASSWORD = ''

PATH_SAVE_FILE='./'

def get_url_hash_password():
    return "/".join([URL_PALTFORM, URL_HASH_PASSWORD])
