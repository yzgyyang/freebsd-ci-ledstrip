from freebsd_gpio_spi import spi_write

# Variables
BRT = 16 # Brightness, 0~31 decimal

# Predefined data frames
START_FRAME = [0, 0, 0, 0]
END_FRAME = [255, 255, 255, 255]
RED_LED_FRAME = [BRT + 224, 1, 0, 0]
GREEN_LED_FRAME = [BRT + 224, 0, 1, 0]
BLUE_LED_FRAME = [BRT + 224, 0, 0, 1]


def light(ch):
    spi_write(START_FRAME)
    if ch == 'r':
        spi_write(RED_LED_FRAME)
    elif ch == 'g':
        spi_write(GREEN_LED_FRAME)
    elif ch == 'b':
        spi_write(BLUE_LED_FRAME)
    spi_write(END_FRAME)

