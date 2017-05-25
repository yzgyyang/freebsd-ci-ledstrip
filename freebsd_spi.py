import os
import time

from fbsd_gpio import GpioController

# Controller
gpioc = GpioController(0)

# Variables
SCLK = 2 # CI (Blue)
MOSI = 3 # DI (Green)
DELAY = 0.01 # Delay time (s)


def delay():
    # time.sleep(DELAY)
    pass


def spi_init():
    gpioc.pin_output(SCLK)
    gpioc.pin_output(MOSI)
    gpioc.pin_set(SCLK, 0)
    gpioc.pin_set(MOSI, 0)
    
    
def spi_write_byte(b):
    for i in xrange(8):
        gpioc.pin_set(SCLK, 0)
        gpioc.pin_set(MOSI, int(format(b, "08b")[i]))
        delay()
        gpioc.pin_set(SCLK, 1)


def spi_write(buf):
    for i in buf:
        spi_write_byte(i)

