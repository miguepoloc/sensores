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

import psycopg2
from datetime import datetime

conexion1 = psycopg2.connect(database="boya", user="admin", password="Contrasena1!")
cursor1 = conexion1.cursor()
sql = "insert into api_temperatura(temperatura, fecha, unidad, flag, latitud, longitud) values (%s,%s,%s,%s, %s,%s)"
conexion1.commit()

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
    datos = (round(sensor.temperature, 3),
             fecha[0], "°C", 4, "11.229602", "-74.163671")
    print(fecha[0])
    cursor1.execute(sql, datos)
    conexion1.commit()
    # Se espera 1 segundo
    time.sleep(2)

conexion1.close()
