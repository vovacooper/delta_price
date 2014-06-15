__author__ = 'vovacooper'

from providers import geo_ip_provider

#from classes.mongo import db
#from providers.geo_ip_provider import GeoIpProvider
#from classes.logger import logger


########################################################################################################################
class DeltaPriceProvider():

    def __init__(self):
        return

    def get_js(self, request_data):
        return 'alert("No js in delta_price provider!!!!");'

    def get_data(self, request_data):
        _gip = geo_ip_provider.GeoIpProvider()
        _json_gip = _gip.get_ip_info(request_data["ip"])
        return \
            {
                "publisher_id": request_data["publisher_id"],
                "placement_id": request_data["placement_id"],
                "geo_ip_data": _json_gip
            }
