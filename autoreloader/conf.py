from django.conf import settings


CHANNEL = getattr(settings, 'ARCHANNEL', 'reload')
try:
    arwl = getattr(settings, 'ARWL')
except:
    arwl = ["templates"]
WL = arwl

EXCLUDE = getattr(settings, 'ARX', ["admin"])
