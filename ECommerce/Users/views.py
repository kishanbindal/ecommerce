import logging
import pdb
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import User
from .serializers import LoginOtpViewSerializer
from services.auth import logged_in
from services.sms_service import OtpService, SmsService
from services import redis_service, token_service

logging.basicConfig(level=logging.DEBUG)

rdb = redis_service.Redis()


class LoginOtp(GenericAPIView):

    serializer_class = LoginOtpViewSerializer

    def post(self, request, *args, **kwargs):

        smd = {
            'success': False,
            'message': 'Unsuccessful in Generating Otp. Please Try Again',
            'data': []
        }

        try:
            # pdb.set_trace()
            serializer = LoginOtpViewSerializer(data=request.data)
            if serializer.is_valid():
                user = User.objects.get(phone_number=serializer.data.get('phone_number'))
                if user is not None:
                    otp, validity_period = OtpService().generate_otp()
                    if len(str(otp)) != 6:
                        raise ValueError('Length of OTP is not 6 digits.')
                    elif type(otp) != int:
                        raise TypeError('OTP Generated is not of type integer')
                    else:
                        smd = {
                            'success': True,
                            'message': "Successfully generated OTP",
                            'data': {'otp': 567345}
                        }
                        rdb.set(user.phone_number, '567345', validity_period)
                        # SmsService().send_sms(user, otp, validity_period)
                        return Response(data=smd, status=status.HTTP_200_OK)
                else:
                    return Response(data=smd, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            smd['data'] = 'User Does Not Exist'
            return Response(data=smd, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            smd['data'] = ValueError
            return Response(data=smd, status=status.HTTP_400_BAD_REQUEST)
        except TypeError:
            smd['data'] = TypeError
            return Response(data=smd, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(GenericAPIView):

    serializer_class = LoginOtpViewSerializer

    def post(self, request, *args, **kwargs):

        try:
            smd = {
                'success': False,
                'message': 'Login Unsuccessful',
                'data': []
            }
            otp = request.data.get('otp')
            user = User.objects.get(phone_number=request.data.get('phone_number'))
            if user is not None:
                if type(otp) != int:
                    raise TypeError('OTP is not of valid type')
                elif len(str(otp)) != 6:
                    raise ValueError('Otp is of invalid length')
                else:
                    rdb.delete(str(user.phone_number))
                    if user.is_superuser is False:
                        token = token_service.TokenService().generate_login_token(user.pk)
                    else:
                        token = token_service.TokenService().generate_admin_token(user.pk)
                    rdb.set(user.pk, token)
                    smd['success'], smd['message'], smd['data'] = True, 'Login Successful', {'token': token}
                    return Response(data=smd, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except TypeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@method_decorator(logged_in, name='post')
class UserLogoutView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            token = request.headers.get('token')
            payload = token_service.TokenService().decode_token(token)
            user_id = payload.get('id')
            rdb.delete(user_id)
            smd = {
                'success': True,
                'message': 'Successfully logged user out',
                'data': []
            }
            return Response(data=smd, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'error': "error"}, status=status.HTTP_400_BAD_REQUEST)
