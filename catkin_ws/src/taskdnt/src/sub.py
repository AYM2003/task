#!/usr/bin/python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("Received decrypted name: %s", msg.data)

def subscriber():
    rospy.init_node('subscriber_node', anonymous=True)
    rospy.Subscriber('decrypted_name', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass