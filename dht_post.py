import Adafruit_DHT
import time
import requests

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        params = {
            "temperatura": round(temperature, 3),
            # "temperatura": 19,
            "fecha": "",
            "unidad": "°C",
            "flag": 0,
            "latitud": "11.229602",
            "longitud": "-74.163671"
        }
        r = requests.post('http://192.168.0.14:8000/api/temperatura/', data=params)
        print("Temp={0:0.01f}°C  Humedad={1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to retrieve data from humidity sensor")

    time.sleep(5)
