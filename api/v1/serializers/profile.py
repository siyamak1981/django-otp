from cgitb import lookup
from operator import truediv
from accounts.models import Profile, User
from rest_framework import serializers
from api.v1.serializers.otp import VarifyOtpRequestSerializer

from api.v1.serializers.users import UserSerializer 
#######################
### Profile Serializer ###
####################### 

class ProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only = True)
    class Meta:
        model = Profile
        fields = "__all__"
