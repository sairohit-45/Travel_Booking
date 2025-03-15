from django.db import models
from django.contrib.auth.models import User

class TravelOption(models.Model):
    travel_id = models.CharField(max_length=10, unique=True)
    type = models.CharField(max_length=10, choices=[('Flight', 'Flight'), ('Train', 'Train'), ('Bus', 'Bus')])
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.IntegerField()

    def __str__(self):
        return f"{self.type} from {self.source} to {self.destination}"

class Booking(models.Model):
    booking_id = models.CharField(max_length=10, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_option = models.ForeignKey('TravelOption', on_delete=models.CASCADE)
    number_of_seats = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], default='Confirmed')

    def save(self, *args, **kwargs):
        if not self.booking_id:  # Only generate if not already set
            # Generate a unique booking_id (e.g., BK000001, BK000002, etc.)
            count = Booking.objects.count() + 1
            self.booking_id = f"BK{count:06d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking {self.booking_id} by {self.user.username}"