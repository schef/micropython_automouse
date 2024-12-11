import usb_hid
from adafruit_hid.mouse import Mouse
import time

m = None

def init():
    global m
    usb_hid.enable((usb_hid.Device.MOUSE,))
    m = Mouse(usb_hid.devices)

def loop():
    while True:
        m.move(-1, 1, 0)
        time.sleep(0.1)
        m.move(-1, -1, 0)
        time.sleep(10)

def test():
    init()
    loop()
