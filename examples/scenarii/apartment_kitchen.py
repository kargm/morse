from morse.builder import *

# A PR2 robot to the scene
james = BasePR2()
james.add_interface('ros')
james.translate(x=-0.666, y=1.1464, z=0.0)
james.rotate(z=-5.776)

hans = Human()
hans.name = 'Human'
hans.translate(x=0.63, y=0.9)
hans.rotate(z=-3.0)

human_pose = Pose()
human_pose.name = 'Pose'
hans.append(human_pose)
human_pose.add_stream('ros', 'morse.middleware.ros.pose.OdometryPublisher')

#semantic_camera = SemanticCamera()
#semantic_camera.translate(x=0.086, y=0, z=1.265)
#semantic_camera.properties(noocclusion = True)
#semantic_camera.properties(cam_focal = 15)
#james.append(semantic_camera)
##semantic_camera.add_interface('ros', ['morse.middleware.ros_mw.ROSClass', 'post_lisp_code', 'morse/middleware/ros/semantic_camera'])
#semantic_camera.add_stream('ros', 'morse.middleware.ros.semantic_camera.SemanticCameraPublisherLisp')

#semantic_door_cam = SemanticDoorCamera()
#semantic_door_cam.translate(x=0.086, y=0, z=1.265)
#semantic_door_cam.properties(noocclusion = True)
#semantic_door_cam.properties(cam_focal = 15)
#james.append(semantic_door_cam)
#semantic_door_cam.add_stream('ros', 'morse.middleware.ros.semantic_door_camera.SemanticDoorCameraPublisherLisp')

semantic_objects_cam = SemanticCameraObjects();
semantic_objects_cam.translate(x=0.086, y=0, z=1.265)
semantic_objects_cam.properties(noocclusion = True)
semantic_objects_cam.properties(cam_focal = 15)
james.append(semantic_objects_cam)
semantic_objects_cam.add_stream('ros', 'morse.middleware.ros.semantic_camera.SemanticCameraPublisherLisp2')

semantic_doors_cam = SemanticCameraDoors();
semantic_doors_cam.translate(x=0.086, y=0, z=1.265)
semantic_doors_cam.properties(noocclusion = True)
semantic_doors_cam.properties(cam_focal = 15)
james.append(semantic_doors_cam)
semantic_doors_cam.add_stream('ros', 'morse.middleware.ros.semantic_door_camera.SemanticDoorCameraPublisherLisp')

semantic_drawers_cam = SemanticCameraDrawers();
semantic_drawers_cam.translate(x=0.086, y=0, z=1.265)
semantic_drawers_cam.properties(noocclusion = True)
semantic_drawers_cam.properties(cam_focal = 15)
james.append(semantic_drawers_cam)
semantic_drawers_cam.add_stream('ros', 'morse.middleware.ros.semantic_door_camera.SemanticDrawerCameraPublisherLisp')

motion = MotionXYW()
james.append(motion)
motion.add_interface('ros', topic='/cmd_vel')

l_gripper = Gripper()
l_gripper.translate(x=0.9918, y=-0.00246, z=0.742)
l_gripper.properties(Distance = 2)
l_gripper.properties(Angle = 60)
james.l_arm.append(l_gripper)
l_gripper.add_overlay('ros', 'morse.middleware.ros.overlays.gripper.Gripper')

r_gripper = Gripper()
r_gripper.translate(x=0.9918, y=0.00246, z=0.742)
james.r_arm.append(r_gripper)
r_gripper.properties(Distance = 2)
r_gripper.properties(Angle = 60)
r_gripper.add_overlay('ros', 'morse.middleware.ros.overlays.gripper.Gripper')

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

# add "actuators" to open doors and drawers
#~ door_control = DoorOpener()
#~ james.append(door_control)
#~ door_control.add_interface('ros')

# Keyboard control
keyboard = Keyboard()
keyboard.name = 'keyboard_control'
james.append(keyboard)

# Door opener
door_opener = DoorOpener()
james.append(door_opener)
door_opener.add_overlay('ros', 'morse.middleware.ros.overlays.open_doors.DoorOpener')

# Add passive objects
cornflakes = PassiveObject('props/kitchen_objects.blend', 'Cornflakes')
cornflakes.setgraspable()
cornflakes.translate(x=-1.6, y=2.7, z=1.06)

spoon = PassiveObject('props/kitchen_objects.blend', 'Spoon')
spoon.setgraspable()
spoon.translate(x=1.41, y=2.28, z=0.985)
spoon.rotate(z=-0.238)

#~ fork = PassiveObject('props/kitchen_objects.blend', 'Fork')
#~ fork.setgraspable()
#~ fork.translate(x=1.41, y=2.28, z=0.956)
#~ fork.rotate(z=-0.238)

#~ knife = PassiveObject('props/kitchen_objects.blend', 'Knife')
#~ knife.setgraspable()
#~ knife.translate(x=0.894, y=2.301, z=0.956)
#~ knife.rotate(z=1.45)
#~
#~ plate = PassiveObject('props/kitchen_objects.blend', 'Plate')
#~ plate.setgraspable()
#~ plate.translate(x=1.16, y=2.34, z=0.946)
#~ plate.rotate(z=1.45)

#bread = PassiveObject('props/kitchen_objects.blend', 'Bread')
#bread.setgraspable()
#bread.translate(x=0.5, y=1.97, z=0.86)
#bread.rotate(z=1.45)

bowl = PassiveObject('props/kitchen_objects.blend', 'Bowl')
bowl.setgraspable()
bowl.translate(x=1.383, y=2.651, z=0.98) #z=0.92)
bowl.rotate(z=1.45)

#~ jam = PassiveObject('props/kitchen_objects.blend', 'Jam')
#~ jam.setgraspable()
#~ jam.translate(x=0.619, y=2.4, z=0.96)
#~ jam.rotate(z=1.45)
#~
#~ nutella = PassiveObject('props/kitchen_objects.blend', 'Nutella')
#~ nutella.setgraspable()
#~ nutella.translate(x=0.704, y=2.52, z=0.902)
#~ nutella.rotate(z=1.45)

# Set scenario
env = Environment('apartment/apartment')
env.aim_camera([1.0470, 0, 0.7854])


