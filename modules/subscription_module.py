__author__ = 'vovacooper'

from classes.logger import logger

from providers.subscription_provider import SubscriptionProvider

from flask import Blueprint, request, Response, json

########################################################################################################################
subscription_module = Blueprint("subscription_module", __name__, url_prefix="/subscribe")

########################################################################################################################
@subscription_module.route('/')
def subscribe():
    try:
        request_data = \
            {
                "ip": request.remote_addr,
                "callback": request.args.get("callback", False),
                "email": request.args.get("email", False)
            }

        #init data provider
        subscription_provider = SubscriptionProvider(request_data)
        #get data from provider
        response_data = subscription_provider.get_data()
        #make json
        response_json = json.dumps(response_data)

        if request_data["callback"]:
            response_json = "{0}({1})".format(request_data["callback"], json.dumps(response_data))

        return Response(response=response_json, status=200, mimetype="application/json",
                        headers={"P3P": "CP=\"IDC DSP COR ADM DEVi TAIi PSA PSD "
                                        "IVAi IVDi CONi HIS OUR IND CNT\""})
    except Exception, e:
        logger.exception(e)
        response = Response(response=None, status=200)
        return response



