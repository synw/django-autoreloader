# Django Autoreloader

Autoreload files in browser for Django developement with Linux

## Install

   ```bash
   pip install django-autoreloader  
   ```

Add `"autoreloader",` to installed apps.

Add your watch list in settings.py:

  ```python
  # if not set the default is ["templates"]
  ARWL = ["static/js", "static/css", "templates"]
  
  # prevent paths from reloading: default is ["admin"]
  ARX = ["admin", "do/not/reload"]
  ```
  
Include the client in a template:

   ```django
   <script type="text/javascript">
      {% include "autoreloader/client.js" %}
   </script>
   ```

## Run

Run the Django dev server and launch the watcher in another terminal:

   ```bash
   python3 manage.py autoreload
   ```
   
## Credits

- [Python Websockets Server](https://github.com/Pithikos/python-websocket-server)
- [Pyinotify](https://github.com/seb-m/pyinotify)