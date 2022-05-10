from uuid import getnode as get_mac

class WaterLevelSchema:
    ACCESS_USER = "access_user"
    ACCESS_KEY = "access_key"
    SENSOR_HEIGHT = "sensor_height"
    HUMIDITY = "humidity"
    
class WaterLevel:
    def __init__(self, access_user, accesss_key, sensor_height, humidity, temperature) -> None:
        self.access_user = access_user
        self.accesss_key = accesss_key
        self.sensor_height = sensor_height
        self.humidity = humidity
        self.temperature = temperature
        self.mac_address = ":".join(("%012X" % get_mac())[i:i+2] for i in range(0, 12, 2))