from flask import Flask
from controllers.bulbController import bulb_controller
from controllers.homeController import home_controller
from controllers.websiteController import website_controller
from services.homeGateService import HomeGateServiceSingleton
from services.propertiesService import PropertiesService
from services.ikeaBulbService import IKEABulbService
from services.osramBulbService import OSRAMBulbService


app = Flask(__name__)

app.register_blueprint(bulb_controller, url_prefix='/bulb')
app.register_blueprint(home_controller, url_prefix='/home')
app.register_blueprint(website_controller)

if __name__ == '__main__':

    properties_service = PropertiesService('resources/config.properties')
    home_gate_service = HomeGateServiceSingleton()
    home_gate_service.init(properties_service)
    home_gate_service.add_bulb_service(IKEABulbService())
    home_gate_service.add_bulb_service(OSRAMBulbService())

    app.run(
        host='0.0.0.0',
        debug=True)
