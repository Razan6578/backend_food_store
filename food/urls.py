from django.urls import path
from .views import FoodListView, FoodDetailView

urlpatterns = [
    path('foods/', FoodListView.as_view()),
    path('foods/<int:pk>/', FoodDetailView.as_view()),
]
