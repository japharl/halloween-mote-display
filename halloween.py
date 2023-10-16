#!/usr/bin/env python

import time

from mote import Mote

from random import randrange,uniform


rgb = (128,128, 128)

mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

while True:
    r = 128
    g = 128
    b = 128
    mote.set_all(r, g, b)
    mote.show()
    time.sleep(uniform(.05,.3))  # display white led for 0.05 to .3 seconds
    r = 0
    g = 0
    b = 0
    mote.set_all(r, g, b)
    mote.show()
    time.sleep(uniform(0,10) # sleep for 0 .. 10 seconds
