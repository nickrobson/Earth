import earth
import tray
from threading import Timer

config = earth.config

def fetch_images(limit=20):
    earth.fetch_images(limit=limit)


def set_random_background():
    earth.set_random_background()


def run_tray():
    try:
        tray.run()
    except AttributeError:
        pass  # can't run as tray! :(


def fetch_timer(limit=20):
    fetch_images(limit=limit)
    t = Timer(config.get('fetch_images', 3600), fetch_timer, limit=limit)
    t.start()


def bg_timer():
    set_random_background()
    t = Timer(config.get('background_change', 300), bg_timer)
    t.start()
