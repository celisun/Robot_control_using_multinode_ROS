#!/usr/bin/env python

import rospy
import math
import time
import actionlib
from geometry_msgs.msg import Twist 
from turtlebot3_console_controller.msg import MotorAction, MotorGoal, MotorResult, MotorFeedback

# Initialize node 
rospy.init_node ('motor_action_server')  

# Initialize publisher, publish msg to control turtlebot
cmd_vel_pub = rospy.Publisher("/cmd_vel_mux/input/teleop", Twist, queue_size=1)  


# Callback function for action server 
def do_action(goal):
    angle_rad = math.radians((math.fabs(goal.angle))%360);  # angle mod 360 to range [0,360] and convert degree to radian
    angular_turn_speed= 1.5      # Note: ROS using international standard unit, so 
    update_time = 0.1            # angular speed: rad/s

    print("Motion action server got a new goal, turn "+str(goal.angle))
    
    start_time = time.time()
    goal_time = abs(angle_rad)/angular_turn_speed       # Calculate time estimated when finish the goal ( the turn)
    
    if goal.angle<0:
        angular_turn_speed=-angular_turn_speed           
    
    ## Build twist message 
    undates_count = 0
    twist_msg = Twist()
    twist_msg.angular.z = angular_turn_speed    
    
    
    while (time.time() - start_time) < goal_time:
        
         ## Handle Preemption: 
         #  fill in a result and provide a status string
        if server.is_preempt_requested():
            result = MotorResult()
            result.updates_n = undates_count
            result.angle_done = math.degrees((time.time()-start_time)*math.fabs(angular_turn_speed))
            text = "Other process preempted the current one. goal.angle is "+str(goal.angle)
            server.set_preempted(result,text)
            return
            
        ## Report Feedback 
        # Initialize a feedback
        feedback = MotorFeedback()
        
        angle_turned = (time.time()-start_time)*math.fabs(angular_turn_speed)   # Calculate angle turned
        feedback.angle_left = math.degrees(angle_rad-angle_turned)              # Calculate angle left to turn       
        
        server.publish_feedback (feedback) # Send feedbacks
        ###########################
        
        # Publish the twist msg to control turtlebot 
        cmd_vel_pub.publish(twist_msg)
    
        
        if (goal_time - (time.time()-start_time)) < update_time:        #Sleep for a while
            time.sleep(goal_time - (time.time()-start_time))
        else:
            time.sleep(update_time)
        undates_count += 1
        
        
    ## Action Mission Complete
    ## Report Result
    # initialize and set result
    cmd_vel_pub.publish(Twist())  # Stop turtlebot
    result = MotorResult()
    result.angle_done = math.degrees(angle_rad)
    server.set_succeeded(result, "Mission Complete.")    #result. --> server.
    
   

server = actionlib.SimpleActionServer ('motor', MotorAction, do_action, False)
server.start()

rospy.spin()









