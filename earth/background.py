plat = 'Unknown'

try:
    import ctypes.windll as windll
    plat = 'Windows'
except ImportError:
    try:
        from appscript import *
        plat = 'Mac OS X'
    except ImportError:
        try:
            import gconf
            plat = 'gconf'
        except ImportError:
            print 'Unknown platform'


def set_background_image(image):
    if plat == 'Windows':
        windll.user32.SystemParametersInfoW(0x14, 0, image, 0x2)
    elif plat == 'Mac OS X':
        app('System Events').desktops.picture.set(image)
    elif plat == 'gconf':
        conf = gconf.client_get_default()
        conf.set_string('/desktop/gnome/background/picture_filename', image)
    else:
        print 'Unknown platform'
