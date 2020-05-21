from functools import wraps
from services import sms_service, redis_service, token_service
from services.exception import CacheDoesNotExist
import pdb

rdb = redis_service.Redis()


def logged_in(func=None):

    @wraps(func)
    def func_decorator(request, *args, **kwargs):
        try:
            token = request.headers.get('token')
            if token is None:
                raise ValueError('Token Cannot be empty')
            elif type(token) != str:
                raise TypeError('Token is of Invalid Type')
            else:
                payload = token_service.TokenService().decode_token(token)
                user_id = payload.get('id')
                if rdb.exists(user_id) and rdb.get(user_id).decode() == token:
                    if func is not None:
                        return func(request, args, kwargs)
                    else:
                        print('FUNC IS NONE')
                else:
                    raise CacheDoesNotExist(f'{user_id} does not exist in Cache Memory')
        except ValueError:
            return ValueError
        except TypeError:
            return TypeError
        except CacheDoesNotExist:
            return CacheDoesNotExist

    return func_decorator

