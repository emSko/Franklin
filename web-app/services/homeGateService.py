from propertiesService import PropertiesService
from apiService import *
from bulbService import BulbService


class HomeGateServiceSingleton:
    class HomeGateService:
        def __init__(self):

            self._property_service = None
            self.bulb_services = []

            self.grant_type = None
            self.client_id = None
            self.username = None
            self.password = None

            self.home_id = None

            self.access_token = None
            self.home_info = None

        def __read_properties(self):
            try:
                self.grant_type = self._property_service.get_property('HomeGateService.grant_type')
            except KeyError:
                self.grant_type = ''
                self._property_service.save_property('HomeGateService.grant_type', '')

            try:
                self.client_id = self._property_service.get_property("HomeGateService.client_id")
            except KeyError:
                self.client_id = ''
                self._property_service.save_property('HomeGateService.client_id', '')

            try:
                self.username = self._property_service.get_property("HomeGateService.username")
            except KeyError:
                self.username = ''
                self._property_service.save_property('HomeGateService.username', '')

            try:
                self.password = self._property_service.get_property("HomeGateService.password")
            except KeyError:
                self.password = ''
                self._property_service.save_property('HomeGateService.password', '')

            try:
                self.home_id = self._property_service.get_property("HomeGateService.home_id")
            except KeyError:
                self.home_id = ''
                self._property_service.save_property('HomeGateService.home_id', '')

            if self.grant_type == '':
                raise KeyError('grant_type property is empty')
            if self.client_id == '':
                raise KeyError('client_id property is empty')
            if self.username == '':
                raise KeyError('username property is empty')
            if self.password == '':
                raise KeyError('password property is empty')
            if self.home_id == '':
                raise KeyError('home_id property is empty')

        def __download_home_key(self):
            self.access_token = get_home_key(self.grant_type, self.client_id, self.username, self.password)[
                "access_token"]

        def __download_home_info(self):
            self.home_info = get_home_info(self.access_token, self.home_id)

        def init(self, properties_service):
            if isinstance(properties_service, PropertiesService):
                self._property_service = properties_service
            else:
                raise TypeError
            self.__read_properties()
            self.__download_home_key()
            self.__download_home_info()

        def add_bulb_service(self, bulb_service):
            if isinstance(bulb_service, BulbService):
                self.bulb_services.append(bulb_service)
            else:
                raise TypeError

        def reload(self):
            self.__read_properties()
            self.__download_home_key()
            self.__download_home_info()

        def get_bulbs(self):
            self.__download_home_info()
            bulbs = []
            for device in self.home_info['devices']:
                if device['productType'] == 'lightBulb':
                    bulbs.append(device)
            return bulbs

        def get_bulb_service(self, device_id):
            for bulb in self.home_info['devices']:
                if bulb['productType'] == 'lightBulb' and bulb['serialNo'] == device_id:
                    for bulb_service in self.bulb_services:
                        for bulb_model in bulb_service.get_compatible_models():
                            if bulb_model == bulb['model']:
                                return bulb_service
                    else:
                        raise NotImplementedError
            else:
                for bulb in self.home_info['devices']:
                    if bulb['productType'] == 'lightBulb' and bulb['serialNo'] == device_id:
                        for bulb_service in self.bulb_services:
                            for bulb_model in bulb_service.get_compatible_models():
                                if bulb_model == bulb['model']:
                                    return bulb_service
                        else:
                            raise NotImplementedError
                else:
                    raise KeyError

    __instance = None

    def __init__(self):
        if HomeGateServiceSingleton.__instance is None:
            HomeGateServiceSingleton.__instance = HomeGateServiceSingleton.HomeGateService()
        self.__dict__['_Singleton__instance'] = HomeGateServiceSingleton.__instance

    def __getattr__(self, attr):
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        return setattr(self.__instance, attr, value)
