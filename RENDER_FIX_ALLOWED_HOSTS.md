# Quick Fix: ALLOWED_HOSTS Error on Render

## Error Message
```
Invalid HTTP_HOST header: 'workshop-management-system-elb4.onrender.com'. 
You may need to add 'workshop-management-system-elb4.onrender.com' to ALLOWED_HOSTS.
```

## Quick Fix (2 minutes)

### Step 1: Go to Render Dashboard
1. Login to [render.com](https://render.com)
2. Click on your web service: `workshop-management-system`

### Step 2: Update Environment Variable
1. Click on **"Environment"** tab
2. Find the `ALLOWED_HOSTS` variable (or add it if it doesn't exist)
3. Change the value to:

**Add your exact domain:**
```
ALLOWED_HOSTS=workshop-management-system-elb4.onrender.com
```

**Note:** Django doesn't support wildcards in ALLOWED_HOSTS. You must use the exact domain name.

### Step 3: Save and Wait
1. Click **"Save Changes"**
2. Render will automatically redeploy (or trigger manual deploy)
3. Wait 2-3 minutes for redeployment
4. Refresh your app URL - it should work! ✅

## Why This Happened

Your `ALLOWED_HOSTS` environment variable either:
- Wasn't set
- Was set to a different domain
- Was set incorrectly

Django requires the exact domain (or pattern) in `ALLOWED_HOSTS` for security reasons.

## Verify It's Fixed

After redeployment, you should see:
- ✅ No more "Invalid HTTP_HOST header" errors in logs
- ✅ Your app loads normally at your Render URL
- ✅ No 400 Bad Request errors

## If You Add Custom Domains Later

If you add a custom domain in Render, update `ALLOWED_HOSTS` to include both:
```
ALLOWED_HOSTS=workshop-management-system-elb4.onrender.com,your-custom-domain.com
```

You can add multiple domains separated by commas.

Your settings.py already handles this correctly - it just needs the right value in the environment variable!

