__author__ = 'vovacooper'

import requests

from classes.logger import logger
from classes.config import *


class GeoIpProvider:
    def get_ip_info(self, ip):
        try:
            result = requests.get("http://freegeoip.net/json/{0}".format(ip), timeout=HTTP_REQUEST_TIMEOUT)
            result = result.json()
            return result

        except Exception, e:
            logger.error(e)

        return \
            {
                "ip": ip,
                "country_code": "---",
                "country_name": "---",
                "region_code": "---",
                "region_name": "---",
                "city": "---",
                "zipcode": "---",
                "latitude": 0,
                "longitude": 0,
                "metro_code": "0",
                "areacode": "0"
            }

########################################################################################################################
if __name__ == "__main__":
    cl = GeoIpProvider()
    print(cl.get_ip_info("87.69.129.84"))

