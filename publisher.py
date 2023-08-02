#! usr/bin/env python

import rospy
from std_msgs.msg import Bool

def button_publisher():
    rospy.init_node('button_publisher')
    pub = rospy.Publisher('button_topic', Bool, queue_size = 10)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        button_input = input("Press Enter to send True: ")
        button_value = True if button_input == '' else False
        pub.publish(button_value)
        rate.sleep()


if __name__ == '__main__':
    try:
        button_publisher()
    except rospy.ROSInterruptException:
        pass