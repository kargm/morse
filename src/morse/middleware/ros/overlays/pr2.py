from morse.middleware.ros_request_manager import ros_service, ros_action
from morse.core.overlay import MorseOverlay
from morse.core import status

import roslib; roslib.load_manifest('morsetesting')
import logging
from morsetesting.srv import *
from pr2_controllers_msgs.msg import *

class PR2(MorseOverlay):

    def __init__(self, overlaid_object):
        # Call the constructor of the parent class
        super(self.__class__,self).__init__(overlaid_object)
    
    @ros_service(type = GetHead)
    def get_head(self):
        #print("Head rotations: %s"%self.overlaid_object.get_rotations())
        return self.overlaid_object.get_rotations()
        
    @ros_service(type = GetTorso)
    def get_torso(self):
        # NOTE: We do NOT care about the IK limits here!
        return self.overlaid_object.get_translation("torso_lift")[1]
        
    @ros_service(type = SetTorso)
    def set_torso(self, height):
        if height >= 0 and height <= 0.311:
            self.overlaid_object.set_location("torso_lift", [0, height, 0])
            return True
        else: 
            print("Received invalid value: %s for PR2 torso. Torso height must be betweeen 0 and 0.31"%height)
            return False
        
    @ros_service(type = SetHead)
    def set_head(self, pan, tilt):
        #print("Setting head to: %s"%pan, tilt)
        self.overlaid_object.set_rotation("head_pan", [0, pan, 0])
        self.overlaid_object.set_rotation("head_tilt", [0, 0, tilt])
        return True
        
    @ros_service(type = TuckLeftArm)    
    def tuck_left_arm(self):
        #print("Channels are %s"%self.overlaid_object.get_channels())
        self.overlaid_object.set_rotation("l_shoulder_pan", [0, 0, -0.06024])
        self.overlaid_object.set_rotation("l_shoulder_lift", [-1.248526, 0, 0])
        self.overlaid_object.set_rotation("l_upper_arm", [0, 1.78907, 0])
        self.overlaid_object.set_rotation("l_elbow", [1.683386, 0, 0])
        self.overlaid_object.set_rotation("l_forearm", [0, 1.7343417, 0])
        self.overlaid_object.set_rotation("l_wrist_flex", [0.0962141, 0, 0])
        self.overlaid_object.set_rotation("l_wrist_roll", [0, 0.0864407, 0])
        return True
        
    @ros_service(type = TuckRightArm)    
    def tuck_right_arm(self):
        #print("Channels are %s"%self.overlaid_object.get_channels())
        self.overlaid_object.set_rotation("r_shoulder_pan", [0, 0, 0.023593])
        self.overlaid_object.set_rotation("r_shoulder_lift", [-1.1072800, 0, 0])
        self.overlaid_object.set_rotation("r_upper_arm", [0, 1.5566882, 0])
        self.overlaid_object.set_rotation("r_elbow", [-2.124408, 0, 0])
        self.overlaid_object.set_rotation("r_forearm", [0, 1.4175, 0])
        self.overlaid_object.set_rotation("r_wrist_flex", [1.8417, 0, 0])
        self.overlaid_object.set_rotation("r_wrist_roll", [0, -0.21436, 0])
        return True

    @ros_action(type = JointTrajectoryAction)
    def joint_trajectory_action(self, req):
        joint_name_modified = []
        more_modify_list = ['l_upper_arm_roll_joint','l_elbow_flex_joint','l_forearm_roll_joint','r_upper_arm_roll_joint','r_elbow_flex_joint','r_forearm_roll_joint']
        i = 0
        for joint_name, joint_position in zip(req.trajectory.joint_names, req.trajectory.points[0].positions):      
            # In joint_name do string modification and cut off "_joint" at the end of every name  
            print('trajectory.points.positions: %s'%str(joint_position))    
            joint_name_modified.append(joint_name.rsplit('_', 1)[0])	    
            if joint_name in more_modify_list:  
                joint_name_modified[i] = joint_name_modified[i].rsplit('_',1)[0]
            print('joint_name:%s'%joint_name)
            joint_position_tuple = ()<
            if joint_name_modified[i] == 'l_shoulder_pan' or joint_name_modified[i] == 'r_shoulder_pan':
                joint_position_tuple = (0.0, 0.0, joint_position)
            elif joint_name_modified[i] == 'l_shoulder_lift' or joint_name_modified[i] == 'r_shoulder_lift':
                joint_position_tuple = (joint_position, 0.0, 0.0)
            elif joint_name_modified[i] == 'l_upper_arm' or joint_name_modified[i] == 'r_upper_arm':
                joint_position_tuple = ( 0.0, joint_position,0.0)
            elif joint_name_modified[i] == 'l_elbow' or joint_name_modified[i] == 'r_elbow':
                joint_position_tuple = ( joint_position,0.0, 0.0)
            elif joint_name_modified[i] == 'l_forearm' or joint_name_modified[i] == 'r_forearm':
                joint_position_tuple = ( 0.0, joint_position,0.0)
            elif joint_name_modified[i] == 'l_wrist_flex' or joint_name_modified[i] == 'r_wrist_flex':
                joint_position_tuple = (joint_position, 0.0, 0.0)
            elif joint_name_modified[i] == 'l_wrist_roll' or joint_name_modified[i] == 'r_wrist_roll':
                joint_position_tuple = (0.0, joint_position, 0.0)
       	    self.overlaid_object.set_rotation(joint_name_modified[i], joint_position_tuple)
            i += 1


