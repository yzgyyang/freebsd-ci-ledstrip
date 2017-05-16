import freebsd-gpio

# Variables
SS
SCLK
MOSI
MISO

def delay():
    pass


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

