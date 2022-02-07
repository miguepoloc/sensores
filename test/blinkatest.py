import board
import digitalio
import busio

print("Hello blinka!")

# Try to great a Digital input
pin = digitalio.DigitalInOut(board.D4)
print("Digital IO ok!")

# Try to create an I2C device
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C ok!")

# Try to create an SPI device
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print("SPI ok!")

import time
import board
import digitalio

print("hello blinky!")

led = digitalio.DigitalInOut(board.D20)
led.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.D21)
led2.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    led2.value = False
    time.sleep(0.5)
    led.value = False
    led2.value = True
    time.sleep(0.5)

print("done!")
