import time
import serial
import string
import pynmea2

port = "/dev/ttyAMA0"

ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)

while 1:
    try:
        data = ser.readline()
    except:
        print("loading")
    if '$GPGGA' in str(data):
        print(data)
        msg = pynmea2.parse(data.decode(encoding="utf-8"))
        latval = msg.latitude
        concatlat = "lat: " + str(latval)
        print (concatlat)
        longval = msg.longitude
        concatlon = "Long: " + str(longval)
        print (concatlon)
        
    time.sleep(1)