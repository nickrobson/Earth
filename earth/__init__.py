import earth
import tray
from threading import Timer


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
    t = Timer(earth.config.get('fetch_images', 3600), fetch_timer)
    t.start()


def bg_timer():
    set_random_background()
    t = Timer(earth.config.get('background_change', 300), bg_timer)
    t.start()
