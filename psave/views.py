from rest_framework import viewsets, authentication, permissions

from psave.models import Data
from psave.serializers import DataSerializer

# Create your views here.


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]
