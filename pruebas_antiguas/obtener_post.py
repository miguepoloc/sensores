# DHT - Temperatura y humedad
import Adafruit_DHT
# Giroscopio y Magnetometro
from i2clibraries import i2c_itg3205, i2c_hmc5883l
# Acelerometro
import board
import busio
import adafruit_adxl34x
# Tiempo
import time
# Http
import requests


# Configuración i2c
i2c = busio.I2C(board.SCL, board.SDA)

# Configuraciones DHT
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 21

# Configuracion giroscopio
itg3205 = i2c_itg3205.i2c_itg3205(1)

# Configuracion acelerometro
accelerometer = adafruit_adxl34x.ADXL343(i2c)
accelerometer.enable_motion_detection()
# Alternativamente, puede especificar el umbral cuando habilita la detección de movimiento para un mayor control:
# accelerometer.enable_motion_detection(threshold=10)


# Configuracion magnetometro
# Se elige el puerto i2c para usar, RPi3 model B usa port 1
hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1)
hmc5883l.setContinuousMode()

# Escriba la declinación magnética de su ubicación (degrees, minute)
hmc5883l.setDeclination(0, 6)

# Variables
vector_variable = ("Temperatura dht", "Humedad", "Temperatura", "X Giroscopio",
                   "Y Giroscopio", "Z Giroscopio", "X Acelerómetro", "Y Acelerómetro", "Z Acelerómetro")
variable_codigo = (1, 2, 3, 4, 5, 6, 7, 8)
unidad = ("°C", "%", "°C", "°/s", "°/s", "°/s", "m/s2", "m/s2", "m/s2")
while True:
    # Se obtiene la temperatura y la humedad del DHT
    humedad, temperatura_dht = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    # Si la humedad y la temperatura es diferente de nada
    if humedad is not None and temperatura_dht is not None:
        print(
            "Temp={0:0.01f}*C  humedad={1:0.1f}%".format(temperatura_dht, humedad))
    else:
        print("Error al recibir datos del DHT")

    # Se obtiene el estado del sensor
    (itgready, dataready) = itg3205.getInterruptStatus()
    # Si hay datos
    if dataready:
        # Obtiene una temperatura de este sensor
        temp = itg3205.getDieTemperature()
        # Se obtiene la inclinación de cada eje
        (x_giro, y_giro, z_giro) = itg3205.getDegPerSecAxes()
        print("Temp: "+str(temp))
        print("X giroscopio:    "+str(x_giro))
        print("Y giroscopio:    "+str(y_giro))
        print("Z giroscopio:    "+str(z_giro))
        print("")

    # Se obtienen los datos de la aceleración
    (x_ace, y_ace, z_ace) = itg3205.getDegPerSecAxes()
    print("X acelerómetro:    "+str(x_ace))
    print("Y acelerómetro:    "+str(y_ace))
    print("Z acelerómetro:    "+str(z_ace))
    # print("%f %f %f" % accelerometer.acceleration)

    # Detector de movimiento
    mov = accelerometer.events['motion']
    print("Motion detected: %s" % accelerometer.events['motion'])

    # Se muestra el valor del magnetómetro
    print(hmc5883l)

    cont = 0
    variable = (temperatura_dht, humedad, temp, x_giro,
            y_giro, z_giro, x_ace, y_ace, z_ace)
    for i in vector_variable:
        params = {
            "variable_nombre": i,
            "variable_codigo": cont,
            "variable_valor": variable[cont],
            "fecha": "",
            "unidad": unidad[cont],
            "flag": 0,
            "latitud": "11.1432138252",
            "longitud": "-74.22381520268"
        }
        r = requests.post(
            'http://192.168.0.18:8000/api/sensores/', data=params)
        cont = cont + 1

    time.sleep(5)
