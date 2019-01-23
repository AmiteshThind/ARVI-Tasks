import serial
import time
import rospy
from std_msgs.msg import String

#configuring which port to connect to

arduinoSerial = serial.Serial('/dev/tty.usbmodem14201',9600)

def talker():
   pub = rospy.Publisher('chatter', String, queue_size=10)
   rospy.init_node('talker', anonymous=True)
   rate = rospy.Rate(10) # 10hz

   while not rospy.is_shutdown():
       tempreatureData = arduinoSerial.readline()
       rospy.loginfo(tempreatureData)
       pub.publish(tempreatureData)
       rate.sleep()

   if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass