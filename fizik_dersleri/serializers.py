from rest_framework import serializers
from .models import Ders

class DersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ders
        fields=['id','ad','aciklama']