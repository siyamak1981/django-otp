

from rest_framework.views import APIView


from ..serializers.users import LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, login, authenticate
User = get_user_model()




class LoginApiView(APIView):
    authentication_classes = []
    serializer_class = LoginSerializer
    def post(self, request):

        mobile_number = request.data.get('mobile_number')
        password = request.data.get('password')
        user = authenticate(mobile_number=mobile_number, password=password)
        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, "refresh":str( RefreshToken.for_user(user))},
                        status=status.HTTP_200_OK)
          
        else:
            return Response({'Error': 'Invalid Credentials'},
                        status=status.HTTP_404_NOT_FOUND)
    






