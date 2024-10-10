from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from users.models import User


class UsernameAuthentication(BaseAuthentication):

    def authenticate(self, request):        
        username = request.headers.get('X-USERNAME')        

        if not username:
            return None
            # raise exceptions.AuthenticationFailed('X-USERNAME 헤더가 없습니다.')
        
        try:
            user = User.objects.get(username=username)
            return (user, None)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed(f"{username}이라는 회원은 없습니다.")

