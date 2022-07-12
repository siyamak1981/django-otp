from rest_framework import serializers

from accounts.models import City 




#######################
### City Serializer ###
####################### 
class CitySerializer(serializers.ModelSerializer):
  
    class Meta:
        model = City
        fields = "__all__"
