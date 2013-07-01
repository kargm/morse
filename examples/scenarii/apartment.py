from morse.builder import *

# A PR2 robot to the scene
james = BasePR2()
james.add_interface('ros')
james.translate(x=0, y=1, z=0.0)

hans = Human()

human_pose = Pose()
hans.append(human_pose)
human_pose.add_interface('ros')

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
robot_pose.add_interface('ros')

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
cornflakes.translate(x=0.5, y=1.67, z=0.9)

fork = PassiveObject('props/kitchen_objects.blend', 'Fork')
fork.setgraspable()
fork.translate(x=0.5, y=1.87, z=0.86)
fork.rotate(z=1.45)

knife = PassiveObject('props/kitchen_objects.blend', 'Knife')
knife.setgraspable()
knife.translate(x=0.5, y=1.97, z=0.86)
knife.rotate(z=1.45)

plate = PassiveObject('props/kitchen_objects.blend', 'Plate')
plate.setgraspable()
plate.translate(x=0.5, y=1.97, z=0.86)
plate.rotate(z=1.45)

#bread = PassiveObject('props/kitchen_objects.blend', 'Bread')
#bread.setgraspable()
#bread.translate(x=0.5, y=1.97, z=0.86)
#bread.rotate(z=1.45)

bowl = PassiveObject('props/kitchen_objects.blend', 'Bowl')
bowl.setgraspable()
bowl.translate(x=0.5, y=1.97, z=0.86)
bowl.rotate(z=1.45)

jam = PassiveObject('props/kitchen_objects.blend', 'Jam')
jam.setgraspable()
jam.translate(x=0.5, y=1.97, z=0.86)
jam.rotate(z=1.45)

nutella = PassiveObject('props/kitchen_objects.blend', 'Nutella')
nutella.setgraspable()
nutella.translate(x=0.5, y=1.97, z=0.86)
nutella.rotate(z=1.45)

# Set scenario
env = Environment('apartment/apartment')
env.aim_camera([1.0470, 0, 0.7854])



