from structs.responseBody import ResponseBody
from flask import Response


class BulbService:
    def __init__(self):
        self._message = Response(ResponseBody(False, 'This command cannot be performed!').get_json())
        self._message.headers["Content-Type"] = 'application/json'

    def get_compatible_models(self): pass

    def on(self, access_token, home_id, device_id):
        return self._message

    def off(self, access_token, home_id, device_id):
        return self._message

    def on_off(self, access_token, home_id, device_id):
        return self._message

    def set_light_level(self, access_token, home_id, device_id, light_level):
        return self._message

    def set_light_color(self, access_token, home_id, device_id, hue, saturation):
        return self._message

    def set_light_temperature(self, access_token, home_id, device_id, light_temperature):
        return self._message
