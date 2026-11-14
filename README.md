# SocialConnect – Social Media Platform

A Django social networking project with registration, profiles, image/text posts, likes, comments, and follow/unfollow.

## Features
- User registration, login and logout
- Auto-created profiles with bio and avatar
- Create text and image posts
- Like/unlike posts (one like per user per post)
- Add comments and delete your own comments
- Follow/unfollow users
- View profile posts, follower and following lists
- Django admin

## Run on Windows (VS Code PowerShell)

```powershell
py -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe manage.py makemigrations social
.\venv\Scripts\python.exe manage.py migrate
.\venv\Scripts\python.exe manage.py createsuperuser
.\venv\Scripts\python.exe manage.py runserver
```

Open http://127.0.0.1:8000/ and register an account. Admin: http://127.0.0.1:8000/admin/

## Before deployment
This starter uses SQLite and local media storage for development. For public deployment, configure PostgreSQL and persistent media/object storage, set a private `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`, HTTPS/CSRF settings, and production static/media hosting. Test all flows against your internship rubric before submission.
