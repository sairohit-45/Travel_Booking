# Travel Booking Application

A Django-based web application for booking travel options (flights, trains, buses) with user authentication, booking management, and a responsive frontend.

## Prerequisites
- Python 3.11+ (Download from [python.org](https://www.python.org/downloads/))
- Git (Download from [git-scm.com](https://git-scm.com/downloads))
- MySQL (Optional, for bonus points; Download from [mysql.com](https://dev.mysql.com/downloads/mysql/))

## Setup Instructions (Local)
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/travel-booking.git
   cd travel-booking
2. **Create and Activate a Virtual Environment:**
python -m venv myenv
myenv\Scripts\activate  # Windows
3. **Install Dependencies**
pip install django mysqlclient

4. **Configure Database:**

**For MySQL (optional):**
Install MySQL and set a root password (e.g., mypassword123).
**Open MySQL:** mysql -u root -p, enter password.
**Create database:** CREATE DATABASE travel_booking_db;
**Update travel_booking/settings.py:**
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'travel_booking_db',
        'USER': 'root',
        'PASSWORD': 'mypassword123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5. **Apply Migrations**
python manage.py makemigrations
python manage.py migrate

6. **Create a SuperUser:**
python manage.py createsuperuser

7. **Run the Server**
python manage.py runserver

**Adding Travel Options**
1. **Start the Server**
python manage.py runserver

2. **Log In to Admin Panel:**

Go to http://127.0.0.1:8000/admin/.
Use superuser credentials (e.g., admin / admin123).

3. **Add Travel Options:**

Under “Travel,” click “Travel options.”
Click “Add travel option” and fill in:
Travel ID: Unique ID (e.g., F001).
Type: Select Flight, Train, or Bus.
Source: Starting location (e.g., New York).
Destination: Ending location (e.g., London).
Date and time: e.g., 2025-04-01 10:00:00.
Price: e.g., 200.00.
Available seats: e.g., 50.
Click “Save.”
Repeat to add more options (e.g., T001 for Train, B001 for Bus).
