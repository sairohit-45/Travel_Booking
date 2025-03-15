from django.contrib import admin
from .models import Booking, TravelOption

admin.site.register(TravelOption)

admin.site.register(Booking)