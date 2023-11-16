#!/usr/bin/python3
import rospy
from std_msgs.msg import String
rospy.init_node("the_node_that_talks",anonymous=False)

the_talker=rospy.Publisher("gossip",String,queue_size=10)

rate=rospy.Rate(100)

while not rospy.is_shutdown():
    word="lalala";
    the_talker.publish(word)
    rate.sleep()