from django.http import HttpResponse
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from .car_serializers import CarSerializer
from .models import Car

import requests

# Create your views here.

def index(request):
    r = requests.get('https://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')


class CarListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # 1. List all

    def get(self, request, *args, **kwargs):
        '''
        List all the car items for given requested user
        '''
        cars = Car.objects.filter(user=request.user.id)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):

        # Create the car with given car data

        data = {
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'content': request.data.get('content'),
            'user': request.user.id
        }
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarDetailAPIView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, car_id, user_id):
        '''
        Helper method to get the object with given car_id, and user_id
        '''
        try:
            return Car.objects.get(id=car_id, user = user_id)
        except Car.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, car_id, *args, **kwargs):
        '''
        Retrieves the Car with given car_id
        '''
        car_instance = self.get_object(car_id, request.user.id)
        if not car_instance:
            return Response(
                {"res": "Object with car id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CarSerializer(car_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, car_id, *args, **kwargs):
        '''
        Updates the car item with given car_id if exists
        '''
        car_instance = self.get_object(car_id, request.user.id)
        if not car_instance:
            return Response(
                {"res": "Object with car id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'content': request.data.get('content'),
            'user': request.user.id

        }
        serializer = CarSerializer(instance = car_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, car_id, *args, **kwargs):
        '''
        Deletes the car item with given car_id if exists
        '''
        car_instance = self.get_object(car_id, request.user.id)
        if not car_instance:
            return Response(
                {"res": "Object with car id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        car_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )