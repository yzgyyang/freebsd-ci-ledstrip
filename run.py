import time
import datetime
import ast
import urllib
import threading

from freebsd_spi import spi_init
from freebsd_apa102 import led_send_start, led_send_end, led_send, led_send_all
from config import status

JENKINS_URL = "https://ci.freebsd.org/api/python"


def timestamp():
    return "[" + str(datetime.datetime.now) + "] "


class Led_controller(threading.Thread):
    def run(self):
        blink_flag = False
        while True:
            blink_flag = not blink_flag
            led_send_start()
            led_send_all(status, blink_flag)
            led_send_end()
            time.sleep(0.5)


if __name__ == "__main__":
    spi_init()
    led_controller = Led_controller()
    led_controller.start()

    while True:
        data = ast.literal_eval(urllib.urlopen(JENKINS_URL).read())["jobs"]
        for job in status:
            isfound = False
            for item in data:
                if item["name"] == job["name"]:
                    isfound = True
                    if job["status"] != item["color"]:
                        print timestamp() + job["name"] + " changed to status: " + item["color"]
                        job["status"] = item["color"]
                    break
            if job["status"] != "dne" and not isfound:
                print timestamp() + job["name"] + " does not exist"
                job["status"] = "dne"
        print timestamp() + "Status updated successfully."
        time.sleep(20)


