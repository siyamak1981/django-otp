from rest_framework import serializers
from accounts.models import SendSmsRequest
from painless.models.choices import OTPCHannel





class RequestOTPSerializer(serializers.Serializer):
    """get data from client"""
    receiver = serializers.CharField(max_length = 225, allow_null = False)
    channel = serializers.ChoiceField(allow_null = False, choices = OTPCHannel.choices, default = OTPCHannel.PHONE)


class RequestOTPResponseSerializer(serializers. ModelSerializer):
    """return request_id from server to client"""
    class Meta:
        model = SendSmsRequest
        fields = ['request_id', 'code']



class VarifyOtpRequestSerializer(serializers.Serializer):
    # request_id = serializers.CharField(allow_null = False)
    code = serializers.CharField(max_length = 4, allow_null = False)
    receiver = serializers.CharField(max_length = 64, allow_null = False)
    


class ObtainTokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length = 128, allow_null = False)
    refresh = serializers.CharField(max_length = 128, allow_null = False)
    created = serializers.BooleanField()