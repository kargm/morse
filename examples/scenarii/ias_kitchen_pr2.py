from morse.builder import *

# A PR2 robot to the scene
james = BasePR2()
james.add_interface('ros')
james.translate(x=-3, y=2.7, z=0.0)

hans = Human()

human_pose = Pose()
hans.append(human_pose)
human_pose.add_interface('ros')

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

l_gripper = Gripper()
l_gripper.translate(x=0.9918, y=-0.00246, z=0.742)
james.l_arm.append(l_gripper)
l_gripper.add_overlay('ros', 'morse.middleware.ros.overlays.gripper.Gripper')

r_gripper = Gripper()
r_gripper.translate(x=0.9918, y=0.00246, z=0.742)
james.r_arm.append(r_gripper)



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
cornflakes.translate(x=1.37, y=0.5, z=0.9)
cornflakes.properties(Type='cereals')

fork = PassiveObject('props/kitchen_objects.blend', 'Fork')
fork.setgraspable()
fork.translate(x=1.38, y=0.5, z=0.86)
fork.rotate(z=1.45)
fork.properties(Type='fork')

knife = PassiveObject('props/kitchen_objects.blend', 'Knife')
knife.setgraspable()
knife.translate(x=1.39, y=0.5, z=0.86)
knife.rotate(z=1.45)
knife.properties(Type='knife')

plate = PassiveObject('props/kitchen_objects.blend', 'Plate')
plate.setgraspable()
plate.translate(x=-1.36, y=2.27, z=0.86)
plate.rotate(z=1.45)
plate.properties(Type='plate')

bowl = PassiveObject('props/kitchen_objects.blend', 'Bowl')
bowl.setgraspable()
bowl.translate(x=-1.38, y=2.30, z=0.86)
bowl.rotate(z=1.45)
bowl.properties(Type='bowl')

jam = PassiveObject('props/kitchen_objects.blend', 'Jam')
jam.setgraspable()
jam.translate(x=1.33, y=0.45, z=0.86)
jam.rotate(z=1.45)
jam.properties(Type='jam')

nutella = PassiveObject('props/kitchen_objects.blend', 'Nutella')
nutella.setgraspable()
nutella.translate(x=1.35, y=0.42, z=0.86)
nutella.rotate(z=1.45)
nutella.properties(Type='nutella')

# Set scenario
env = Environment('tum_kitchen/tum_kitchen')
env.aim_camera([1.0470, 0, 0.7854])
