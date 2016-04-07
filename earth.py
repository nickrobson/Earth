#!/usr/bin/env python

import earth

def toInt(string, default):
    try:
        return int(string)
    except Exception:
        return default

fetch_limit = toInt(earth.config.get('fetch_limit', ''), 20)
earth.fetch_timer(fetch_limit)
earth.bg_timer()
earth.run_tray()
