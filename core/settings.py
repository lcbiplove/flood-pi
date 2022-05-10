import os
from dotenv import load_dotenv

load_dotenv()

"""Time interval to send request to server (in seconds)"""
REQUEST_TIME_INTERVAL = os.environ.get("REQUEST_TIME_INTERVAL", 10)

"""Id of river"""
RIVER_ID = os.environ.get("RIVER_ID")

"""River acces username from admin panel"""
RIVER_ACCESS_USER = os.environ.get("RIVER_ACCESS_USER")

"""River access key from admin panel"""
RIVER_ACCESS_KEY = os.environ.get("RIVER_ACCESS_KEY")

"""River url where data is to be sent"""
ADD_DATA_ROUTE = f"http://{os.environ.get('REMOTE_URL')}/rivers/{RIVER_ID}/water-level"

"""Physical Echo PIN of ultrasonic sensors in raspberry"""
ULTRASONIC_ECHO_PIN = os.environ.get("ULTRASONIC_ECHO_PIN", 11)

"""Physical Trigger PIN of ultrasonic sensors in raspberry"""
ULTRASONIC_TRIGGER_PIN = os.environ.get("ULTRASONIC_TRIGGER_PIN", 12)

"""Physical HUMIDITY PIN of ultrasonic sensors in raspberry"""
HUMIDITY_PIN = os.environ.get("HUMIDITY_PIN", 4)