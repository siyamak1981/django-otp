from rest_framework import serializers

from accounts.models import Province 



#######################
### Province Serializer ###
####################### 
class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = "__all__"

