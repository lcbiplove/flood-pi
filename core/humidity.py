import logging
import Adafruit_DHT

from . import settings


def get_humidity():
    """Gets humidity data from the sensor
        Returns: tuple (humidity, temperature)
    """
    humidity, temperature = Adafruit_DHT.read_retry(settings.HUMIDITY_PIN, settings.Hu)

    if humidity is not None and temperature is not None:
        logging.info(f"TEMP: {humidity} AND HUMID: {temperature}")
    else:
        logging.error("Error to get humidity data from sensor")

    return humidity, temperature

