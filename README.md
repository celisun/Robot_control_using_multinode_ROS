
## Ros Console Controller
This is a practice of writing multiple nodes with communicates via main using three ROS techniques: topic, action and service. Our three nodes are nlp_server, console_reader and motor_action_server.


  'nlp_server' <---- service --->   main   <--- topic --->  'console_reader'

                                           <----action- --> 'motion_action_server'
                                    

  


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
