# Se importan las librerías a utilizar
import time
# La librería board es una forma de llamar a los pines de la Rpi
import board
# Se importa la librería del bme280 de adafruit
from adafruit_bme280 import basic as adafruit_bme280

# Se crea el sensro, usando los pines por defecto de la Rpi para I2C
i2c = board.I2C()  # Usa los pines board.SCL (3) y board.SDA (2)
# Debido a que el sensor que tenemos cuenta con la dirección 0x76 y no 0x77 que es con la que viene por defecto
# Se debe agregar el parámetro de address como se observa abajo
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

# Se debe colocar la presión (hPa) sobre el nivel del mar del lugar en que se encuentre
# Sería bueno consumir un api que entregue esta información a partir de las coordenadas
bme280.sea_level_pressure = 1010

while True:
    print("\nTemperatura: %0.1f C" % bme280.temperature)
    print("Humedad: %0.1f %%" % bme280.relative_humidity)
    print("Presión: %0.1f hPa" % bme280.pressure)
    print("Altura = %0.2f metros" % bme280.altitude)
    time.sleep(2)
