from flask import Blueprint, request, Response
from services.homeGateService import HomeGateServiceSingleton

my_home_gate_service = HomeGateServiceSingleton()

bulb_controller = Blueprint('bulb_controller', __name__)


@bulb_controller.route('/<bulb_id>/identify', methods=['POST'])
def identify(bulb_id):
    bulb_service = my_home_gate_service.get_bulb_service(bulb_id)
    ret = bulb_service.identify(my_home_gate_service.access_token,
                                my_home_gate_service.home_id,
                                bulb_id)
    return ret


@bulb_controller.route('/<bulb_id>/off', methods=['POST'])
def off(bulb_id):
    bulb_service = my_home_gate_service.get_bulb_service(bulb_id)
    ret = bulb_service.off(my_home_gate_service.access_token,
                              my_home_gate_service.home_id,
                              bulb_id)
    return ret


@bulb_controller.route('/<bulb_id>/on', methods=['POST'])
def on(bulb_id):
    bulb_service = my_home_gate_service.get_bulb_service(bulb_id)
    ret = bulb_service.on(my_home_gate_service.access_token,
                              my_home_gate_service.home_id,
                              bulb_id)
    return ret


@bulb_controller.route('/<bulb_id>/onoff', methods=['POST'])
def onoff(bulb_id):
    bulb_service = my_home_gate_service.get_bulb_service(bulb_id)
    ret = bulb_service.on_off(my_home_gate_service.access_token,
                              my_home_gate_service.home_id,
                              bulb_id)
    return ret


@bulb_controller.route('/<bulb_id>/set-light-level', methods=['POST'])
def set_light_level(bulb_id):
    light_level = request.get_json()['data']
    bulb_service = my_home_gate_service.get_bulb_service(bulb_id)
    ret = bulb_service.set_light_level(my_home_gate_service.access_token,
                                       my_home_gate_service.home_id,
                                       bulb_id,
                                       light_level)
    return ret


@bulb_controller.route('/<bulb_id>/set-light-temperature', methods=['POST'])
def set_light_temperature(bulb_id):
    light_temperature = request.get_json()['data']
    bulb_service = my_home_gate_service.get_bulb_service(bulb_id)
    ret = bulb_service.set_light_temperature(my_home_gate_service.access_token,
                                             my_home_gate_service.home_id,
                                             bulb_id,
                                             light_temperature)
    return ret


@bulb_controller.route('/<bulb_id>/set-color', methods=['POST'])
def set_color(bulb_id):
    hue = request.get_json()['hue']
    saturation = request.get_json()['saturation']
    bulb_service = my_home_gate_service.get_bulb_service(bulb_id)
    ret = bulb_service.set_light_color(my_home_gate_service.access_token,
                                       my_home_gate_service.home_id,
                                       bulb_id,
                                       hue,
                                       saturation)
    return ret
