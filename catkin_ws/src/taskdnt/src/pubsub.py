#!/usr/bin/python3
import rospy
from std_msgs.msg import String

def caesar_cipher_decrypt(text, shift):
    
    result = ""
    for char in text:
        if char.isalpha():
            check = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - check - shift) % 26 + check)
        else:
            result += char
    return result

def callback(msg):

    rospy.loginfo("Received encrypted name: %s", msg.data)
    decrypted_name = caesar_cipher_decrypt(msg.data, 3)   
    rospy.loginfo("Publishing decrypted name: %s", decrypted_name)
    pub.publish(decrypted_name)

def pubsub():

    rospy.init_node('pubsub_node', anonymous=True)
    rospy.Subscriber('encrypted_name', String, callback)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():

        rate.sleep()

pub = rospy.Publisher('decrypted_name', String, queue_size=10)
pubsub()
    