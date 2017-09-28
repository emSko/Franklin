from bulbService import BulbService
from apiService import do_device_command
from json import dumps


class OSRAMBulbService(BulbService):
    def __init__(self):
        BulbService.__init__(self)

    def get_compatible_models(self):
        return ['PAR 16 50 RGBW - LIGHTIFY']

    def on(self, access_token, home_id, device_id):
        return do_device_command(access_token, home_id, device_id, 3, 6, 1)

    def off(self, access_token, home_id, device_id):
        return do_device_command(access_token, home_id, device_id, 3, 6, 0)

    def set_light_level(self, access_token, home_id, device_id, light_level):
        payload = {'data': (format(int(light_level) * 254 / 100, 'x')).zfill(2) + 'ffff'}
        return do_device_command(access_token, home_id, device_id, 3, 8, 0, dumps(payload))

    def set_light_temperature(self, access_token, home_id, device_id, light_temperature):
        data = format(1000000/(int(light_temperature) * 18 + 2200), 'x').zfill(4)
        payload = {'data': data[2] + data[3] + data[0] + data[1] + '0000'}
        return do_device_command(access_token, home_id, device_id, 3, 0x0300, 10, dumps(payload))

    def set_light_color(self, access_token, home_id, device_id, hue, saturation):
        data = format(int(int(hue) * 254/360), 'x')
        data2 = format(int(int(saturation) * 2.54), 'x')
        payload = {'data': data + data2 + '00000000'}
        print payload
        return do_device_command(access_token, home_id, device_id, 3, 768, 6, dumps(payload))
