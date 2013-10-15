import sys
sys.path.append('/work/kirsch/ros_fuerte_workspace/morse_ros/morse_msgs/src/morse_msgs/msg') # CHANGE THIS!!!
import logging; logger = logging.getLogger("morse." + __name__)
from morse.middleware.ros import ROSReader
from _OpenClose import OpenClose

class OpenDoorReader(ROSReader):
    ros_class = OpenClose

    def update(self, message):
        self.data["door"] = message.object
        self.data["goal_state"] = message.goal_open
        #~ logger.debug("%s door %s"%
                      #~ (if message.goal_open "Opening" else "Closing", message.object))
