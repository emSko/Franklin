from bulbService import BulbService
from apiService import do_device_command
from json import dumps


class IKEABulbService(BulbService):
    def __init__(self):
        BulbService.__init__(self)

    def get_compatible_models(self):
        return ['TRADFRI bulb GU10 WS 400lm']

    def on(self, access_token, home_id, device_id):
        return do_device_command(access_token, home_id, device_id, 1, 6, 1)

    def off(self, access_token, home_id, device_id):
        return do_device_command(access_token, home_id, device_id, 1, 6, 0)

    def on_off(self, access_token, home_id, device_id):
        return do_device_command(access_token, home_id, device_id, 1, 6, 2)

    def set_light_level(self, access_token, home_id, device_id, light_level):
        payload = {'data': (format(int(light_level) * 254 / 100, 'x')).zfill(2) + 'ffff'}
        return do_device_command(access_token, home_id, device_id, 1, 8, 0, dumps(payload))

    def set_light_temperature(self, access_token, home_id, device_id, light_temperature):
        data = format(1000000/(int(light_temperature) * 18 + 2200), 'x').zfill(4)
        payload = {'data': data[2] + data[3] + data[0] + data[1] + '0000'}
        return do_device_command(access_token, home_id, device_id, 1, 0x0300, 10, dumps(payload))
