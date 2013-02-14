#!/usr/bin/env python
import sys
import gtk
import appindicator
import time

PING_FREQUENCY = 1 # seconds

class Clock:
    def __init__(self):
        self.ind = appindicator.Indicator("new-swatch-indicator",
                                           "~/bin/at.svg",
                            appindicator.CATEGORY_APPLICATION_STATUS)

        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon("new-messages-red")
        self.menu_setup()
        self.ind.set_menu(self.menu)

    def menu_setup(self):
        self.menu = gtk.Menu()

        self.quit_item = gtk.MenuItem("Quit")
        self.quit_item.connect("activate", self.quit)
        self.quit_item.show()
        self.menu.append(self.quit_item)

    def main(self):
        gtk.timeout_add(PING_FREQUENCY * 1000, self.check_time)
        gtk.main()

    def check_time(self):
        now = time.gmtime()
        hour = now.tm_hour
        mn = now.tm_min
        sec = now.tm_sec
        update = "%d" % (((sec + (60 * mn) + ((hour + 1) * 3600)) / 86.4) % 1000)
        self.ind.set_label(update)
        gtk.timeout_add(PING_FREQUENCY * 1000, self.check_time)

    def quit(self, widget):
        sys.exit(0)

if __name__ == "__main__":
    indicator = Clock()
    indicator.main()
