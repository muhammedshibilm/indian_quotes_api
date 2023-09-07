from rest_framework import serializers
from .models import RandomData

class RandomDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RandomData
        fields = ['author','text','image_url']