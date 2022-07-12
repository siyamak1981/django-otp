
from rest_framework import serializers 
from api.v1.serializers.otp import VarifyOtpRequestSerializer
from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.contrib.auth import get_user_model
User = get_user_model()






#######################
### User Serializer ###
####################### 
class UserSerializer(serializers.ModelSerializer):

    sendsms = VarifyOtpRequestSerializer(write_only=True)
    class Meta:
        model = User
        fields = ["first_name","mobile_number", "last_name", "password", "email", "sendsms"]  
        


class LoginSerializer(serializers.Serializer):
    
    mobile_number = serializers.CharField()
    password = serializers.CharField(required=True, write_only=True)



class RegisterSerializer(serializers.Serializer):
    
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    ("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                ("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
          
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user