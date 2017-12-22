#!/usr/bin/env python
#Useful ref for making new srv and msg: 
#http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv#Creating_a_msg
#http://wiki.ros.org/ROS/Tutorials/CustomMessagePublisherSubscriber%28python%29
#import roslib; roslib.load_manifest('Course_Exemplary_assignment')
import rospy

from turtlebot3_console_controller.srv import NLP
from turtlebot3_console_controller.msg import MotorAction, MotorGoal, MotorResult, MotorFeedback
from std_msgs.msg import String

import actionlib

# construct the main node with the following features:
# service client, action client, console subscriber

class MainCenter:
    def __init__(self):
        rospy.init_node('main')
        
        ###### Setup NLP Service 
        rospy.loginfo('Main: Main is waiting for NLP service...')
        rospy.wait_for_service('nl_processing')     # wait service to be advertised     
        self.processor = rospy.ServiceProxy('nl_processing', NLP)           # Initialize service proxy
        rospy.loginfo('Main: NLP service is ready.')
        
       
        ###### Setup Motion Action Server
        rospy.loginfo('Main: Main is waiting for Motor action server...')
        # wait action server to be ready
        self.action_client = actionlib.SimpleActionClient('motor', MotorAction)
        self.action_client.wait_for_server()
        # Get the action client 
        rospy.loginfo('Main: Action service is ready.')
        
        
        ##### Setup Console Message Subscriber 
        ##### Construct subscriber for console input from console reader
        self.console_subscriber = rospy.Subscriber('console', String, self.callback_execute)

        
    # callback function for console message subscriber
    def callback_execute(self, msg):

        nlp_reponse = self.processor(msg.data)     
        
        # initialize goal for motor action server
        goal = MotorGoal()  
        goal.angle = nlp_reponse.angle  
        rospy.loginfo(msg.data + ' interpreted as' + str(goal.angle))
        
        self.action_client.send_goal(goal, feedback_cb=self.feedback_cb)
        
        ##! Uncomment this line to preempt the goal
        # client.cancel_goal()        
        
        self.action_client.wait_for_result()         # wait for action to complete and report result to log
        
        rospy.loginfo('')
        rospy.loginfo('[Report] State: %d'%(self.action_client.get_state()))
        rospy.loginfo('[Report] Status: %s' % (self.action_client.get_goal_status_text()))
        rospy.loginfo('[Report] Angle turned: %s' % (self.action_client.get_result().angle_done))
        rospy.loginfo('- - - - - - - - - - - - - - - - - - - - -' )

        
        
    # callback function of action server feedback
    def feedback_cb(self, feedback):
        rospy.loginfo('Angle left '+ str(feedback.angle_left) + ' degree.')

    def run(self):
        rospy.spin()


        
        

def main():
    center = MainCenter()
    center.run()

if __name__ == "__main__":
    main()







