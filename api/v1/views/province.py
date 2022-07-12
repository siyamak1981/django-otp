from accounts.models import Province
from api.permissions import IsActiveOrReadOnly
from rest_framework import viewsets
from api.v1.serializers.province import ProvinceSerializer



class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    permission_classes = [IsActiveOrReadOnly]
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
