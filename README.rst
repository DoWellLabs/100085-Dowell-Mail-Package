=====================
DOWELL MAIL APP
=====================

This is a django mail package consuming the Dowell Mail API. It validates each email then sends email once validated.

QUICK START
====================

1. Add `maillib` to your INSTALLED_APPS in settings.py like this:

    INSTALLED_APPS = [
        ...
        'maillib',
    ]

2. Add `import os` then edit TEMPLATES to include `os.path.join(BASE_DIR, 'templates')` in DIRS like:
    "DIRS" : [
        os.path.join(BASE_DIR, 'templates')
    ]

3. Include maillib URLconf in the projects url.py like this:
    path('mail', include('maillib.urls')),

4. The package doesnt have any database so no migrations are necessary

5. Start the server and navigate to `http://127.0.0.1:8000/mail` and start sending emails!