import time
import ast
import urllib

from freebsd_spi import spi_init
from freebsd_apa102 import led_send_start, led_send_end, led_send
from config import status

JENKINS_URL = "https://ci.freebsd.org/api/python"


if __name__ == "__main__":
    spi_init()
    while True:
        data = ast.literal_eval(urllib.urlopen(JENKINS_URL).read())["jobs"]
        led_send_start()
        for job in status:
            for item in data:
                if item["name"] == job["name"]:
                    led_send(item["color"])
                    break
                led_send("else")
        led_send_end()
        time.sleep(2)



