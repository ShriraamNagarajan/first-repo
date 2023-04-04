from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Bookings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']



class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'Title', 'Price', 'Inventory']
        read_only_fields = ['Id']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'