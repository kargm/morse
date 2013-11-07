import logging; logger = logging.getLogger("morse." + __name__)

from morse.core.services import interruptible
from morse.middleware.ros_request_manager import ros_action
from morse.core.overlay import MorseOverlay
from morse.core import status

from morse.middleware.ros.helpers import ros_add_to_syspath
ros_add_to_syspath("morse_msgs")
from morse_msgs.msg import *

class DoorOpener(MorseOverlay):

    def __init__(self, overlaid_object):
        # Call the constructor of the parent class
        super(self.__class__,self).__init__(overlaid_object)

    def door_opener_action_result(self, result):
        state, value = result

        logger.info("DoorOpener action completed! got value " + str(value))

        return (state, DoorOpenerResult())

    @interruptible
    @ros_action(type = DoorOpenerAction)
    def door_opener_action(self, req):

        if req.open:
            logger.info("Opening door")
            self.overlaid_object.local_data['door'] = req.door
            self.overlaid_object.open(self.chain_callback(self.door_opener_action_result))
        else:
            logger.info("Closing door")
            self.overlaid_object.local_data['door'] = req.door
            self.overlaid_object.close(self.chain_callback(self.door_opener_action_result))
