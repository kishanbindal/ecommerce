import logging
import pdb
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserInfo
from .serializers import LoginOtpViewSerializer
from services.sms_service import OtpService, SmsService
from services import redis_service

logging.basicConfig(level=logging.DEBUG)

rdb = redis_service.Redis()


class LoginOtp(GenericAPIView):

    def post(self, request, *args, **kwargs):
        try:
            serializer = LoginOtpViewSerializer(data=request.data)
            if serializer.is_valid():
                user = UserInfo.objects.get(phone_number=serializer.data.get('phone_number'))
                if user is not None:
                    otp, validity_period = OtpService().generate_otp()
                    if len(str(otp)) != 6:
                        raise ValueError('Length of OTP is not 6 digits.')
                    elif type(otp) != int:
                        raise TypeError('OTP Generated is not of type integer')
                    else:
                        # SmsService().send_sms(user, otp, validity_period)
                        return Response(status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
        except UserInfo.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response(data=ValueError, status=status.HTTP_400_BAD_REQUEST)
        except TypeError:
            return Response(data=TypeError, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(GenericAPIView):

    def post(self, request, *args, **kwargs):

        try:
            otp = request.data.get('otp')
            user = UserInfo.objects.get(phone_number=request.data.get('phone_number'))
            pdb.set_trace()
            if user is not None:
                if type(otp) != int:
                    raise TypeError('OTP is not of valid type')
                elif len(str(otp)) != 6:
                    raise ValueError('Otp is of invalid length')
                else:
                    return Response(status=status.HTTP_200_OK)
        except UserInfo.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except TypeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # TODO -->

        #     if user is not None:
        #         rdb.set(user.pk, 'online')
        #         return Response(status=status.HTTP_200_OK)
        # except UserInfo.DoesNotExist:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
        # except ValueError:
        #     return Response(data=ValueError, status=status.HTTP_400_BAD_REQUEST)
        # except TypeError:
        #     return Response(data=TypeError, status=status.HTTP_400_BAD_REQUEST)
