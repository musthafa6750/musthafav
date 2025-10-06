# Deployment Instructions for Hosting Django Website on Render.com

This document provides step-by-step instructions to deploy your Django website on Render.com free tier.

## Prerequisites

- A Render.com account (sign up at https://render.com)
- Git installed on your local machine
- Your Django project pushed to a GitHub repository

## Steps to Deploy

1. **Push your code to GitHub**

   Make sure your Django project is committed and pushed to a GitHub repository.

2. **Create a new Web Service on Render**

   - Log in to Render.com
   - Click on "New" > "Web Service"
   - Connect your GitHub account and select your Django repository
   - Choose the branch to deploy (e.g., main or master)
   - Set the environment to "Python 3"
   - Set the build command to:
     ```
     pip install -r requirements.txt
     python manage.py collectstatic --noinput
     python manage.py migrate
     ```
   - Set the start command to:
     ```
     gunicorn --bind 0.0.0.0:$PORT mywebsite.wsgi:application
     ```
   - Set environment variables:
     - `SECRET_KEY`: Your Django secret key (generate a new one for production)
     - `DEBUG`: False
     - `ALLOWED_HOSTS`: Your Render service URL (e.g., yourapp.onrender.com)

3. **Database**

   - For the free tier, SQLite is used, but data may not persist across deploys.
   - For persistent data, upgrade to a paid plan or use a managed PostgreSQL database.

4. **Deploy**

   - Click "Create Web Service"
   - Render will build and deploy your app automatically.
   - Once deployed, your website will be available at the provided URL.

## Alternative: GitHub Pages (for Static Sites)

If your website is mostly static and doesn't require dynamic features like the contact form, you can host it on GitHub Pages for free.

- Convert your Django templates to static HTML using tools like Django's `collectstatic` or static site generators.
- Push the static files to a GitHub repository.
- Enable GitHub Pages in the repository settings.

Note: This won't work for dynamic content like forms saving to a database.

## Testing

After deployment, test your website to ensure all features work correctly, especially the contact form and any dynamic content.
