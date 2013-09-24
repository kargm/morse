from morse.builder import *

# A PR2 robot to the scene
james = BasePR2()
james.add_interface('ros')
james.translate(x=1.343, y=-1.5, z=0.0)

hans = Human()
human_pose = Pose()
hans.append(human_pose)
human_pose.add_interface('ros')
hans.translate(x=0.223, y=-2.417, z=0.0)

semantic_camera = SemanticCamera()
semantic_camera.translate(x=0.086, y=0, z=1.265)
james.append(semantic_camera)
#semantic_camera.add_interface('ros', ['morse.middleware.ros_mw.ROSClass', 'post_lisp_code', 'morse/middleware/ros/semantic_camera'])
#semantic_camera.add_interface('ros')
semantic_camera.add_stream('ros','morse.middleware.ros.semantic_camera.SemanticCameraPublisherLisp2')

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
env = Environment('adapto_kitchens/mueller_kitchen')
env.aim_camera([1.0470, 0, 0.7854])
