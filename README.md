# Workshop Management System

A production-ready Django web application for a mechanic workshop owner to track workshop jobs (cars coming in) and manage radiator inventory with minimal clicks and no unnecessary complexity.

## Features

- **Secure Authentication**: Login required for all pages except login page
- **Workshop Job Tracking**: Add, view, edit, and delete workshop jobs with customer and vehicle information
- **Radiator Inventory Management**: Track radiator stock with automatic low stock alerts (quantity < 5)
- **Dashboard**: Quick overview of jobs statistics and low stock items
- **Clean UI**: Simple, vibrant design with color-coded statuses and easy navigation

## Tech Stack

- **Backend**: Django 5.2.5 (Python)
- **Database**: Supabase PostgreSQL (configurable via DATABASE_URL, falls back to SQLite for local development)
- **Frontend**: HTML & CSS (no frameworks)
- **Authentication**: Django's built-in authentication system

## Project Structure

```
workshop_manager/
├── manage.py
├── workshop_manager/
│   ├── settings.py
│   ├── urls.py
│   └── views.py
├── jobs/                    # Workshop job tracking app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── inventory/              # Radiator inventory app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── templates/              # HTML templates
│   ├── base.html
│   ├── dashboard.html
│   ├── registration/
│   ├── jobs/
│   └── inventory/
└── static/
    └── css/
        └── style.css
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Navigate to Project Directory

```bash
cd Stock-Management-System
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Database (Optional - Supabase PostgreSQL)

By default, the application uses SQLite for local development. To use Supabase PostgreSQL:

1. Follow the detailed guide in [SUPABASE_SETUP.md](SUPABASE_SETUP.md)
2. Or simply set the `DATABASE_URL` environment variable in a `.env` file

If you skip this step, the app will use SQLite automatically.

### Step 5: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin user. You'll need this to log in to the application.

### Step 7: Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

### Step 8: Access the Application

1. Open your browser and navigate to `http://127.0.0.1:8000/`
2. You'll be redirected to the login page
3. Log in with the superuser credentials you created

## Usage

### Workshop Jobs

- **View All Jobs**: Click "Jobs" in the navigation bar
- **Add New Job**: Click "Add Job" in the navigation bar or from the jobs list page
- **View Job Details**: Click "View" on any job card
- **Edit Job**: Click "Edit" on any job card or from the job detail page
- **Delete Job**: Click "Delete" from the job detail page

**Job Fields:**
- Customer name
- Contact number
- Vehicle registration number
- Vehicle make & model
- Work type (Repair, Service, Radiator Replacement, Other)
- Status (Pending, In Progress, Completed)
- Date received (automatically set)
- Notes (optional)

**Status Colors:**
- 🔴 Red: Pending
- 🟠 Orange: In Progress
- 🟢 Green: Completed

### Radiator Inventory

- **View Inventory**: Click "Inventory" in the navigation bar
- **Add New Radiator**: Click "Add Stock" in the navigation bar or from the inventory list page
- **Edit Radiator**: Click "Edit" on any radiator in the table
- **Delete Radiator**: Click "Delete" on any radiator in the table

**Radiator Fields:**
- Name/Model
- Compatible vehicles
- Quantity in stock
- Cost price
- Selling price

**Low Stock Alert:**
- Items with quantity < 5 are automatically highlighted in red
- Low stock items appear on the dashboard

### Dashboard

The dashboard provides:
- Quick statistics (Total Jobs, Pending, In Progress, Completed)
- Recent jobs list
- Low stock alerts
- Quick action buttons

## Development

### Running Tests

```bash
python manage.py test
```

### Accessing Admin Panel

Django admin panel is available at `http://127.0.0.1:8000/admin/`

### Making Changes to Models

After modifying models in `jobs/models.py` or `inventory/models.py`:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Production Deployment

For production deployment:

1. Set `DEBUG = False` in your `.env` file or environment variables
2. Set `ALLOWED_HOSTS` in your `.env` file (comma-separated list of domains)
3. Configure Supabase PostgreSQL database (see [SUPABASE_SETUP.md](SUPABASE_SETUP.md))
4. Set `DATABASE_URL` environment variable with your Supabase connection string
5. Set up static file serving (WhiteNoise is already configured)
6. Use environment variables for all sensitive settings (SECRET_KEY, DATABASE_URL, etc.)

The application is already configured to use environment variables via `python-decouple` and `dj-database-url`.

## License

This project is created for workshop management purposes.

## Support

For issues or questions, please refer to the Django documentation: https://docs.djangoproject.com/
