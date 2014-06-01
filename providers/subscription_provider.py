__author__ = 'vovacooper'

from classes.mail import Mail

class SubscriptionProvider():
    _request_data = {}

    def __init__(self, request_data):
        self._request_data = request_data

    def get_data(self):
        SubscriptionProvider.subscribe(self._request_data["email"])
        return \
            {
                "status": "OK"
            }

    @staticmethod
    def subscribe(email):
        Mail.send_mail("vovacooper@gmail.com","Delta Price Support","New subscription registered","new subscription registered from " + email)
        return


