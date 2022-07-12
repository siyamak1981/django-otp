
from rest_framework import viewsets
from session.models import Session
from api.permissions import IsSuperSignupOrReadOnly
from api.v1.serializers.otp import ObtainTokenSerializer
from session.models import Session
from ..serializers.users import UserSerializer
from accounts.models import SendSmsRequest
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
User = get_user_model()



class SignUpApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    serializer_class = UserSerializer
    permission_classes = [IsSuperSignupOrReadOnly]

    def create(self, request, *args, **kwargs):
        mobile_number = request.data.get('mobile_number')
       
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            otp_number = {dict(dict(data)['sendsms'])['receiver']}
            otp_code = {dict(dict(data)['sendsms'])['code']}
     
            if "".join(otp_number) == mobile_number :
     
                """check the code client sent to server and check the code is valid or not"""
                if SendSmsRequest.objects.is_valid("".join(otp_number),"".join(otp_code)):
                    return Response(self._handle_login(data))
                else:
                    """if request_id or code or receiver was not True return 401"""
                    return Response({"Error": "request_id or code or receiver is invalid "},status = status.HTTP_401_UNAUTHORIZED)
            else:
                print("new number is not True ")
                return Response({"Messages":"mobile Number is invalid"}, status = status.HTTP_401_UNAUTHORIZED)
        else:
            """ if else the code of send sms is not valid"""
            return Response({"Messages":"Otp Code is invalid"},status = status.HTTP_400_BAD_REQUEST, data = serializer.errors)


    def _handle_login(self, otp):
        query = User.objects.filter(mobile_number = dict(dict(otp)['sendsms'])['receiver'])
        """if user with this number is exists """
        if query.exists():
            created = False
            user = query.first()

        else:
            """if user with this number isnot exists """
            user = User.objects.create(mobile_number = dict(dict(otp)['sendsms'])['receiver'],\
                                            first_name = dict(otp)["first_name"],last_name = dict(otp)['last_name'],\
                                            password = make_password(dict(otp)['password']), email = dict(otp)['email'],\
            )
    
            Session.objects.create(
                user_id = user.id,
                client_ip = self.request.META.get("REMOTE_ADDR"),
                uniqe_device_code= self.request.META.get("HTTP_USER_AGENT"),
                client_version = self.request.META.get("HTTP_HOST"),
                server_version = self.request.META.get("SERVER_NAME"),
                refresh_has_token = self.request.COOKIES['csrftoken']
        )
  
            created = True

        """return token and refresh token """
        refresh = RefreshToken.for_user(user)
        return ObtainTokenSerializer({
            "refresh":str(refresh), 
            "token":str(refresh.access_token),
            "created":created,
        }).data
       
