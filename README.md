Boutique Ado Project Steps
1. Create new GitHub repo from template and launch GitPod workspace
2. Install Django with `pip3 install django`
3. Start Django Project with `django-admin startproject boutique_ado .`
4. Add *.sqlite3 and *.pyc to .gitignore
5. Test app install with `python3 manage.py runserver`
6. Run initial migrations with `python3 manage.py migrate`
7. Create superuser with `python3 manage.py createsuperuser`
8. Install Django AllAuth with `pip3 install django-allauth==0.41.0`
9. Update settings.py with the required settings for allauth from the documentation
10. Include `SITE_ID = 1` on settings.py
11. Include allauth urls in urls.py with `path('accounts/', include('allauth.urls'))`
12. Run migrations
13. Run the app, login as admin and update domain name and display name under Sites
14. Include the following in settings.py

    `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`

    `ACCOUNT_AUTHENTICATION_METHOD = 'username_email'`

    `ACCOUNT_EMAIL_REQUIRED = True`

    `ACCOUNT_EMAIL_VERIFICATION = 'mandatory'`

    `ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True`

    `ACCOUNT_USERNAME_MIN_LENGTH = 4`

    `LOGIN_URL = '/accounts/login/'`

    `LOGIN_REDIRECT_URL = '/'`

15. Freeze requirements `pip3 freeze > requirements.txt`
16. Create directory for templates > allauth
17. Copy allauth templates with `cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/`
18. Create a base template under templates
