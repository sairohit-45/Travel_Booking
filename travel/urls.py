
from django.urls import path
from . import views

urlpatterns = [
    path('', views.travel_options, name='travel_options'),
    path('book/<str:travel_id>/', views.book_travel, name='book_travel'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel/<str:booking_id>/', views.cancel_booking, name='cancel_booking'),
]