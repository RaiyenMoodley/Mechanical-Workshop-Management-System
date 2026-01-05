# Render Quick Start - At a Glance

## Your Project is Already Ready! ✅

Your Django project is configured to work with Render out of the box:
- ✅ Environment variables configured (`python-decouple`)
- ✅ PostgreSQL support (`DATABASE_URL` configured)
- ✅ Static files configured (WhiteNoise)
- ✅ All dependencies in `requirements.txt`

## Quick Deployment Steps

### 1. Push to GitHub
```bash
git add .
git commit -m "Ready for Render"
git push
```

### 2. Create Render Account & Service
1. Go to [render.com](https://render.com) → Sign up with GitHub
2. Click "New +" → "Web Service"
3. Connect your repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn workshop_manager.wsgi:application`

### 3. Add Environment Variables
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app.onrender.com
```

### 4. Add PostgreSQL Database
- Click "New +" → "PostgreSQL"
- Select "Free" tier
- Render automatically links it (sets `DATABASE_URL`)

### 5. Deploy & Migrate
- Click "Create Web Service"
- Wait for deployment
- Use "Shell" tab to run: `python manage.py migrate`
- Create superuser: `python manage.py createsuperuser`

## Key Differences: Render vs Railway

| Aspect | Render | Railway |
|--------|--------|---------|
| **Free Tier** | 750 hours/month | $5 credit/month |
| **PostgreSQL** | Free (512 MB) | Free (1 GB) |
| **Sleep Mode** | Yes (15 min inactivity) | No |
| **Build Config** | Dashboard or `build.sh` | Procfile or auto-detect |
| **Start Command** | Dashboard or Procfile | Procfile |
| **Auto-Deploy** | ✅ Yes | ✅ Yes |
| **CLI Required** | ❌ No (optional) | ✅ Recommended |

## Important Notes

1. **Sleep Mode (Free Tier)**: Render services sleep after 15 min of inactivity. First request after sleep takes ~30 seconds to wake up.

2. **Build Command**: Render needs to collect static files:
   ```
   pip install -r requirements.txt && python manage.py collectstatic --noinput
   ```

3. **Start Command**: Render needs Gunicorn:
   ```
   gunicorn workshop_manager.wsgi:application
   ```

4. **DATABASE_URL**: Automatically set when you add PostgreSQL - your settings.py already handles this!

5. **Procfile**: You have one, but Render typically uses dashboard settings. Having both is fine!

## Need More Details?

See the full guide: `RENDER_DEPLOYMENT.md`

