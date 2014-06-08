__author__ = 'vovacooper'

TTL = 10


########################################################################################################################
class AffiliateBase(object):
    """
    Abstract class representing an affiliation.
    """
    generic_service = \
        {
            "apiKey": None,
            "publisherId": None,
            "placementId": 1,
            "format": "json",
            "callback": "callback"
        }
    def __init__(self, placement_id, format, callback):
        self.generic_service["placementId"] = placement_id
        self.generic_service["format"] = format
        self.generic_service["callback"] = callback

    def get_product(self, data):
        """
        get product from affiliate provider
        data:
            {

            }
        return:
            {

            }
        """
        return

    def get_offer(self, data):
        """
        get offer from affiliate provider
        data:
        {

        }
        return:
        {

        }
        """
        return

########################################################################################################################