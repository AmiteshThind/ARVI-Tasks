import serial
import time

#configuring which port to connect to

arduinoSerial = serial.Serial('/dev/tty.usbmodem14201',9600)

while True:
    print("Input: ")
    user_input =raw_input() #takes value of 1 or 0 from user
    if(user_input == '1'): #if user inputs value of 1 then 1 is sent to arduino
        arduinoSerial.write('1')
        print("Led ON")
        time.sleep(1)
        
    if (user_input == '0'):
        arduinoSerial.write(('0'))#if user inputs value of 0 then 1 is sent to arduino
        time.sleep(1)
        print("Led OFF")

