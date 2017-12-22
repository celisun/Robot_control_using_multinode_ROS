import rospy
from turtlebot3_console_controller.srv import NLP, NLPResponse 	# note: NLP and NLPResponse classes generated automatically by running catkin_make


# Callback function for nlp service
# arg[string]: incoming service request received  
# return[float]: get angle to turn, such as 'turn 90' --> 90 
def find_angle(request):
	inp =  request.words.strip().split(' ')
	if(inp[0]=='turn'):
		return NLPResponse(float(inp[1]));
	return NLPResponse(0.0);



# initialize the server node with name
print('bringing up NLP server...')
rospy.init_node('nlp_server')

# Advertise service: name, type, callback
service = rospy.Service('nl_processing', NLP, find_angle)
print('NLP server is running.')

# Gives control of the node over to ROS, and waits for incoming service requests
rospy.spin()



