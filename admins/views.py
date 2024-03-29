from django.shortcuts import render
from rest_framework import generics
from .models import Center
from .serializers import CenterListCreateSerializer

class CenterListCreateAPIView(generics.ListCreateAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterListCreateSerializer