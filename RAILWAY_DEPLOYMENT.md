# Railway Deployment Guide

This guide will help you deploy your Django Stock Management System to Railway.

## Prerequisites

1. A Railway account ([railway.app](https://railway.app))
2. Your project code in a Git repository (GitHub, GitLab, or Bitbucket)
3. Basic understanding of Git commands

## Step 1: Prepare Your Project

All necessary configuration files have been created:
- ✅ `Procfile` - Tells Railway how to run your app
- ✅ `requirements.txt` - Updated with production dependencies
- ✅ `runtime.txt` - Specifies Python version
- ✅ `.gitignore` - Excludes sensitive files
- ✅ `settings.py` - Updated for production with environment variables

## Step 2: Generate a New Secret Key

For production, you should generate a new secret key. Run this in your terminal:

```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the generated key - you'll need it in Step 5.

## Step 3: Commit and Push to Git

Make sure all changes are committed and pushed to your Git repository:

```bash
git add .
git commit -m "Prepare for Railway deployment"
git push
```

## Step 4: Deploy to Railway

### Option A: Using Railway Dashboard (Recommended)

1. Go to [railway.app](https://railway.app) and sign up/login
2. Click "New Project"
3. Select "Deploy from GitHub repo" (or GitLab/Bitbucket)
4. Connect your repository and select your project
5. Railway will automatically detect it's a Python/Django project

### Option B: Using Railway CLI

1. Install Railway CLI:
   ```bash
   npm install -g @railway/cli
   ```

2. Login to Railway:
   ```bash
   railway login
   ```

3. Initialize your project:
   ```bash
   railway init
   ```

4. Deploy:
   ```bash
   railway up
   ```

## Step 5: Configure Environment Variables

In your Railway project dashboard:

1. Go to your project → "Variables" tab
2. Add the following environment variables:

   ```
   SECRET_KEY=your-generated-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=your-app-name.railway.app,*.railway.app
   ```

   **Important Notes:**
   - Replace `your-generated-secret-key-here` with the key you generated in Step 2
   - Replace `your-app-name.railway.app` with your actual Railway domain (Railway will show you this)
   - You can also add `*.railway.app` to allow any Railway subdomain

## Step 6: Add PostgreSQL Database

1. In your Railway project dashboard, click "New" → "Database" → "Add PostgreSQL"
2. Railway will automatically create the database and set the `DATABASE_URL` environment variable
3. Your app will automatically use this database - no additional configuration needed!

## Step 7: Run Migrations

After deployment, you need to run database migrations. You can do this in two ways:

### Option A: Using Railway Dashboard
1. Go to your service
2. Click on "Deployments"
3. Click on the latest deployment
4. Open the "Shell" tab
5. Run: `python manage.py migrate`
6. Create a superuser (optional): `python manage.py createsuperuser`

### Option B: Using Railway CLI
```bash
railway run python manage.py migrate
railway run python manage.py createsuperuser
```

## Step 8: Collect Static Files

Railway will automatically run `collectstatic` during deployment, but if you need to run it manually:

```bash
railway run python manage.py collectstatic --noinput
```

## Step 9: Access Your Application

1. Railway will provide you with a URL like: `https://your-app-name.railway.app`
2. Visit this URL to see your deployed application
3. You may need to wait a few minutes for the first deployment to complete

## Step 10: Set Up Custom Domain (Optional)

1. In Railway dashboard → Your project → Settings → Domains
2. Click "Generate Domain" or "Add Custom Domain"
3. For custom domains, follow Railway's DNS configuration instructions

## Troubleshooting

### Application not loading?
- Check the "Logs" tab in Railway dashboard for errors
- Verify all environment variables are set correctly
- Make sure `ALLOWED_HOSTS` includes your Railway domain

### Database errors?
- Ensure PostgreSQL database is added and running
- Check that `DATABASE_URL` is set automatically by Railway
- Try running migrations again: `railway run python manage.py migrate`

### Static files not loading?
- Make sure WhiteNoise is in your middleware (already configured)
- Check that `STATIC_ROOT` is set in settings.py (already configured)
- Static files should be collected automatically during deployment

### Can't create superuser?
- Use Railway CLI: `railway run python manage.py createsuperuser`
- Or use the Shell in Railway dashboard

## Post-Deployment Checklist

- ✅ Application is accessible via Railway URL
- ✅ Database migrations are run
- ✅ Superuser account is created
- ✅ Static files are loading correctly
- ✅ All environment variables are set
- ✅ DEBUG is set to False
- ✅ SECRET_KEY is changed from default

## Monitoring and Updates

- **View Logs**: Railway dashboard → Your service → Logs
- **Redeploy**: Push new commits to your Git repository - Railway will auto-deploy
- **Environment Variables**: Update in Railway dashboard → Variables
- **Scale**: Adjust resources in Railway dashboard → Settings

## Cost Notes

- Railway offers a free tier with $5 credit per month
- PostgreSQL database usage counts toward your usage
- Check Railway pricing for details on limits

## Need Help?

- Railway Documentation: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- Django Deployment Checklist: https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

---

**Congratulations! Your Django application should now be live on Railway! 🚀**

