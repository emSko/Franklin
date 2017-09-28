from json import dumps


class ResponseBody:
    def __init__(self, is_success, body):
        if isinstance(is_success, bool):
            self.is_success = is_success
        else:
            raise TypeError
        self.body = body

    def get_json(self):
        return dumps({
            'status': 'success' if (self.is_success == True) else 'fail',
            'message': self.body
        })
