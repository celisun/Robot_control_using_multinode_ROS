import rospy
from std_msgs.msg import String
import sys

# Initiailze node
rospy.init_node('console_reader')

# Initialize publisher, publish msg to topic 'console',
# channel used to talk to main 
publisher = rospy.Publisher('console', String, queue_size=1)

# Keep reading from terminal  
while True:
	cmd = raw_input('What do you want the robot to do?  ')
	if cmd == 'exit':
		print('Shutting down...')
		break
		
	# publish message
	publisher.publish(cmd)
