__author__ = 'vovacooper'


from flask import Blueprint, request, Response, json

from classes.logger import logger

from providers.data_provider import DataProvider

########################################################################################################################
data_module = Blueprint("data_module", __name__, url_prefix="/data")


########################################################################################################################
@data_module.route("/init")
def get_data():
    try:
        request_data = \
            {
                "ip": request.remote_addr
            }

        #init data provider
        data_provider = DataProvider(request_data)
        #get data from provider
        response_data = data_provider.get_data()
        #make json
        response_json = json.dumps(response_data)

        return Response(response=response_json, status=200, mimetype="application/json",
                        headers={"P3P": "CP=\"IDC DSP COR ADM DEVi TAIi PSA PSD "
                                        "IVAi IVDi CONi HIS OUR IND CNT\""})
    except Exception, e:
        logger.exception(e)
        response = Response(response=None, status=200)
        return response


