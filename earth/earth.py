import background
import os
import sys
import praw
import random
import requests
import time

try:
    import simplejson as json
except:
    import json

earthdir = os.path.expanduser('~/.earth')
filesdir = earthdir + '/source'
imagedir = earthdir + '/images'

cfg = os.path.join(filesdir, 'config.json')
config = dict()
if os.path.isfile(cfg):
    with open(cfg, 'r') as f:
        config = json.loads(f.read())

if not os.path.isdir(imagedir):
    os.mkdir(imagedir)

ua = '%s:%s:%s (by /u/fusion_games)' % (sys.platform, 'Earth', '1.0.0')
reddit = praw.Reddit(user_agent=ua)


def get_file_name(name, ext):
    fname = '%s.%s' % (name, ext)
    fname = fname.replace('/', '|')
    return fname


def get_file_path(name, ext):
    return os.path.join(imagedir, get_file_name(name, ext))


def get_hot_submissions(limit=20):
    try:
        return list(reddit.get_subreddit('earthporn').get_hot(limit=limit))
    except requests.exceptions.ConnectionError:
        print "It looks like you're not connected to the internet!"
        return []


def get_image_urls(limit=20):
    return map(lambda s: (s.title, s.url), get_hot_submissions(limit=limit))


def get_ext(mime):
    return {'image/jpeg': 'jpg', 'image/png': 'png'}.get(mime, 'N/A')


def fetch_image(name, url):
    res = requests.get(url, stream=True)
    ext = get_ext(res.headers['Content-Type'])
    clen = res.headers.get('Content-Length', 0)
    if long(clen) > long(config.get('max_file_size', 32 * 10 ** 7)):  # 32 MB
        print 'Skipped', name, '(' + str(res.headers['Content-Length']) + ')'
        return
    if ext == 'N/A':
        return
    fname = get_file_path(name, ext)
    if len(fname) > 30:
        fname = fname[0:30]
    if os.path.isfile(fname):
        return
    with open(fname, 'wb+') as f:
        for chunk in res.iter_content(1024):
            f.write(chunk)


def fetch_images(limit=20):
    files = os.listdir(imagedir)
    files = filter(lambda f: f.endswith('.jpg') or f.endswith('.png'), files)
    files = map(lambda f: os.path.join(imagedir, f), files)
    keep_time = config.get('keep_file_time', 60 * 60 * 24 * 2)

    # Delete old files after 2 days.
    def delta(f):
        return os.path.getmtime(f) < int(time.time()) - keep_time

    files = filter(delta, files)
    for f in files:
        os.remove(f)

    for name, url in get_image_urls(limit=limit):
        fetch_image(name, url)


def set_random_background():
    files = os.listdir(imagedir)
    files = filter(lambda f: f.endswith('.jpg') or f.endswith('.png'), files)
    if len(files) > 0:
        file = files[random.randint(0, len(files) - 1)]
        background.set_background_image(os.path.join(imagedir, file))
