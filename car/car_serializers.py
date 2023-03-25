from rest_framework import serializers
from .models import Car, Brand

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car 
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand 
        fields = '__all__'
