from morse.builder import *

# A PR2 robot to the scene
james = BasePR2()
james.add_interface('ros')

motion = MotionXYW()
james.append(motion)
motion.add_interface('ros', topic='/cmd_vel')

# An odometry sensor to get odometry information
odometry = Odometry()
james.append(odometry)
odometry.add_interface('ros', topic="/odom")

robot_pose = Pose()
robot_pose.name = 'robot_pose'
james.append(robot_pose)
robot_pose.add_stream('ros', 'morse.middleware.ros.pose.OdometryPublisher')

scan = Hokuyo()
scan.translate(x=0.275, z=0.252)
james.append(scan)
scan.properties(Visible_arc = False)
scan.properties(laser_range = 30.0)
scan.properties(resolution = 1.0)
scan.properties(scan_window = 180.0)
scan.create_laser_arc()

scan.add_interface('ros', topic='/base_scan')

# Keyboard control
keyboard = Keyboard()
keyboard.name = 'keyboard_control'
james.append(keyboard)

# Set scenario
env = Environment('indoors-1/indoor-1-adapto')
env.aim_camera([1.0470, 0, 0.7854])
