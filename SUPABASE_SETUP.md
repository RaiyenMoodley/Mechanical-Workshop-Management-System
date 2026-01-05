# Supabase PostgreSQL Setup Guide

This guide will help you set up Supabase PostgreSQL as your database for the Workshop Management System.

## Prerequisites

- A Supabase account (sign up at [supabase.com](https://supabase.com))
- Python 3.8+ installed
- All project dependencies installed (`pip install -r requirements.txt`)

## Step 1: Create a Supabase Project

1. Go to [supabase.com](https://supabase.com) and sign in (or create an account)
2. Click "New Project"
3. Fill in your project details:
   - **Name**: Choose a name for your project (e.g., "workshop-manager")
   - **Database Password**: Create a strong password (save this securely!)
   - **Region**: Choose the region closest to you
4. Click "Create new project"
5. Wait for the project to be set up (this may take a few minutes)

## Step 2: Get Your Database Connection String

1. In your Supabase project dashboard, go to **Settings** (gear icon in the left sidebar)
2. Click on **Database** in the settings menu
3. Scroll down to the **Connection string** section
4. Select the **URI** tab
5. You'll see a connection string that looks like:
   ```
   postgresql://postgres:[YOUR-PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres
   ```
6. Copy this connection string
7. **Important**: Replace `[YOUR-PASSWORD]` with the actual database password you set when creating the project

## Step 3: Configure Your Local Environment

1. Copy the example environment file:
   ```bash
   cp env.example .env
   ```

2. Open the `.env` file in a text editor

3. Update the `DATABASE_URL` with your Supabase connection string:
   ```env
   DATABASE_URL=postgresql://postgres:your-actual-password@db.abcdefghijklmnop.supabase.co:5432/postgres
   ```

   Replace:
   - `your-actual-password` with your actual database password
   - `abcdefghijklmnop` with your actual project reference ID

4. Save the file

## Step 4: Run Database Migrations

Now that your database is configured, you need to create the database tables:

```bash
# Make sure you're in the project directory
cd Stock-Management-System

# Run migrations to create all tables in Supabase
python manage.py migrate
```

This will create all the necessary tables in your Supabase PostgreSQL database.

## Step 5: Create a Superuser

Create an admin user to access the application:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

## Step 6: Verify the Connection

1. Start your development server:
   ```bash
   python manage.py runserver
   ```

2. Open your browser and go to `http://127.0.0.1:8000/`

3. Log in with your superuser credentials

4. If everything works, you're successfully connected to Supabase!

## Step 7: (Optional) Verify in Supabase Dashboard

You can verify that your tables were created:

1. Go to your Supabase project dashboard
2. Click on **Table Editor** in the left sidebar
3. You should see all your Django tables:
   - `auth_*` tables (for authentication)
   - `jobs_*` tables (for workshop jobs)
   - `inventory_*` tables (for radiator inventory)
   - `bookings_*` tables (for bookings)
   - `django_*` tables (Django system tables)

## Troubleshooting

### Connection Error: "password authentication failed"

- Double-check that you've replaced `[YOUR-PASSWORD]` in the connection string with your actual database password
- Make sure there are no extra spaces or special characters that need to be URL-encoded

### Connection Error: "could not connect to server"

- Verify your internet connection
- Check that your Supabase project is active (not paused)
- Ensure the connection string format is correct

### SSL Connection Error

If you encounter SSL-related errors, you can add SSL parameters to your connection string:
```
DATABASE_URL=postgresql://postgres:password@db.project.supabase.co:5432/postgres?sslmode=require
```

### Migration Errors

If migrations fail:
1. Make sure all dependencies are installed: `pip install -r requirements.txt`
2. Check that `psycopg2-binary` is installed (it should be in requirements.txt)
3. Try running migrations again: `python manage.py migrate`

## Production Deployment

For production deployments (e.g., on Render, Railway, or Heroku):

1. Set the `DATABASE_URL` environment variable in your hosting platform's settings
2. Use the same connection string format from Supabase
3. Make sure to set `DEBUG=False` and configure `ALLOWED_HOSTS` appropriately

## Security Notes

- **Never commit your `.env` file** to version control
- The `.env` file is already in `.gitignore` (or should be)
- Keep your database password secure
- Use different databases for development and production if possible

## Additional Resources

- [Supabase Documentation](https://supabase.com/docs)
- [Django Database Configuration](https://docs.djangoproject.com/en/stable/ref/settings/#databases)
- [PostgreSQL Connection Strings](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING)

