import os
import time

from fbsd_gpio import GpioController

# Controller
gpioc = GpioController(0)

# Variables
SCLK = 2 # CI (Blue)
MOSI = 3 # DI (Green)
DELAY = 0.01 # Delay time (s)


# Gpio value is one of [0, 1, "0", "1"]
def gpio_set_value(pin, value):
    gpioc.pin_set(int(pin), int(value))


# Direction is one of ["IN", "OUT"]
def gpio_set_direction(pin, direction):
    if direction == "OUT":
        gpioc.pin_output(int(pin))


def delay():
    # time.sleep(DELAY)
    pass


def spi_init():
    gpio_set_direction(SCLK, "OUT")
    gpio_set_direction(MOSI, "OUT")
    gpio_set_value(SCLK, 0)
    gpio_set_value(MOSI, 0)
    
    
def spi_write_byte(b):
    print "Writing: " + format(b, "08b")
    for i in xrange(8):
        gpio_set_value(SCLK, 0)
        gpio_set_value(MOSI, format(b, "08b")[i])
        delay()
        gpio_set_value(SCLK, 1)


def spi_write(buf):
    for i in buf:
        spi_write_byte(i)

