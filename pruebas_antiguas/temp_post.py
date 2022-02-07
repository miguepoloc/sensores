# Se importa la librería encargada de controlar los tiempos de espera
import time
# Se utiliza Circuitpython para esto
# Se importa la librería que asigna los pines GPIO
import board
# Se importa la librería que controla el protocolo SPI
import busio
# Se importa la librería que controla los pines GPIO
import digitalio
# Se importa la librería de adafruit para el controlador de la RTC
import adafruit_max31865
import requests

from datetime import datetime

# Se asignan los pines encargados del protocolo SPI
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
# Se selecciona el pin donde está conectado el sensor o plata MAX31865
# En este caso se asigna el pin 5
cs = digitalio.DigitalInOut(board.D5)
# Se llama a la librería MAX31865 asignandole los pines spi, cs
# e indicandole que es una PT100 y de 3 cables
sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=100.0, wires=3)


# Se crea un bucle infinito
while True:
    now = datetime.now()
    fecha = str(now).split(".")
    # Lee la temperatura
    temp = sensor.temperature
    # Imprime el valor de la temperatura en °C
    print('Temperatura: {0:0.3f} °C'.format(temp))
    # Se imprime el valor que está leyendo la resistencia
    print('Resistencia: {0:0.3f} Ohms'.format(sensor.resistance))
    print(fecha[0])

    params = {
        "temperatura": round(sensor.temperature, 3),
        # "temperatura": 19,
        "fecha": "",
        "unidad": "°C",
        "flag": 4,
        "latitud": "11.229602",
        "longitud": "-74.163671"
    }
    r = requests.post('http://127.0.0.1:8000/api/temperatura/', data=params)
    print(r.text)
    time.sleep(10)
