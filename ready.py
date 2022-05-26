#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import logging
import Adafruit_DHT

ULTRASONIC_ECHO_PIN=11
ULTRASONIC_TRIGGER_PIN=12
HUMIDITY_PIN=4

def get_distance():
      """Gets distance data from the sensor in cm
            Returns: decimal
      """
      distance = None
      try:
            GPIO.setmode(GPIO.BOARD)

            GPIO.setup(ULTRASONIC_TRIGGER_PIN, GPIO.OUT)
            GPIO.setup(ULTRASONIC_ECHO_PIN, GPIO.IN)

            GPIO.output(ULTRASONIC_TRIGGER_PIN, GPIO.LOW)

            time.sleep(1)

            GPIO.output(ULTRASONIC_TRIGGER_PIN, GPIO.HIGH)

            time.sleep(0.00001)

            GPIO.output(ULTRASONIC_TRIGGER_PIN, GPIO.LOW)

            while GPIO.input(ULTRASONIC_ECHO_PIN)==0:
                  pulse_start_time = time.time()
            while GPIO.input(ULTRASONIC_ECHO_PIN)==1:
                  pulse_end_time = time.time()

            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration * 17150, 2)
      finally:
            GPIO.cleanup()

      if distance is None:
            logging.error("Error to get distance data from sensor")

      return distance


def get_humidity():
    """Gets humidity data from the sensor
        Returns: tuple (humidity, temperature)
    """
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, HUMIDITY_PIN)

    if humidity is not None and temperature is not None:
        logging.info(f"TEMP: {humidity} AND HUMID: {temperature}")
    else:
        logging.error("Error to get humidity data from sensor")

    return humidity, temperature


while True:
    print("Distance: ", get_distance())
    print("Humidity & Temperature: ", get_humidity())