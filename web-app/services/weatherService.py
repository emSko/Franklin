import requests
import propertiesService


class WeatherService:
    def __init__(self, property_service):
        """
        Initializes WeatherService

        city_code: Unique city code. You can find proper one in city.list.json.gz file on http://bulk.openweathermap.org/sample/
        api_key: Application key. You can get it after registration on https://openweathermap.org
        """
        if isinstance(property_service, propertiesService.PropertiesService):
            self._property_service = property_service
        else:
            raise TypeError

        self._city = None  # city name
        self._temperature = None  # temperature [Celsius degrees]
        self._pressure = None  # pressure [hPa]
        self._humidity = None  # humidity [%]

        self.__load_properties()

    def __load_properties(self):
        try:
            self._city_code = self._property_service.get_property('WeatherService.city_code')
        except KeyError:
            self._city_code = ''
            self._property_service.save_property('WeatherService.city_code', '')

        try:
            self._api_key = self._property_service.get_property('WeatherService.api_key')
        except KeyError:
            self._api_key = ''
            self._property_service.save_property('WeatherService.api_key', '')

        if self._city_code == '' or self._api_key == '':
            raise KeyError('at least one WeatherService property is empty')

    def get_current_weather(self):

        response = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?id=' + self._city_code + '&APPID=' + self._api_key)

        if response.status_code == 200:
            return {"city": response.json()['name'],
                    "temperature": response.json()['main']['temp'] - 273,
                    "pressure": response.json()['main']['pressure'],
                    "humidity": response.json()['main']['humidity']
                    }
        else:
            raise requests.exceptions.RequestException("Couldn't get weather :(")
