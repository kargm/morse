import logging; logger = logging.getLogger("morse." + __name__)

from morse.core.services import interruptible
from morse.middleware.ros_request_manager import ros_action
from morse.core.overlay import MorseOverlay
from morse.core import status

from morse.middleware.ros.helpers import ros_add_to_syspath
ros_add_to_syspath("morse_msgs")
from morse_msgs.msg import *

class Gripper(MorseOverlay):

    def __init__(self, overlaid_object):
        # Call the constructor of the parent class
        super(self.__class__,self).__init__(overlaid_object)

    def gripper_action_result(self, result):
        return (result)

    @interruptible
    @ros_action(type = GripperAction)
    def gripper_action(self, req):

        if req.grasp:
            logger.info("Grasping nearest object")
            self.overlaid_object.grab(self.chain_callback(self.gripper_action_result))
        else:
            logger.info("Releasing object")
            self.overlaid_object.release(self.chain_callback(self.gripper_action_result))

