#! /usr/bin/python

'''
Matt Droter's Path Follower, originally from https://gist.github.com/droter/eef584eccb0a7328f5b957c744fecf9b

Recreated here for convienence
'''
import rospy
import actionlib

from nav_msgs.msg import Path, Odometry
from geometry_msgs.msg import  PoseStamped, Pose
from tf.transformations import quaternion_from_euler
from math import pow, atan2, sqrt
from mbf_msgs.msg import (ExePathAction, ExePathFeedback, ExePathGoal, ExePathResult)
from geometry_msgs.msg import PoseStamped


class PathFollower():

    def __init__(self):
        self.vel_sub = rospy.Subscriber('drive_path', Path, self.path_callback)
        self.client = actionlib.SimpleActionClient('/move_base_flex/exe_path', ExePathAction)

        self.got_path = 0

        self.drive_path = Path()

        self.path_seq = 0
        self.poses = []
        self.safeDist = 1.0


    def path_callback(self, msg):
        if self.got_path == 0:
            self.drive_path = msg
            self.got_path = 1
            self.on_enter()


    def on_enter(self):
        # Create the goal.
        goal = ExePathGoal()
        goal.path = self.drive_path

        try:
            self.client.send_goal(goal)
        except Exception as e:
            rospy.logwarn('Failed to send goal:\n%s' % str(e))
            self._error = True


    def publish_point(self):
        rate = rospy.Rate(5)
        while not rospy.is_shutdown():
            #print("")
            rate.sleep()
        rospy.spin()


if __name__ == '__main__':
    rospy.init_node('path_follower_node')
    path_follower_object = PathFollower()
    try:
        path_follower_object.publish_point()
    except rospy.ROSInterruptException:
        pass