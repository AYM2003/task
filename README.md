Publisher Subscriber task
Three nodes are created for a caesar cipher encryption/decryption code
1) First create a workspace in home directory
2) Then create an src file
3) Created a taskdnt names package
4) Again created an src file
5) Here in src file the three nodes will be saved
pub.py - ROS Publisher Node:
    * Encrypts a string (your name) using the Caesar cipher.
    * Publishes the encrypted name on a ROS topic.
pubsub.py - ROS Node (Subscriber/Publisher):
    * Subscribes to the topic from pub.py.
    * Decrypts the encrypted name using the Caesar cipher.
    * Publishes the decrypted name on a new ROS topic.
sub.py - ROS Subscriber Node:
    * Listens to the final topic from pubsub.py.
    * Prints out the decrypted name.
Usage:
    * Launch each script in separate terminals using rosrun.
    * Terminal 1: roscore
    * Terminal 2: rosrun your_package_name pub.py
    * Terminal 3: rosrun your_package_name pubsub.py
    * Terminal 4: rosrun your_package_name sub.py
Using the rqt_graph command all the nodes and topics can be seen and the publishers and subscribers can be identified.
