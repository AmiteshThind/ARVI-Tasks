import serial
import time

#configuring which port to connect to

arduinoSerial = serial.Serial('/dev/tty.usbmodem14201',9600)

#time is used to create a delay to establish a connection between the sensor(transmitter) and computer(reciver)
time.sleep(2)


while(True):
    print arduinoSerial.readline()# outputs value of the tempreaure sensor being read by arduino 
    

