from morse.builder import *

# A PR2 robot to the scene
james = BasePR2()
james.add_interface('ros')
james.translate(x=-0.652, y=2.47, z=0.0)
james.rotate(z=-1.412)

hans = Human()
hans.name = 'Human'
hans.translate(x=1.74, y=-4.5)

human_pose = Pose()
human_pose.name = 'Pose'
hans.append(human_pose)
human_pose.add_stream('ros', 'morse.middleware.ros.pose.OdometryPublisher')

semantic_camera = SemanticCamera()
semantic_camera.translate(x=0.086, y=0, z=1.265)
james.append(semantic_camera)
#semantic_camera.add_interface('ros', ['morse.middleware.ros_mw.ROSClass', 'post_lisp_code', 'morse/middleware/ros/semantic_camera'])
semantic_camera.add_interface('ros')

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

# Add passive objects
cornflakes = PassiveObject('props/kitchen_objects.blend', 'Cornflakes')
cornflakes.setgraspable()
cornflakes.translate(x=-3.7, y=0.263, z=1.08)

fork = PassiveObject('props/kitchen_objects.blend', 'Fork')
fork.setgraspable()
fork.translate(x=-3.3, y=1.11, z=0.956)
fork.rotate(z=1.45)

knife = PassiveObject('props/kitchen_objects.blend', 'Knife')
knife.setgraspable()
knife.translate(x=-3.3, y=1.21, z=0.956)
knife.rotate(z=1.45)

plate = PassiveObject('props/kitchen_objects.blend', 'Plate')
plate.setgraspable()
plate.translate(x=-3.52, y=0.712, z=0.94)
plate.rotate(z=1.45)

#bread = PassiveObject('props/kitchen_objects.blend', 'Bread')
#bread.setgraspable()
#bread.translate(x=0.5, y=1.97, z=0.86)
#bread.rotate(z=1.45)

bowl = PassiveObject('props/kitchen_objects.blend', 'Bowl')
bowl.setgraspable()
bowl.translate(x=-3.642, y=1.11, z=0.92)
bowl.rotate(z=1.45)

jam = PassiveObject('props/kitchen_objects.blend', 'Jam')
jam.setgraspable()
jam.translate(x=-3.51, y=0.26, z=0.96)
jam.rotate(z=1.45)

nutella = PassiveObject('props/kitchen_objects.blend', 'Nutella')
nutella.setgraspable()
nutella.translate(x=-3.3, y=0.44, z=0.902)
nutella.rotate(z=1.45)

# Set scenario
env = Environment('apartment/apartment')
env.aim_camera([1.0470, 0, 0.7854])



