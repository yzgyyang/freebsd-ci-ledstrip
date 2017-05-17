import time

import freebsd-gpio

# Variables
SS
SCLK =  # CI (Blue)
MOSI =  # DI (Green)
MISO

def delay():
    time.sleep(0.01)


def spi_init():
    set_gpio_direction(SS, "OUT")
    set_gpio_direction(SCLK, "OUT")
    set_gpio_direction(MOSI, "OUT")
    set_gpio_direction(MISO, "IN")
    set_gpio_value(SCLK, 0)
    set_gpio_value(MOSI, 0)
    
    
def ss_enable(flag):
    if flag:
        set_gpio_value(SS, 0)
    else:
        set_gpio_value(SS, 1)


def spi_write_byte(b):
    for i in reversed(xrange(8)):
        set_gpio_value(SCLK, 0)
        set_gpio_value(MOSI, b & (1 << i))
        delay()
        set_gpio_value(SCLK, 1)
        delay()


def spi_write(buf):
    spi_init()
    ss_enable(True)
    delay()
    for i in buf:
        spi_write_byte(i)
    delay()
    ss_enable(False)


def led_on():
    spi_write_byte(0b00000000)
    spi_write_byte(0b00000000)
    spi_write_byte(0b00000000)
    spi_write_byte(0b00000000)

    spi_write_byte(0b11111111)
    spi_write_byte(0b11111111)
    spi_write_byte(0b11111111)
    spi_write_byte(0b11111111)

    spi_write_byte(0b11111111)
    spi_write_byte(0b11111111)
    spi_write_byte(0b11111111)
    spi_write_byte(0b11111111)
    
    spi_write_byte(0b11111111)
    spi_write_byte(0b11111111)
    spi_write_byte(0b11111111)
    spi_write_byte(0b11111111)

if __name__ == "__main__":
    led_on()
