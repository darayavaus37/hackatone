from django.shortcuts import render
from rest_framework import viewsets
from .models import Resource
from .serializers import ResourceSerializer

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

