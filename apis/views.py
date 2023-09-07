from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RandomData
from .serializers import RandomDataSerializer
import random

# Create your views here.

class RandomAPIView(APIView):
    def get(self, request):
        random_data = RandomData.objects.all()
        if random_data:
            random_item = random.choice(random_data)
            serializer = RandomDataSerializer(random_item)
            return Response(serializer.data)
        else:
            return Response({"error": "no data available"})