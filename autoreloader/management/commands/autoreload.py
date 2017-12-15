# -*- coding: utf-8 -*-

from __future__ import print_function
import time
import pyinotify
from django.core.management.base import BaseCommand
from django.utils._os import safe_join
from django.conf import settings
from instant.producers import publish
from autoreloader.conf import WL

wm = pyinotify.WatchManager()
mask = pyinotify.IN_MODIFY | pyinotify.IN_CREATE


class EventHandler(pyinotify.ProcessEvent):

    def process_IN_CREATE(self, event):
        print("Creating", event.pathname)

    def process_IN_MODIFY(self, event):
        print("Change in", event.pathname)
        publish("reload", event_class="reload", channel="$autoreload")


def new_client(client, server):
    pass


class Command(BaseCommand):
    help = 'Start autoreloader daemon'

    def handle(self, *args, **options):
        if settings.DEBUG is False:
            print("This command can only run with DEBUG = True in settings")
            return
        print("Watching file changes in:")
        #excl = pyinotify.ExcludeFilter(EXCLUDE)
        for d in WL:
            print("/" + d)
            path = safe_join(settings.BASE_DIR, d)
            #wm.add_watch(path, mask, rec=True, exclude_filter=excl)
            wm.add_watch(path, mask, rec=True)
        # run watcher
        notifier = pyinotify.ThreadedNotifier(wm, EventHandler())
        notifier.start()

        while True:
            try:
                time.sleep(5)
            except KeyboardInterrupt:
                notifier.stop()
                return
            except:
                notifier.stop()
                return
