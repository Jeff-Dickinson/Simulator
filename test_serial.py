import time
import serial

ser = serial.Serial ("COM6")
ser.baudrate = 9600

ser.write(b'cls WHITE\xFF\xFF\xFF')

ser.close()