__author__ = 'vovacooper'
# http://catalog.bizrate.com/services/catalog/v1/documentation/service_1.html?publisherId=606425&apiKey=ee723a9c9d485d354eed4b587f76ced8#representations

from affiliate_base_module import AffiliateBase

import requests
from classes.config import *


########################################################################################################################
class AffiliateShopzilla(AffiliateBase):
    PUBLISHER_ID = '606425'
    API_KEY = 'ee723a9c9d485d354eed4b587f76ced8'

    def __init__(self, placement_id, format, callback):
        AffiliateBase.__init__(self, placement_id, format, callback)

        self.generic_service["apiKey"] = self.API_KEY
        self.generic_service["publisherId"] = self.PUBLISHER_ID

    product_service = \
        {
            "categoryId": "",
            "keyword": None,
            "productId": None,
            "productIdType": None,
            "offersOnly": False,
            "merchantId": None,
            "brandId": None,
            "biddedOnly": True,
            "minPrice": None,
            "maxPrice": None,
            "minMarkdown": None,
            "zipCode": None,
            "freeShipping": False,
            "start": 0,
            "results": 10,
            "backfillResults": 0,
            "startOffers": 0,
            "resultsOffers": 0,
            "sort": "relevancy_desc",
            "attFilter": None,
            "attWeights": None,
            "attributeId": None,
            "resultsAttribute": 10,
            "resultsAttributeValues": 10,
            "showAttributes": False,
            "showProductAttributes": False,
            "minRelevancyScore": 100,
            "maxAge": None,
            "showRawUrl": False,
            "imageOnly": False,
            "reviews": None,
            "retailOnly": False
        }

    brand_service = \
        {
            "categoryId": None,
            "keyword": None,
            "brandName": None,
            "start": None,
            "results": None,
            "attFilter": None
        }

    attribute_service = \
        {
            "categoryId": None,
            "keyword": None,
            "attributeId": None,
            "attFilter": None,
            "results": None,
            "resultsAttributeValues": None,
            "minMarkdown": None,
            "maxAge": None
        }

    taxonomy_service = \
        {
            "categoryId": None,
            "keyword": None,
            "ancestors": None,
            "results": None,
            "sort": None,
            "attFilter": None
        }

    merchant_service = \
        {
            "merchantId": None,
            "timePeriod": None,
            "startDate": None,
            "endDate": None,
            "start": None,
            "results": None,
            "minOSAT": None,
            "minMerchantOSAT": None,
            "showRatings": None,
            "showReviews": None,
            "filterEmptyComments": None,
            "showMerchantDetails": None,
            "ratedOnly": None,
            "certifiedOnly": None
        }

    product_review_service = \
        {
            "productId": None,
            "reviews": None,
            "start": None,
            "results": None,
            "sort": None
        }

    def get_product(self, data):
        """get product from affiliate provider"""
        payload = {}
        payload.update(self.generic_service)
        payload.update(self.product_service)

        r = requests.get("http://catalog.bizrate.com/services/catalog/v1/us/{0}".format("product"), params=payload)
        print("URL: ")
        print(r.url)

        print("RESPONSE: ")
        print(r.json())

        return

    def get_offer(self, data):
        """get offer from affiliate provider"""
        payload = {}
        payload.update(self.generic_service)
        payload.update(self.product_service)

        r = requests.get("http://catalog.bizrate.com/services/catalog/v1/us/{0}".format("offer"), params=payload)
        print("URL: ")
        print(r.url)

        print("RESPONSE: ")
        print(r.json())

        return


########################################################################################################################

########################################################################################################################
if __name__ == "__main__":
    a = AffiliateShopzilla(1, "json", "callback")
    a.get_product({})
