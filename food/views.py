from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Food
from .serializers import FoodSerializer


@api_view(['GET'])
def get_foods(request):
    foods = Food.objects.all()
    serializer = FoodSerializer(foods, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_food(request, pk):
    try:
        food = Food.objects.get(id=pk)
    except Food.DoesNotExist:
        return Response({"error": "Food not found"}, status=404)

    serializer = FoodSerializer(food)
    return Response(serializer.data)