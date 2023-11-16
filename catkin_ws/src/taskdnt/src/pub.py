#!/usr/bin/python3
import rospy
from std_msgs.msg import String



def encrypt_text(plaintext,n):
     
    word = ""
 
    for i in range(len(plaintext)):
        ch = plaintext[i]
        word += chr((ord(ch) + n-65) % 26 + 65)
    return word

def publish_encryption():
    
    rospy.init_node("encryption_node",anonymous=True)

    plaintext = "AAYUSHI"
    n=3

    the_encrypter=rospy.Publisher("/encrypted_name",String,queue_size=1)

    rate=rospy.Rate(100)

    while not rospy.is_shutdown():
        word=encrypt_text(plaintext,n)
        rospy.loginfo(f"Publishing encrypted name: {word}")
        the_encrypter.publish(word)
        rate.sleep()
if __name__=='__main__':
    try:
        publish_encryption()
    except rospy.ROSInterruptException:
        pass

