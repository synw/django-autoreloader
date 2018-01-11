# Django Autoreloader

Autoreload files in browser for Django developement with Linux

## Requirement

Install and run [django-instant](https://github.com/synw/django-instant) for the websockets

## Install

   ```bash
   pip install django-autoreloader  
   ```
   
Add to settings:

   ```python
   INSTANT_SUPERUSER_CHANNELS = [
       ["$autoreload"]
   ]
   ```

Add `"autoreloader",` to installed apps.

Create a ``/templates/instant/handlers/$autoreload.js`` with this content:

   ```django
   {% include "autoreload/autoreload.js" %}
   ```

## Option

Add your watch list in settings.py:

  ```python
  # if not set the default is ["templates"]
  ARWL = ["static/js", "static/css", "templates"]
  
  # prevent paths from reloading: default is ["admin"]
  ARX = ["admin", "do/not/reload"]
  ```

## Run

Run the Django dev server and launch the watcher in another terminal:

   ```bash
   python3 manage.py autoreload
   ```
   
## Credits

- [Pyinotify](https://github.com/seb-m/pyinotify)
- [Django Instant](https://github.com/synw/django-instant)

