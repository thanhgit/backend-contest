
from rest_framework import serializers
from .models import Logger

class LoggerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Logger
        fields = ('filename', 'filepath', 'client_ip', 'file_size', 'time')