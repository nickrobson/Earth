#!/usr/bin/env python

import earth

try:
    import rumps


    class EarthApp(rumps.App):

        def __init__(self, name):
            super(EarthApp, self).__init__(name, icon=None)
            self.menu = ['Change Background', 'Fetch Images']

        @rumps.clicked('Change Background')
        def set_random_background(self, sender):
            earth.set_random_background()


        @rumps.clicked('Fetch Images')
        def fetch_images(self, sender):
            earth.fetch_images()


    def run():
        EarthApp('Earth').run()


    if __name__ == '__main__':
        run()

except ImportError, e:
    print e
    pass # I guess you're not on a Mac! >:(