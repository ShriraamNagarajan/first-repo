from django.urls import path, include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('booking/', include(router.urls)),
    path('users/', views.UserViewSet.as_view()),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
   
]