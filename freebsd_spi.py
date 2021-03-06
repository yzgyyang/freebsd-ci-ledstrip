import os
import time

from fbsd_gpio import GpioController

# Controller
gpioc = GpioController(0)

# Variables
SCLK = 2  # CI (Blue)
MOSI = 3  # DI (Green)


def spi_init():
    gpioc.pin_output(SCLK)
    gpioc.pin_output(MOSI)
    gpioc.pin_set(SCLK, 0)
    gpioc.pin_set(MOSI, 0)


def spi_write_byte(b):
    for i in xrange(7, -1, -1):
        gpioc.pin_set(SCLK, 0)
        gpioc.pin_set(MOSI, (b >> i) & 1)
        gpioc.pin_set(SCLK, 1)


def spi_write(buf):
    for i in buf:
        spi_write_byte(i)
