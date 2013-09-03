import logging; logger = logging.getLogger("morse." + __name__)
import json
import roslib; roslib.load_manifest('rospy'); roslib.load_manifest('std_msgs')
import rospy
from std_msgs.msg import String
from morse.middleware.ros import ROSPublisherTF
from morse.middleware.socket_datastream import MorseEncoder

class SemanticCameraPublisher(ROSPublisherTF):
    """ Publish the data of the semantic camera as JSON in a ROS String message.
    And send TF transform between '/map' and ``object.name``.
    """
    ros_class = String

    def default(self, ci='unused'):
        for obj in self.data['visible_objects']:
            # send tf-frame for every object
            self.sendTransform(obj['position'], obj['orientation'], \
                               rospy.Time.now(), str(obj['name']), "/map")
        string = String()
        string.data = json.dumps(self.data['visible_objects'], cls=MorseEncoder)
        self.publish(string)


class SemanticCameraPublisherLisp(ROSPublisherTF):
    """ Publish the data of the semantic camera as a ROS String message,
    that contains a lisp-list (each field are separated by a space).

    This function was designed for the use with CRAM and the Adapto group.
    """
    ros_class = String

    def default(self, ci='unused'):
        string = String()
        string.data = "("
        for obj in self.data['visible_objects']:
            description = obj['description'] or '-'

            # send tf-frame for every object
            self.sendTransform(obj['position'], obj['orientation'], \
                               rospy.Time.now(), str(obj['name']), "/map")

            # Build string from name, description, location and orientation in the global world frame
            string.data += "(" + str(obj['name']) + " " + description + " " + \
                           str(obj['position'].x) + " " + \
                           str(obj['position'].y) + " " + \
                           str(obj['position'].z) + " " + \
                           str(obj['orientation'].x) + " " + \
                           str(obj['orientation'].y) + " " + \
                           str(obj['orientation'].z) + " " + \
                           str(obj['orientation'].w) + ")"

        string.data += ")"
        self.publish(string)

class SemanticCameraPublisherLisp2(ROSPublisherTF):
    """ Publish the data of the semantic camera as a ROS String message,
    that contains a lisp-list (each field are separated by a space).

    This function was designed for the use with CRAM and the Adapto group.
    """
    ros_class = String

    def default(self, ci='unused'):
        string = String()
        string.data = "("
        for obj in self.data['visible_objects']:
            # if object has no description, set to nil
            if obj['description'] == '':
                description = 'nil'
            else:
                description = obj['description']
            # if object has no type, set to entity
            if obj['type'] == '':
                objtype = 'entity'
            else:
                objtype = obj['type']

            # send tf-frame for every object
            self.sendTransform(obj['position'], obj['orientation'], \
                               rospy.Time.now(), str(obj['name']), "/map")

            # Build string from name, description, location and orientation in the global world frame
            string.data += "(:name " + str(obj['name']) + \
                           " :type " + objtype + \
                           " :description " + description + \
                           " :pos-x " + str(obj['position'].x) + \
                           " :pos-y " + str(obj['position'].y) + \
                           " :pos-z " + str(obj['position'].z) + \
                           " :ori-x " + str(obj['orientation'].x) + \
                           " :ori-y " + str(obj['orientation'].y) + \
                           " :ori-z " + str(obj['orientation'].z) + \
                           " :ori-w " + str(obj['orientation'].w) + ")"

        string.data += ")"
        self.publish(string)
