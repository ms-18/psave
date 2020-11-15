from rest_framework import mixins, permissions, viewsets, response, status
from rest_framework.decorators import action

from psave.models import Data
from psave.serializers import DataSerializer

# Create your views here.


class DataViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    serializer_class = DataSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return Data.objects.filter(host__api_user=self.request.user)

    @action(methods=["get"], detail=False)
    def latest(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(data=queryset.last())

        return response.Response(serializer.data, status=status.HTTP_200_OK)

    # override create to pass the host to serializer
    def create(self, request, *args, **kwargs):
        data = request.data
        print(data)
        data["host"] = request.user.host.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
