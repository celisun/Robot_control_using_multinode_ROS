
## ROS Multinode Control
Exemplary code **[Autonomous Robotics Lab](http://campusrover.org.s3-website-us-west-2.amazonaws.com)** 

@ Celi Sun  @ Nov, 2017  @ Brandeis University

This is a practice to write multiple nodes communicating using the three major ROS functions: topic, action and service, to complete a simple task of asking-turtlebot-to-spin. The three nodes *nlp_server*, *console_reader* and *motor_action_server* are collaborating via the main, by reading the human user's inputs on condole, prcessing the reading and manipulating the turtlebot (to do the spinning to a certain degree) accordinly.

**Nodes:**

- **main**: the main coordinator, listens to console reader for user input, can invoke NLP service for input processing, and can send goals to action server for turtlebot mission 
- **console_reader**: read inputs from the user and publish through message to the Main node
- **nlp_server**: a simple NLP service node to take a string as input when invoked by the Main, e.g. "turn 361" and return an float e.g. "-1"
- **motor_action_server**: publish action mission to turtlebot about motor action to take, e.g. spin -90 degrees, and print out the feedback during the mission, such as the time consumed and angles left

**The strcuture of communication between nodes can be described as below:**

<img src="https://raw.githubusercontent.com/celisun/CourseExemplary_ROSConsoleController/master/multi-node_structure_sketch.png" width="650">

<img src="https://raw.githubusercontent.com/celisun/Human_robot_via_Multinode_ROS_/master/TB3-model.png" width="170">  

## Dependencies

* ros kinetics
* python


 
****
### Run this solution on your labtop
You can clone this repository from git to your own workspace by:
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/campusrover/CourseExemplary_RosConsoleController.git
```
Go back to catkin_ws and build the packages in the workspace by running catkin_make command:
```
$ cd ..
$ catkin_make
```
Now you can run the solution by launch file:
```
$ roslaunch CourseExemplary_RosConsoleController bringup.launch
```
If launched successfully, you will see the line "What do you want the robot to do?",

now type in command to activate the console reader. For example:
```
What do you want the robot to do?
$ turn 90
```
Now just sit tight and watch the turtlebot while getting feedbacks during the action!
