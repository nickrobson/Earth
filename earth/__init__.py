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
    # 60 * 60 means 1 hour (this is in seconds)
    t = Timer(60 * 60, fetch_timer)
    t.start()


def bg_timer():
    set_random_background()
    # 60 * 5 means 5 minutes (this is in seconds)
    t = Timer(60 * 5, bg_timer)
    t.start()
