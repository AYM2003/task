#!/usr/bin/python3
import rospy
from std_msgs.msg import String
rospy.init_node("the_node_that_listens")

def  callback(msg):
    print(msg.data)

the_listener=rospy.Subscriber("gossip",String,callback)
rospy.spin()


