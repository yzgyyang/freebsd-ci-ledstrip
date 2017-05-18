from freebsd_gpio_spi import spi_write

# Variables
BRT = 16 # Brightness, 0~31 decimal

# Predefined data frames
START_FRAME = [0, 0, 0, 0]
END_FRAME = [1, 1, 1, 1]
RED_LED_FRAME = [BRT, 1, 0, 0]
GREEN_LED_FRAME = [BRT, 0, 1, 0]
BLUE_LED_FRAME = [BRT, 0, 0, 1]


def light(ch):
    spi_write(START_FRAME)
    if ch == 'r':
        spi_write(RED_LED_FRAME)
        spi_write(GREEN_LED_FRAME)
        spi_write(BLUE_LED_FRAME)
    spi_write(END_FRAME)

