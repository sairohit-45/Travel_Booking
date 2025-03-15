from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import TravelOption, Booking
from django.contrib import messages
import uuid

def travel_options(request):
    options = TravelOption.objects.all()
    if request.method == 'POST':
        type_filter = request.POST.get('type')
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        if type_filter:
            options = options.filter(type=type_filter)
        if source:
            options = options.filter(source__icontains=source)
        if destination:
            options = options.filter(destination__icontains=destination)
        if date:
            options = options.filter(date_time__date=date)
    return render(request, 'travel/options.html', {'options': options})

@login_required
def book_travel(request, travel_id):
    travel_option = get_object_or_404(TravelOption, id=travel_id)  # Assuming id, not travel_id
    if request.method == 'POST':
        number_of_seats = int(request.POST.get('number_of_seats'))
        if number_of_seats <= 0 or number_of_seats > travel_option.available_seats:
            messages.error(request, "Invalid number of seats!")
            return redirect('book_travel', travel_id=travel_id)
        total_price = travel_option.price * number_of_seats
        booking = Booking.objects.create(
            user=request.user,
            travel_option=travel_option,
            number_of_seats=number_of_seats,
            total_price=total_price
        )
        travel_option.available_seats -= number_of_seats
        travel_option.save()
        messages.success(request, "Booking confirmed!")
        return redirect('my_bookings')
    return render(request, 'travel/book.html', {'travel_option': travel_option})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'travel/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id, user=request.user)
    if booking.status == 'Confirmed':
        booking.status = 'Cancelled'
        booking.travel_option.available_seats += booking.number_of_seats
        booking.travel_option.save()
        booking.save()
        messages.success(request, "Booking cancelled successfully!")
    return redirect('my_bookings')