# Flood detection for raspberry pi

This is the raspberry pi setup for flood detection portal to send sensor data to the remote server.

### _Installation_
You will first have to install python3 version. Then, clone the project and create all the dependencies inside virtual environment.
```
sudo apt update
sudo apt install python3 idle3
git clone https://github.com/lcbiplove/flood-pi.git
cd flood-pi
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```