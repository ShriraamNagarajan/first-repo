from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('users/', views.UserViewSet.as_view()),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('message/', views.msg), 
]