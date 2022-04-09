from urllib.parse import urlencode
from urllib.request import Request, urlopen

import os
from os.path import join, dirname
from dotenv import load_dotenv

from schema import WaterLevel


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

RIVER_ID = os.environ.get("RIVER_ID")
RIVER_ACCESS_USER = os.environ.get("RIVER_ACCESS_USER")
RIVER_ACCESS_KEY = os.environ.get("RIVER_ACCESS_KEY")
ROUTE_URL = os.environ.get("REMOTE_URL").replace("<river_id>", RIVER_ID)


if __name__ == "__main__":
    water_level = WaterLevel(
        access_user=RIVER_ACCESS_USER, 
        accesss_key=RIVER_ACCESS_KEY, 
        sensor_height=1, 
        humidity=2,
    )

    payload = water_level.__dict__
    request = Request(ROUTE_URL, urlencode(payload).encode())
    response = urlopen(request).read().decode()
    print(response)

