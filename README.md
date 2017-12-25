
## ROS Console Controller
This is a practice of writing multiple nodes with communicates via main using three ROS techniques: topic, action and service. The three nodes are defined as 'nlp_server', 'console_reader' and 'motor_action_server'.

- **'console_reader'**: read inputs from the user and publish through message to the Main 
- **'nlp_server'**: a simple NLP service to take a string as input, e.g. "turn 361" and return an float after string processing, e.g. "-1"
- **'motor_action_server'**: publish messages to turtlebot about motor action to take, e.g. spin -90 degrees

<img src="https://raw.githubusercontent.com/celisun/CourseExemplary_ROSConsoleController/master/multi-node_structure_sketch.png" width="650">

  


### Run this solution on your own labtop
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
