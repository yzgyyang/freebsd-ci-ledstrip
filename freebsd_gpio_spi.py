import os
import time

# Variables
SCLK = 2 # CI (Blue)
MOSI = 3 # DI (Green)
DELAY = 0.01 # Delay time (s)


# Gpio value is one of [0, 1, "0", "1"]
def gpio_set_value(pin, value):
    os.system("gpioctl " + str(pin) + " " + str(value))


# Direction is one of ["IN", "OUT"]
def gpio_set_direction(pin, direction):
    os.system("gpioctl -c" + str(pin) + " " + direction)


def delay():
    time.sleep(0.01)


def spi_init():
    gpio_set_direction(SCLK, "OUT")
    gpio_set_direction(MOSI, "OUT")
    gpio_set_value(SCLK, 0)
    gpio_set_value(MOSI, 0)
    
    
def spi_write_byte(b):
    for i in xrange(8):
        gpio_set_value(SCLK, 0)
        gpio_set_value(MOSI, format(b, "08b")[i])
        delay()
        gpio_set_value(SCLK, 1)
        delay()


def spi_write(buf):
    for i in buf:
        spi_write_byte(i)
    delay()

