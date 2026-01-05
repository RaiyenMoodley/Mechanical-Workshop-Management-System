# Render Deployment Guide

This guide will help you deploy your Django Stock Management System to Render.

## Why Render?

- ✅ Free tier with PostgreSQL included
- ✅ Easy GitHub integration with auto-deploy
- ✅ Automatic SSL certificates
- ✅ Simple environment variable management
- ✅ Built-in static file serving

## Prerequisites

1. A Render account ([render.com](https://render.com))
2. Your project code in a GitHub repository
3. Basic understanding of Git

## Step 1: Prepare Your Project

Your project is already configured for deployment! The following files are ready:
- ✅ `requirements.txt` - Production dependencies
- ✅ `settings.py` - Configured for environment variables
- ✅ `.gitignore` - Excludes sensitive files
- ✅ WhiteNoise configured for static files

## Step 2: Generate a New Secret Key

For production, generate a new secret key. Run this in your terminal:

```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the generated key - you'll need it in Step 5.

## Step 3: Commit and Push to GitHub

Make sure all changes are committed and pushed to your GitHub repository:

```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

## Step 4: Create a Render Account and Project

1. Go to [render.com](https://render.com) and sign up/login (GitHub OAuth is easiest)
2. Click "New +" in the dashboard
3. Select "Web Service"
4. Connect your GitHub account if you haven't already
5. Select your repository: `Stock-Management-System`
6. Click "Connect"

## Step 5: Configure Your Web Service

Render will auto-detect Django, but verify/configure these settings:

### Basic Settings:
- **Name**: `workshop-manager` (or any name you prefer)
- **Region**: Choose closest to your users (e.g., `Oregon (US West)`)
- **Branch**: `main` (or your default branch)
- **Root Directory**: Leave empty (or `Stock-Management-System` if your repo has multiple projects)
- **Runtime**: `Python 3`
- **Build Command**: 
  ```bash
  pip install -r requirements.txt && python manage.py collectstatic --noinput
  ```
- **Start Command**: 
  ```bash
  gunicorn workshop_manager.wsgi:application
  ```

### Advanced Settings (Click "Advanced"):
- **Instance Type**: `Free` (for starters, upgrade later if needed)
- **Auto-Deploy**: `Yes` (automatically deploys on git push)

## Step 6: Add Environment Variables

In the Render dashboard, scroll down to "Environment Variables" and add:

```
SECRET_KEY=your-generated-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
PYTHON_VERSION=3.11.9
```

**Important Notes:**
- Replace `your-generated-secret-key-here` with the key from Step 2
- Replace `your-app-name.onrender.com` with your actual Render domain (you'll see this after first deployment)
- You can also add `*.onrender.com` to ALLOWED_HOSTS to allow any Render subdomain

## Step 7: Add PostgreSQL Database

1. In your Render dashboard, click "New +" → "PostgreSQL"
2. Configure:
   - **Name**: `workshop-manager-db` (or any name)
   - **Database**: `workshop_manager` (or leave default)
   - **User**: Leave default (auto-generated)
   - **Region**: Same as your web service
   - **Plan**: `Free` (512 MB storage)
   - **PostgreSQL Version**: Latest (14 or 15)
3. Click "Create Database"
4. Render automatically creates a `DATABASE_URL` environment variable

## Step 8: Link Database to Web Service

1. Go back to your Web Service dashboard
2. Go to "Environment" tab
3. Under "Environment Variables", you should see `DATABASE_URL` automatically added
4. If not, you can manually add it:
   - Go to your PostgreSQL service
   - Copy the "Internal Database URL" or "External Database URL"
   - Add it as `DATABASE_URL` in your web service environment variables

**Note:** Your `settings.py` is already configured to use `DATABASE_URL` automatically!

## Step 9: Deploy and Run Migrations

1. Click "Create Web Service" or "Save Changes"
2. Render will start building and deploying your application
3. Watch the build logs - this will take a few minutes
4. Once deployment completes, you'll see your app URL (e.g., `https://your-app-name.onrender.com`)

### Run Migrations:

**Option A: Using Render Shell (Recommended)**
1. In your Web Service dashboard, click "Shell" tab
2. Run:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
3. Follow prompts to create admin account

**Option B: Using Render CLI**
1. Install Render CLI (optional):
   ```bash
   npm install -g render-cli
   ```
2. Login:
   ```bash
   render login
   ```
3. Run migrations:
   ```bash
   render exec -s your-service-name -- python manage.py migrate
   render exec -s your-service-name -- python manage.py createsuperuser
   ```

## Step 10: Access Your Application

1. Your app URL will be: `https://your-app-name.onrender.com`
2. Visit the URL to see your deployed application
3. Login with the superuser credentials you created

## Step 11: Set Up Custom Domain (Optional)

1. In your Web Service dashboard → Settings → Custom Domains
2. Click "Add Custom Domain"
3. Enter your domain name
4. Follow Render's DNS configuration instructions
5. Update `ALLOWED_HOSTS` environment variable to include your custom domain

## Troubleshooting

### Build Fails?
- Check build logs in Render dashboard
- Verify `requirements.txt` is correct
- Make sure Python version matches (check `PYTHON_VERSION` environment variable)

### Application Not Loading?
- Check "Logs" tab for errors
- Verify all environment variables are set
- Make sure `ALLOWED_HOSTS` includes your Render domain
- Check that database migrations have run

### Database Connection Errors?
- Verify PostgreSQL is running (green status in dashboard)
- Check `DATABASE_URL` is set in environment variables
- Ensure migrations have run: `python manage.py migrate`

### Static Files Not Loading?
- WhiteNoise is already configured in your settings
- Static files are collected during build (`collectstatic` in build command)
- Check build logs to ensure `collectstatic` ran successfully
- Verify `STATIC_ROOT` is set correctly (already configured)

### 502 Bad Gateway?
- Check application logs
- Verify your start command is correct: `gunicorn workshop_manager.wsgi:application`
- Make sure all environment variables are set
- Check that the app is listening on the correct port (Render sets `$PORT` automatically)

### Can't Create Superuser?
- Use Render Shell: Web Service → Shell tab
- Run: `python manage.py createsuperuser`
- Follow the prompts

## Post-Deployment Checklist

- ✅ Application is accessible via Render URL
- ✅ Database migrations are run
- ✅ Superuser account is created
- ✅ Static files are loading correctly
- ✅ All environment variables are set
- ✅ DEBUG is set to False
- ✅ SECRET_KEY is changed from default
- ✅ PostgreSQL database is connected

## Monitoring and Updates

- **View Logs**: Render dashboard → Your service → Logs
- **Redeploy**: Push new commits to GitHub - Render will auto-deploy (if enabled)
- **Manual Deploy**: Dashboard → Manual Deploy → Deploy latest commit
- **Environment Variables**: Dashboard → Environment tab
- **Scale**: Dashboard → Settings → Scale (upgrade plan for more resources)

## Render vs Railway - Key Differences

| Feature | Render | Railway |
|---------|--------|---------|
| Free Tier | Yes, with PostgreSQL | Yes, $5/month credit |
| PostgreSQL | Free tier included | Free tier included |
| Auto-Deploy | Yes, from GitHub | Yes, from GitHub |
| Build Command | Configurable in dashboard | Uses Procfile or auto-detects |
| Start Command | Configurable in dashboard | Uses Procfile |
| Static Files | WhiteNoise or native | WhiteNoise recommended |
| CLI | Optional | Recommended for migrations |

## Cost Notes

- **Free Tier**: 
  - 750 hours/month of web service runtime
  - 512 MB PostgreSQL database
  - Automatic SSL
  - Unlimited bandwidth
- **Paid Plans**: Start at $7/month for more resources
- Free tier services "spin down" after 15 minutes of inactivity (takes ~30 seconds to wake up)

## Sleep Mode (Free Tier)

Render's free tier services automatically sleep after 15 minutes of inactivity. When someone visits:
- The service wakes up automatically (~30 seconds)
- First request may be slow
- Subsequent requests are fast

To avoid sleep mode, you can:
- Upgrade to a paid plan ($7/month)
- Use a service like UptimeRobot to ping your site every 10 minutes (free)

## Need Help?

- Render Documentation: https://render.com/docs
- Render Community: https://community.render.com
- Django Deployment Checklist: https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

---

**Congratulations! Your Django application should now be live on Render! 🚀**

