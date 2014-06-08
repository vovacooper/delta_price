__author__ = 'vovacooper'


from flask import Blueprint, request, Response, json

from classes.logger import logger

from providers.deltaprice_provider import DeltaPriceProvider


########################################################################################################################
deltaprice_module = Blueprint("deltaprice_module", __name__, url_prefix="/dp")


########################################################################################################################
'''
callback - for JSONP response
publisher_id - the id of the publisher
placement_id - the placement, should be XXX?!
'''
@deltaprice_module.route("/get_js")
def get_js():
    try:
        request_data = \
            {
                "ip": request.remote_addr,
                "callback": request.args.get("callback", False),
                "publisher_id": request.args.get("tags", False),
                "placement_id": request.args.get("tags", False)
            }

        #init data provider
        deltaprice_provider = DeltaPriceProvider()
        #get data from provider
        response_data = deltaprice_provider.get_js(request_data)
        #make json
        response_json = json.dumps(response_data)

        #JSONP
        if request_data["callback"]:
            response_json = "{0}({1})".format(request_data["callback"], json.dumps(response_data))

        return Response(response=response_json, status=200, mimetype="application/json",
                        headers={"P3P": "CP=\"IDC DSP COR ADM DEVi TAIi PSA PSD "
                                        "IVAi IVDi CONi HIS OUR IND CNT\""})
    except Exception, e:
        logger.exception(e)
        response = Response(response=None, status=200)
        return response


@deltaprice_module.route("/get_data")
def get_data():
    try:
        request_data = \
            {
                "ip": request.remote_addr,
                "callback": request.args.get("callback", False),
                "publisher_id": request.args.get("publisher_id", False),
                "placement_id": request.args.get("placement_id", False)
            }

        #init data provider
        deltaprice_provider = DeltaPriceProvider()
        #get data from provider
        response_data = deltaprice_provider.get_data(request_data)
        #make json
        response_json = json.dumps(response_data)

        #JSONP
        if request_data["callback"]:
            response_json = "{0}({1})".format(request_data["callback"], json.dumps(response_data))

        return Response(response=response_json, status=200, mimetype="application/json",
                        headers={"P3P": "CP=\"IDC DSP COR ADM DEVi TAIi PSA PSD "
                                        "IVAi IVDi CONi HIS OUR IND CNT\""})
    except Exception, e:
        logger.exception(e)
        response = Response(response=None, status=200)
        return response



