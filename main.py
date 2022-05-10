import logging
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from core import schema, settings, distance, humidity

if __name__ == "__main__":
    sensor_height = distance.get_distance()
    humid, temp = humidity.get_humidity()

    water_level = schema.WaterLevel(
        access_user=settings.RIVER_ACCESS_USER, 
        accesss_key=settings.RIVER_ACCESS_KEY, 
        sensor_height=sensor_height,
        humidity=humid,
        temperature=temp,
    )

    payload = water_level.__dict__
    request = Request(settings.ADD_DATA_ROUTE, urlencode(payload).encode())
    response = urlopen(request).read().decode()
    logging.info(response)

