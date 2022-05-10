#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import logging

from . import settings


def get_distance():
      """Gets distance data from the sensor in cm
            Returns: decimal
      """
      distance = None
      try:
            GPIO.setmode(GPIO.BOARD)

            GPIO.setup(settings.ULTRASONIC_TRIGGER_PIN, GPIO.OUT)
            GPIO.setup(settings.ULTRASONIC_ECHO_PIN, GPIO.IN)

            GPIO.output(settings.ULTRASONIC_TRIGGER_PIN, GPIO.LOW)

            time.sleep(1)

            GPIO.output(settings.ULTRASONIC_TRIGGER_PIN, GPIO.HIGH)

            time.sleep(0.00001)

            GPIO.output(settings.ULTRASONIC_TRIGGER_PIN, GPIO.LOW)

            while GPIO.input(settings.ULTRASONIC_ECHO_PIN)==0:
                  pulse_start_time = time.time()
            while GPIO.input(settings.ULTRASONIC_ECHO_PIN)==1:
                  pulse_end_time = time.time()

            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration * 17150, 2)
      finally:
            GPIO.cleanup()

      if distance is None:
            logging.error("Error to get distance data from sensor")

      return distance




