from django.shortcuts import render
from rest_framework import generics
from .models import Ders
from .serializers import DersSerializer

class DersListCreate(generics.ListCreateAPIView):
    queryset=Ders.objects.all()
    serializer_class=DersSerializer
    
class DersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Ders.objects.all()
    serializer_class=DersSerializer    
