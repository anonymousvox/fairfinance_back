from action.barer_auth import BearerAuth
from config.user_config import get_url_hash_password, token_hash_password
import requests

class GetPasswordPlatform:
    
    __slots__ = (['password'])

    def __init__(self, password):
        self.password = password
    
    def get(self):
        user_dict = {
            "password": self.password
        }
        response = requests.post(f'{get_url_hash_password()}', auth=BearerAuth(token_hash_password), json=user_dict)
        result_data = response.json()
        return result_data.get('password')
    