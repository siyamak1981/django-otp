import re
from rest_framework.views import APIView
from accounts.models import SendSmsRequest
from ..serializers.otp import   RequestOTPSerializer, RequestOTPResponseSerializer, VarifyOtpRequestSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()


class SendSmsView(APIView):
    queryset = User.objects.all()
    serializer_class = RequestOTPSerializer
    """ i ask client send me mobile number with get method or a query string """
    def post(self, request,*args, **kwargs):
        pattern = r'^(09)[1-3][0-9]\d{7}$'
        receiver = request.data['receiver']
        if not re.match(pattern, receiver) and not len(receiver) == 11:
            return Response({"Error":"The Mobile Number is Not True"})

        mobile = User.objects.filter(mobile_number = receiver)

        if mobile:
            return Response({"Messages": "You Login with the number already"},status = status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            """i want serilizer that data come to check to validated"""
            serializer = RequestOTPSerializer(data = request.data)
            if serializer.is_valid():
                data = serializer.validated_data
                """make a recorde of my model"""
                try:
                    otp = SendSmsRequest.objects.generate(data)
                    return Response(status = status.HTTP_200_OK, data = RequestOTPResponseSerializer(otp).data)
                except Exception as e:
                    return Response({"Messages": "Server Unavailable"}, status = status.HTTP_500_INTERNAL_SERVER_ERROR, data = serializer.errors)
            else:
                return Response({"Messages": "Your Number is inValid"},status = status.HTTP_400_BAD_REQUEST, data = serializer.errors)


class VarifyOtpCodeView(APIView):
    queryset = User.objects.all()
    serializer_class = VarifyOtpRequestSerializer

    def post(self, request):

        serializer = VarifyOtpRequestSerializer(data = request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            """check the code client sent to server and check the code is valid or not"""
            if SendSmsRequest.objects.is_valid(data['receiver'], data['code']):
                return Response({"Success": "Your Code is valid next to Signup"}, status = status.HTTP_200_OK)
            else:
                """if request_id or code or receiver was not True return 401"""
                return Response({"Messages": "Your Code is  invalid "}, status = status.HTTP_401_UNAUTHORIZED)
            
        else:
            """ if else the code of send sms is not valid"""
            return Response({"Messages": "There is a problem "}, status = status.HTTP_400_BAD_REQUEST, data = serializer.errors)


       