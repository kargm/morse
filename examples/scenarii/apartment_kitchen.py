from morse.builder import *

# A PR2 robot to the scene
james = BasePR2()
james.add_interface('ros')
james.translate(x=-0.666, y=1.1464, z=0.0)
james.rotate(z=-5.776)

hans = Human()
hans.name = 'Human'
hans.translate(x=1.74, y=-4.5)

human_pose = Pose()
human_pose.name = 'Pose'
hans.append(human_pose)
human_pose.add_stream('ros', 'morse.middleware.ros.pose.OdometryPublisher')

semantic_camera = SemanticCamera()
semantic_camera.translate(x=0.086, y=0, z=1.265)
semantic_camera.properties(noocclusion = True)
semantic_camera.properties(cam_focal = 15)
james.append(semantic_camera)
#semantic_camera.add_interface('ros', ['morse.middleware.ros_mw.ROSClass', 'post_lisp_code', 'morse/middleware/ros/semantic_camera'])
semantic_camera.add_stream('ros', 'morse.middleware.ros.semantic_camera.SemanticCameraPublisherLisp')

semantic_door_cam = SemanticDoorCamera()
semantic_door_cam.translate(x=0.086, y=0, z=1.265)
semantic_door_cam.properties(noocclusion = True)
semantic_door_cam.properties(cam_focal = 15)
james.append(semantic_door_cam)
semantic_door_cam.add_stream('ros', 'morse.middleware.ros.semantic_door_camera.SemanticDoorCameraPublisherLisp')

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
cornflakes.translate(x=0.919, y=2.7, z=1.10)

fork = PassiveObject('props/kitchen_objects.blend', 'Fork')
fork.setgraspable()
fork.translate(x=1.41, y=2.28, z=0.956)
fork.rotate(z=-0.238)

knife = PassiveObject('props/kitchen_objects.blend', 'Knife')
knife.setgraspable()
knife.translate(x=0.894, y=2.301, z=0.956)
knife.rotate(z=1.45)

plate = PassiveObject('props/kitchen_objects.blend', 'Plate')
plate.setgraspable()
plate.translate(x=1.16, y=2.34, z=0.946)
plate.rotate(z=1.45)

#bread = PassiveObject('props/kitchen_objects.blend', 'Bread')
#bread.setgraspable()
#bread.translate(x=0.5, y=1.97, z=0.86)
#bread.rotate(z=1.45)

bowl = PassiveObject('props/kitchen_objects.blend', 'Bowl')
bowl.setgraspable()
bowl.translate(x=1.383, y=2.651, z=0.92)
bowl.rotate(z=1.45)

jam = PassiveObject('props/kitchen_objects.blend', 'Jam')
jam.setgraspable()
jam.translate(x=0.619, y=2.4, z=0.96)
jam.rotate(z=1.45)

nutella = PassiveObject('props/kitchen_objects.blend', 'Nutella')
nutella.setgraspable()
nutella.translate(x=0.704, y=2.52, z=0.902)
nutella.rotate(z=1.45)

# Set scenario
env = Environment('apartment/apartment')
env.aim_camera([1.0470, 0, 0.7854])



