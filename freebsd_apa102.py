from freebsd_spi import spi_init, spi_write

# Variables
BRT = 224 + 16 # Brightness, 0~31 decimal

# Predefined data frames
START_FRAME = [0, 0, 0, 0]
END_FRAME = [255, 255, 255, 255]
BLUE_LED_FRAME = [BRT, 1, 0, 0]
GREEN_LED_FRAME = [BRT, 0, 1, 0]
RED_LED_FRAME = [BRT, 0, 0, 1]
YELLOW_LED_FRAME = [BRT, 0, 1, 1]


def led_send_start():
    spi_write(START_FRAME)


def led_send_end():
    spi_write(END_FRAME)


def led_send(status):
    if status in ["blue", "blue_anime"]:
        spi_write(GREEN_LED_FRAME)
    elif status in ["red", "red_anime"]:
        spi_write(RED_LED_FRAME)
    else:
        spi_write(YELLOW_LED_FRAME)


