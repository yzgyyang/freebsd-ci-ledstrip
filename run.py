import time
import ast
import urllib

from freebsd_spi import spi_init
from freebsd_apa102 import led_send_start, led_send_end, led_send
from config import status

JENKINS_URL = "https://ci.freebsd.org/api/python"


if __name__ == "__main__":
    spi_init()
    blink_flag = False
    while True:
        data = ast.literal_eval(urllib.urlopen(JENKINS_URL).read())["jobs"]
        led_send_start()
        for job in status:
            isfound = False
            for item in data:
                if item["name"] == job["name"]:
                    if job["status"] != item["color"]:
                        isfound = True
                        print job["name"] + " changed to status: " + item["color"]
                        job["status"] = item["color"]
                    break
            if job["status"] != "dne" and not isfound:
                print job["name"] + " does not exist"
                job["status"] = "dne"
        blink_flag = not blink_flag
        led_send_start()
        led_send_end()
        time.sleep(1)



