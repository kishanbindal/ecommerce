import jwt
import os
from dotenv import load_dotenv

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(base, '.env')
load_dotenv(dotenv_path=env_path)


class TokenService:

    secret = os.getenv('secret')

    def generate_login_token(self, user_id):
        payload = {
            'id': user_id,
            'role': 'user'
        }
        return self.__encode(payload)

    def __encode(self, payload):
        encoded_token = jwt.encode(payload, self.secret, algorithm=os.getenv('algorithm')).decode('utf-8')
        return encoded_token

    def generate_admin_token(self, user_id):
        payload = {
            'id': user_id,
            'role': 'admin'
        }
        return self.__encode(payload)

    def decode_token(self, token):
        payload = jwt.decode(token, self.secret, algorithms=os.getenv('algorithm'))
        return payload
