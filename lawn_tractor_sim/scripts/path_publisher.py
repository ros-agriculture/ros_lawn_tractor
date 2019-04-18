#! /usr/bin/python

import rospy
import roslaunch
import rospkg
from nav_msgs.msg import Path, Odometry
from geometry_msgs.msg import  PoseStamped
from tf.transformations import quaternion_from_euler


def path_publisher():
    rospy.init_node('path_publisher')
    content = {}
    rospack = rospkg.RosPack()
    path_pub = rospy.Publisher('/drive_path', Path, queue_size=10)

    points_file = rospy.get_param('~path_test', 'generated_points.txt')

    generated_points = rospack.get_path('lawn_tractor_sim') + '/paths/' + points_file

    try:
        with open(generated_points, 'r') as file:
            content = file.readlines()
            content = [x.strip() for x in content]
    except IOError:
        rospy.loginfo("Could not open generted_points.txt file." + generated_points)
        pass


    path = Path()
    
    path.header.frame_id = "map"
    path.header.seq = 0
    path.header.stamp = rospy.Time.now()
    
    seq = 0

    for line in content:
        pose = PoseStamped()
        
        points = line.split()
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


if __name__ == '__main__':
    try:
        path_publisher()
    except rospy.ROSInterruptException:
        pass