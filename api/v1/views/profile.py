
from accounts.models import Profile, User
from rest_framework import generics
from api.permissions import  IsSuperUserOrStaffReadOnly
from api.v1.serializers.profile import ProfileSerializer
from rest_framework.response import Response
from rest_framework import viewsets




class ProfileListViewSet(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsSuperUserOrStaffReadOnly]



class ProfileUpdateViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsSuperUserOrStaffReadOnly]
    lookup_field = 'pk'
    lookup_url_kwarg = "pk"
    http_method_names = ['put']
   
