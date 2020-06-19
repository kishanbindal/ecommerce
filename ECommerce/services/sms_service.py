from django_otp.oath import totp
from dotenv import load_dotenv
import time
from twilio.rest import Client
import os
from .redis_service import Redis
# from services.redis_service import Redis
# from .redis_service import Redis

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(base, '.env')

load_dotenv(dotenv_path=env_path)

rdb = Redis()


class SmsService:

    def __init__(self):
        self.account_sid = os.getenv('account_sid')
        self.auth_token = os.getenv('auth_token')
        self.client = Client(self.account_sid, self.auth_token)

    def send_sms(self, user, otp, expiry_time):

        message = self.client.messages.create(
            to=user['phone_number'],
            from_=str(os.getenv('number')),
            body=f"Hello {user['first_name']}. Login Otp : {otp}"
        )
        if message.sid is not None:
            print(message.sid)
            rdb.set(user['phone_number'], otp, exp_s=expiry_time)
            rdb.get(user['phone_number'])
        else:
            raise ValueError('Text Message was not created')

    def send_order_placed_sms(self, user, cart):
        import pdb
        pdb.set_trace()
        body = f"Hello {user.first_name}.\nYour Order with order number : {cart.id} has been placed successfully" \
               f"and will be Delivered to \n {cart.address}"
        message = self.client.messages.create(
            to=user.phone_number,
            from_=str(os.getenv('number')),
            body=body
        )
        if message.sid is not None:
            print(message.sid)
        else:
            raise ValueError('Text Message was not created')


class OtpService:

    def __init__(self):
        self.key = os.getenv('otp_secret_key')
        self.step = 900
        self.digits = 6

    def generate_otp(self):
        otp = totp(key=self.key.encode(), step=self.step, digits=self.digits)
        return [otp, self.step]


# OtpService().generate_otp()
# user_obj = {'first_name': 'Kishan', 'phone_number': '+919738478938'}
# print(user_obj)
# SmsService().send_sms(user_obj, 681024,30)
