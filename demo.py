import time
import datetime
import threading

from freebsd_spi import spi_init
from freebsd_apa102 import led_send_all
from config_demo import status

BLINK_INTERVAL = 0.5


def timestamp():
    return "[" + str(datetime.datetime.now()) + "] "


class Led_controller(threading.Thread):
    def run(self):
        blink_flag = False
        while True:
            blink_flag = not blink_flag
            led_send_all(status, blink_flag)
            time.sleep(BLINK_INTERVAL)


if __name__ == "__main__":
    spi_init()
    led_controller = Led_controller()
    led_controller.start()

    while True:
        time.sleep(20)
