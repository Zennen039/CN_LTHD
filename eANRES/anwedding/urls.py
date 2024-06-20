from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from anwedding import views

r = routers.DefaultRouter()
r.register('homepages', views.HomePageViewSet, 'homepages')
r.register('wedding_services', views.WeddingServiceViewSet, 'wedding_services')
r.register('wedding_halls', views.WeddingHallViewSet, 'wedding_halls')
r.register('wedding_menus', views.WeddingMenuViewSet, 'wedding_menus')
r.register('wedding_bookings', views.WeddingBookingViewSet, 'wedding_bookings')
r.register('banquet_rooms', views.BanquetRoomViewSet, 'banquet_rooms')
r.register('food_items', views.FoodItemViewSet, 'food_items')
r.register('food_menus', views.FoodMenuViewSet, 'food_menus')
r.register('users', views.UserViewSet, 'users')
r.register('staffs', views.StaffViewet, 'staffs')
r.register('feedbacks', views.FeedBackViewSet, 'feedbacks')

urlpatterns = [
    path('', include(r.urls))
]