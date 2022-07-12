
from api.permissions import IsActiveOrReadOnly
from api.v1.serializers.session import SessionSerializer
from session.models import Session
from rest_framework import viewsets



class SessionViewSet(viewsets.ModelViewSet):
    """This class defined the create behaviour of our rest api."""
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsActiveOrReadOnly]