from rest_framework import serializers
from psave.models import Data


class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ['host', 'cpu', 'processes', 'memory', 'disk', 'date']
