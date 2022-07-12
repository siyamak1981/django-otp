from accounts.models import City
from api.permissions import IsActiveOrReadOnly
from rest_framework import viewsets
from api.v1.serializers.city import CitySerializer




class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [IsActiveOrReadOnly]
 