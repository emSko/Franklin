from flask import Blueprint, Response
from structs.responseBody import ResponseBody
from services.homeGateService import HomeGateServiceSingleton
from services.ikeaBulbService import IKEABulbService

my_home_gate_service = HomeGateServiceSingleton()
my_home_gate_service.add_bulb_service(IKEABulbService())

home_controller = Blueprint('home_controller', __name__)


@home_controller.route('/reload', methods=['POST'])
def reload():
    my_home_gate_service.reload()
    response = Response(ResponseBody(True, 'server has been reloaded').get_json())
    response.headers["Content-Type"] = 'application/json'
    return response


@home_controller.route('/bulbs', methods=['GET'])
def get_bulbs():
    response = Response(ResponseBody(True, my_home_gate_service.get_bulbs()).get_json())
    response.headers["Content-Type"] = 'application/json'
    return response

# json odpowiedzi
# status: succes
# response: np. json
# albo status: error
# przechwycic wyjatki!