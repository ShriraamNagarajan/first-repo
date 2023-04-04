from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes, throttle_classes

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets

from .models import Menu, Bookings
from django.contrib.auth.models import User
from .serializers import UserSerializer, MenuSerializer, BookingSerializer

# Create your views here.
def sayHello(request):
    return HttpResponse('SayHello')


def index(request):
    return render(request, 'index.html', {})

#@permission_classes([IsAuthenticated])
class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer



class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer



class BookingViewSet(viewsets.ModelViewSet):
    queryset = Bookings.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer

