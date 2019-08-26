from django.shortcuts import render
from rest_framework import viewsets

from .serializers import LoggerSerializer
from .models import Logger

# Create your views here.

class LoggerViewSet(viewsets.ModelViewSet):
    queryset = Logger.objects.all().order_by('id')
    serializer_class = LoggerSerializer