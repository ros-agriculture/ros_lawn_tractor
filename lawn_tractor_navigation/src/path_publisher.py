#! /usr/bin/python

'''
Matt Droter's Path Publisher, orginally from https://gist.github.com/droter/cc63dd40b866bcfe3874bb35fa6c46f9

Recreated here for convienence
'''

import rospy
import rospkg
from nav_msgs.msg import Path
from geometry_msgs.msg import  PoseStamped
from tf.transformations import quaternion_from_euler
from std_msgs.msg import Float64

def path_publisher():
    rospy.init_node('path_publisher')
    path_pub = rospy.Publisher('/drive_path', Path, queue_size=10)

    path = Path()
    
    path.header.frame_id = "map"
    path.header.seq = 0
    path.header.stamp = rospy.Time.now()
    
    seq = 0

    for line in content:
        #print(line)
        pose = PoseStamped()
        
        points = line.split()
        #print(points)
        x = float(points[0])
        y = float(points[1])
        yaw = float(points[2])

        quat = quaternion_from_euler(0, 0, yaw)

        pose.header.frame_id = "map"
        pose.header.seq = seq
        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = 0
        pose.pose.orientation.x = quat[0]
        pose.pose.orientation.y = quat[1]
        pose.pose.orientation.z = quat[2]
        pose.pose.orientation.w = quat[3]
        pose.header.stamp = path.header.stamp
        
        path.poses.append(pose)

        seq += 1


    while not rospy.is_shutdown():
        path_pub.publish(path)

        rospy.sleep(5)


content = {}
def load_file():
    # TODO: Get filename from rosparam
    # File format each waypoint on its own line:  
    #  x y yaw
    #  x y yaw
    
    global content
    pkg_filepath = rospkg.RosPack().get_path('lawn_tractor_navigation')
    path_filepath = pkg_filepath + "/example_path.txt"
    rospy.loginfo(path_filepath)
    with open(path_filepath, 'r') as file:
         content = file.readlines()
         content = [x.strip() for x in content]


if __name__ == '__main__':
    load_file()
    path_publisher()