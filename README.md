# Workshop Management System

A comprehensive, production-ready Django web application designed for automotive workshop owners to efficiently manage workshop operations, track customer jobs, manage inventory, and handle bookings. Built with simplicity and usability in mind, this system streamlines daily workshop operations with minimal complexity.

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage Guide](#-usage-guide)
- [Development](#-development)
- [Deployment](#-deployment)
- [Project Structure](#-project-structure)
- [API Documentation](#-api-documentation)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

### Core Functionality

- **🔐 Secure Authentication System**
  - Django's built-in authentication with session management
  - Login required for all pages (except login page)
  - Secure password validation and user management

- **📊 Comprehensive Dashboard**
  - Real-time job statistics (Total, Pending, In Progress, Completed)
  - Low stock alerts for inventory items
  - Recent jobs overview
  - Quick action buttons for common tasks

- **🔧 Workshop Job Management**
  - Complete job lifecycle tracking (Pending → In Progress → Completed)
  - Customer and vehicle information management
  - Multiple work types (Repair, Service, Radiator Replacement, Other)
  - Automatic date tracking (received, completed)
  - Invoice number tracking
  - Notes and additional information fields
  - Color-coded status indicators for quick visual reference

- **📦 Inventory Management**
  - Track multiple part types (Radiators, Oil Coolers, Intercoolers, Fuel Tanks, Others)
  - Customer and order information tracking
  - Status management (Pending, In Progress, Completed)
  - Invoice number tracking
  - Automatic low stock alerts (quantity < 5)
  - Date received and completion tracking

- **📅 Booking System**
  - Vehicle and radiator booking management
  - Calendar-based booking interface
  - All-day and hourly booking options
  - Customer contact information
  - Booking status tracking (Pending, Confirmed, Completed, Cancelled)

- **📈 Reporting System**
  - Generate reports for jobs and inventory
  - Export capabilities for data analysis

### User Experience

- **🎨 Clean, Modern UI**
  - Intuitive navigation
  - Color-coded status indicators
  - Responsive design
  - Minimal clicks for common operations

- **⚡ Performance Optimized**
  - Efficient database queries
  - Static file optimization with WhiteNoise
  - Connection pooling for PostgreSQL

## 🛠 Tech Stack

### Backend
- **Framework**: Django 5.2.5
- **Language**: Python 3.11.9
- **Database**: 
  - Production: Supabase PostgreSQL (with SSL support)
  - Development: SQLite (default, fallback)
- **WSGI Server**: Gunicorn 21.2.0
- **Static Files**: WhiteNoise 6.6.0

### Frontend
- **Templates**: Django Template Engine
- **Styling**: Custom CSS (no frameworks)
- **JavaScript**: Vanilla JavaScript (minimal)

### Database & Infrastructure
- **ORM**: Django ORM
- **Database Adapter**: psycopg2-binary 2.9.9
- **Connection Management**: dj-database-url 2.1.0
- **Environment Variables**: python-decouple 3.8

### Additional Tools
- **Excel Support**: openpyxl 3.1.2 (for reports)
- **Deployment**: Render, Railway, Heroku compatible

## 🏗 Architecture

### Application Structure

The application follows Django's app-based architecture with clear separation of concerns:

- **`workshop_manager/`**: Main project configuration
- **`jobs/`**: Workshop job tracking application
- **`inventory/`**: Parts inventory management application
- **`bookings/`**: Booking and scheduling application
- **`reports/`**: Reporting and analytics application

### Database Architecture

- **PostgreSQL** for production (Supabase)
- **SQLite** for local development
- Automatic SSL configuration for Supabase connections
- Connection pooling support

### Security Features

- CSRF protection enabled
- XSS protection
- Secure session management
- Password validation
- Environment-based configuration
- SSL/TLS for database connections

## 📥 Installation

### Prerequisites

- **Python**: 3.8 or higher (3.11.9 recommended)
- **pip**: Python package manager
- **Git**: Version control (optional)
- **PostgreSQL**: For production (via Supabase or self-hosted)

### Step-by-Step Installation

#### 1. Clone the Repository

```bash
git clone <repository-url>
cd Stock-Management-System
```

Or navigate to the project directory if you already have it:

```bash
cd Stock-Management-System
```

#### 2. Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Django 5.2.5
- psycopg2-binary 2.9.9
- python-decouple 3.8
- dj-database-url 2.1.0
- gunicorn 21.2.0
- whitenoise 6.6.0
- openpyxl 3.1.2

#### 4. Configure Environment Variables

Create a `.env` file in the project root:

```bash
cp env.example .env
```

Edit `.env` with your configuration:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration (Optional - uses SQLite if not set)
DATABASE_URL=postgresql://postgres:password@db.project.supabase.co:5432/postgres?sslmode=require
```

**Note**: If `DATABASE_URL` is not set, the application will automatically use SQLite for local development.

#### 5. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

This creates all necessary database tables.

#### 6. Create Superuser Account

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account. You'll need this to log into the application.

#### 7. Collect Static Files (Production)

```bash
python manage.py collectstatic --noinput
```

#### 8. Start Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## ⚙️ Configuration

### Database Configuration

#### Using Supabase PostgreSQL (Recommended for Production)

1. **Create a Supabase Project**
   - Go to [supabase.com](https://supabase.com)
   - Create a new project
   - Note your database password

2. **Get Connection String**
   - Navigate to Settings → Database
   - Copy the connection string from the "URI" tab
   - Add `?sslmode=require` at the end

3. **Set Environment Variable**
   ```env
   DATABASE_URL=postgresql://postgres:YOUR-PASSWORD@db.PROJECT-REF.supabase.co:5432/postgres?sslmode=require
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

#### Using SQLite (Default for Development)

If `DATABASE_URL` is not set, the application automatically uses SQLite. No additional configuration needed.

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `SECRET_KEY` | Django secret key | (generated) | Yes |
| `DEBUG` | Debug mode | `True` | No |
| `ALLOWED_HOSTS` | Allowed hostnames | `localhost,127.0.0.1` | Yes (production) |
| `DATABASE_URL` | Database connection string | None (uses SQLite) | No |

### Static Files Configuration

Static files are automatically handled by WhiteNoise in production. No additional configuration needed.

## 📖 Usage Guide

### Accessing the Application

1. Navigate to `http://127.0.0.1:8000/` (development) or your production URL
2. You'll be redirected to the login page
3. Log in with your superuser credentials

### Managing Workshop Jobs

#### Viewing Jobs
- Click **"Jobs"** in the navigation bar
- View all jobs with their current status
- Jobs are sorted by most recent first

#### Creating a New Job
1. Click **"Add Job"** in the navigation bar or from the jobs list
2. Fill in the required information:
   - Customer name
   - Contact number
   - Vehicle registration
   - Vehicle make and model
   - Work type
   - Status (defaults to "Pending")
   - Notes (optional)
3. Click **"Save"**

#### Job Status Management
- **Pending** (🔴 Red): Job is waiting to be started
- **In Progress** (🟠 Orange): Work is currently being performed
- **Completed** (🟢 Green): Job is finished

Status automatically updates the completion date when changed to "Completed".

#### Editing and Deleting Jobs
- Click **"Edit"** on any job card to modify details
- Click **"Delete"** from the job detail page to remove a job
- Confirmation required before deletion

### Managing Inventory

#### Viewing Inventory
- Click **"Inventory"** in the navigation bar
- View all parts with their current stock status
- Low stock items (quantity < 5) are highlighted in red

#### Adding New Inventory Items
1. Click **"Add Stock"** in the navigation bar
2. Fill in the part information:
   - Name/Model
   - Part type (Radiator, Oil Cooler, Intercooler, Fuel Tank, Other)
   - Customer name (optional)
   - Contact number (optional)
   - Invoice number (optional)
   - Status
   - Notes (optional)
3. Click **"Save"**

#### Low Stock Alerts
- Items with quantity less than 5 are automatically highlighted
- Low stock items appear on the dashboard
- Helps prevent stockouts

### Managing Bookings

#### Viewing Bookings
- Click **"Bookings"** in the navigation bar
- View calendar-based booking interface
- Filter by booking type (Vehicle or Radiator)

#### Creating a Booking
1. Click **"Add Booking"** or select a date on the calendar
2. Choose booking type (Vehicle or Radiator)
3. Fill in customer and booking details
4. Select date and time (or mark as all-day)
5. Save the booking

### Dashboard Overview

The dashboard provides:
- **Quick Statistics**: Total jobs, pending, in progress, completed
- **Recent Jobs**: Latest job entries
- **Low Stock Alerts**: Items needing restocking
- **Quick Actions**: Direct links to common tasks

### Django Admin Panel

Access the admin panel at `/admin/`:
- Manage all models directly
- Bulk operations
- Advanced filtering and search
- User management

## 🔧 Development

### Running Tests

```bash
python manage.py test
```

### Making Model Changes

After modifying models in any app:

```bash
# Create migration files
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### Development Server Options

```bash
# Run on default port (8000)
python manage.py runserver

# Run on custom port
python manage.py runserver 8080

# Run on all interfaces
python manage.py runserver 0.0.0.0:8000
```

### Code Style

- Follow PEP 8 Python style guide
- Use Django's coding style conventions
- Keep functions and classes focused and small

### Debugging

- Set `DEBUG=True` in `.env` for detailed error pages
- Check Django logs in the console
- Use Django's debug toolbar (if installed)

## 🚀 Deployment

### Deployment Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Set `ALLOWED_HOSTS` with your domain
- [ ] Generate a new `SECRET_KEY` for production
- [ ] Configure `DATABASE_URL` with production database
- [ ] Run `collectstatic` to gather static files
- [ ] Set up proper logging
- [ ] Configure SSL/TLS certificates
- [ ] Set up backup strategy

### Deploying to Render

1. **Set Environment Variables** in Render dashboard:
   ```
   SECRET_KEY=your-production-secret-key
   DEBUG=False
   ALLOWED_HOSTS=your-app.onrender.com
   PYTHON_VERSION=3.11.9
   DATABASE_URL=postgresql://postgres:password@db.project.supabase.co:5432/postgres?sslmode=require
   ```

2. **Configure Build Command**:
   ```bash
   pip install -r requirements.txt && python manage.py collectstatic --noinput
   ```

3. **Configure Start Command**:
   ```bash
   gunicorn workshop_manager.wsgi:application
   ```

4. **Run Migrations** after deployment:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

### Deploying to Other Platforms

The application is compatible with:
- **Railway**: Uses `Procfile` automatically
- **Heroku**: Uses `Procfile` automatically
- **DigitalOcean App Platform**: Configure via dashboard
- **AWS Elastic Beanstalk**: Requires `Procfile`
- **Self-hosted**: Use Gunicorn with Nginx

### Production Settings

Ensure these are set in production:

```env
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SECRET_KEY=<strong-random-key>
DATABASE_URL=<production-database-url>
```

## 📁 Project Structure

```
Stock-Management-System/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── runtime.txt               # Python version specification
├── Procfile                  # Process file for deployment
├── .env                      # Environment variables (not in git)
├── .gitignore               # Git ignore rules
│
├── workshop_manager/        # Main project configuration
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Root URL configuration
│   ├── views.py             # Root views
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
│
├── jobs/                    # Workshop job tracking app
│   ├── models.py            # Job model definitions
│   ├── views.py             # Job views and logic
│   ├── forms.py             # Job forms
│   ├── urls.py              # Job URL routing
│   ├── admin.py             # Admin configuration
│   └── migrations/          # Database migrations
│
├── inventory/               # Inventory management app
│   ├── models.py            # Inventory model definitions
│   ├── views.py             # Inventory views
│   ├── forms.py             # Inventory forms
│   ├── urls.py              # Inventory URL routing
│   ├── admin.py             # Admin configuration
│   └── migrations/          # Database migrations
│
├── bookings/                # Booking management app
│   ├── models.py            # Booking model definitions
│   ├── views.py             # Booking views
│   ├── forms.py             # Booking forms
│   ├── urls.py              # Booking URL routing
│   ├── admin.py             # Admin configuration
│   └── migrations/          # Database migrations
│
├── reports/                 # Reporting app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   ├── dashboard.html       # Dashboard template
│   ├── jobs/                # Job templates
│   ├── inventory/           # Inventory templates
│   ├── bookings/            # Booking templates
│   ├── reports/             # Report templates
│   └── registration/        # Auth templates
│
└── static/                  # Static files
    └── css/
        └── style.css        # Custom styles
```

## 🔌 API Documentation

The application primarily uses server-side rendering. For API access, use Django's admin panel or extend with Django REST Framework if needed.

### URL Patterns

- `/` - Dashboard
- `/login/` - Login page
- `/logout/` - Logout
- `/jobs/` - Job list
- `/jobs/<id>/` - Job detail
- `/inventory/` - Inventory list
- `/bookings/` - Booking calendar
- `/reports/` - Reports page
- `/admin/` - Django admin panel

## 🐛 Troubleshooting

### Common Issues

#### Database Connection Errors

**Problem**: Cannot connect to Supabase PostgreSQL

**Solutions**:
1. Verify `DATABASE_URL` is set correctly in `.env`
2. Check Supabase project is active (not paused)
3. Ensure connection string includes `?sslmode=require`
4. Verify password is correct and URL-encoded if needed

#### Migration Errors

**Problem**: Migrations fail to run

**Solutions**:
1. Ensure database is accessible
2. Check for conflicting migrations: `python manage.py showmigrations`
3. Try: `python manage.py migrate --run-syncdb`

#### Static Files Not Loading

**Problem**: CSS/styles not appearing

**Solutions**:
1. Run `python manage.py collectstatic`
2. Check `STATIC_ROOT` and `STATIC_URL` in settings
3. Verify WhiteNoise is configured (already done)

#### psycopg2 Installation Issues

**Problem**: `Error loading psycopg2 module`

**Solutions**:
1. Ensure Python version is 3.11.9 (set `PYTHON_VERSION=3.11.9` in deployment)
2. Install system dependencies: `apt-get install libpq-dev` (Linux)
3. Use `psycopg2-binary` (already in requirements.txt)

#### Permission Errors

**Problem**: Permission denied errors

**Solutions**:
1. Check file permissions
2. Ensure virtual environment is activated
3. Verify user has write permissions in project directory

### Getting Help

- Check Django documentation: https://docs.djangoproject.com/
- Review error logs in console or deployment platform
- Check Supabase dashboard for database issues
- Verify environment variables are set correctly

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Write clear commit messages
- Add tests for new features
- Update documentation as needed
- Keep code simple and maintainable

## 📄 License

This project is created for workshop management purposes. All rights reserved.

## 👤 Support

For issues, questions, or contributions:

- **Documentation**: See Django documentation at https://docs.djangoproject.com/
- **Issues**: Open an issue in the repository
- **Questions**: Contact the project maintainer

## 🙏 Acknowledgments

- Built with [Django](https://www.djangoproject.com/)
- Database powered by [Supabase](https://supabase.com/)
- Deployed on [Render](https://render.com/)

---

**Made with ❤️ for workshop management**
