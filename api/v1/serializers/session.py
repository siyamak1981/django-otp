from rest_framework import serializers 
from session.models import Session




class SessionSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Session
        fields = "__all__"
        read_only_fields = ('created', 'client_ip')

    def create(self, validated_data):
        validated_data['client_ip'] = self.context.get('request').META.get("REMOTE_ADDR")
        validated_data['uniqe_device_code'] = self.context.get('request').META.get("HTTP_USER_AGENT")
        validated_data['client_version'] = self.context.get('request').META.get("HTTP_HOST")
        validated_data['server_version'] = self.context.get('request').META.get("SERVER_NAME")
        validated_data['refresh_has_token'] = self.context.get('request').COOKIES['csrftoken']
        return Session.objects.create(**validated_data)
    
