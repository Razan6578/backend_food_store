from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Food
from .serializers import FoodSerializer

# Create your views here.

class FoodListView(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetailView(RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    

