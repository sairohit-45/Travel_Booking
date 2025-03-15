# Travel Booking Application

A Django-based web application for booking travel options (flights, trains, buses) with user authentication, booking management, and a responsive frontend using Bootstrap.

---

## Prerequisites
- **Python 3.11+** ([Download](https://www.python.org/downloads/))
- **Git** ([Download](https://git-scm.com/downloads))
- **MySQL (Optional)** ([Download](https://dev.mysql.com/downloads/mysql/)) or use **SQLite** (default)

---

## Cloning and Running Locally

### 1. Clone the Repository
```bash
git clone https://github.com/sairohit-45/Travel_Booking.git
cd Travel_Booking
```

### 2. Set Up a Virtual Environment
#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
#### Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django mysqlclient
```
> **Note:** Use `mysqlclient` only if you plan to use MySQL. For SQLite, it's not required.

### 4. Configure the Database
#### **SQLite (Default):**
No extra setup is needed as SQLite uses the `db.sqlite3` file automatically.

#### **MySQL (Optional):**
1. **Create a Database:**
   ```bash
   mysql -u root -p
   ```
   Enter your MySQL password and run:
   ```sql
   CREATE DATABASE travel_booking_db;
   EXIT;
   ```

2. **Update the Database Settings:**
   Open `travel_booking/settings.py` and update the `DATABASES` section:
   ```python
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
   ```

### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server
```bash
python manage.py runserver
```
Now, open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the application in action.

---

## Creating a Superuser

1. **Run the Superuser Creation Command:**
   ```bash
   python manage.py createsuperuser
   ```
2. **Enter the Required Details:**
   - **Username:** e.g., `admin`
   - **Email:** e.g., `admin@example.com` (optional)
   - **Password:** e.g., `admin123` (confirm by entering it twice)

3. **Confirmation:**
   You should see a confirmation message stating “Superuser created successfully.”

---

## Adding Travel Options via the Admin Panel

1. **Start the Server (if not already running):**
   ```bash
   python manage.py runserver
   ```

2. **Access the Admin Panel:**
   Open your browser and go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/), then log in using your superuser credentials (e.g., `admin` / `admin123`).

3. **Add Travel Options:**
   - In the admin dashboard, locate and click on “Travel options” under the “Travel” section.
   - Click “Add travel option” and fill in the following details:
     - **Travel ID:** e.g., `F001` (unique, max 10 characters)
     - **Type:** Select Flight, Train, or Bus from the dropdown
     - **Source:** e.g., `New York`
     - **Destination:** e.g., `London`
     - **Date and Time:** e.g., `2025-04-01 10:00:00` (use the calendar widget)
     - **Price:** e.g., `200.00`
     - **Available Seats:** e.g., `50`
   - Click “Save” to add the travel option.
   - Repeat the process to add more travel options (e.g., `T001` for Train, `B001` for Bus).

---

## Features
- **User Authentication:** Register, log in, log out, and update profiles.
- **Travel Options:** View and filter travel options by type, source, destination, and date.
- **Booking:** Book travel with seat selection and pricing details.
- **Booking Management:** View and cancel bookings.
- **Responsive Design:** Built with Bootstrap for a mobile-friendly experience.
