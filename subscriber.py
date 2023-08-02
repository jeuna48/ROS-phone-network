#! usr/bin/env python

import rospy
from std_msgs.msg import Bool
import subprocess

def button_callback(msg):
    if msg.data:
        # 'rosbag record -a' 명령 실행
        subprocess.Popen(['rosbag', 'record', '-a'])
    else:
        # 'rosbag record' 중지
        subprocess.Popen(['rosbag', 'kill', '/record'])


def button_subscriber():
    rospy.init_node('button_subscriber')
    rospy.Subscriber('button_topic', Bool, button_callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        button_subscriber()
    except rospy.ROSInterruptException:
        pass