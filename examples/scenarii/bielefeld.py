from morse.builder.morsebuilder import *
from morse.builder.extensions.pr2extension import PR2


import roslib; roslib.load_manifest("morsetesting")
from morsetesting.msg import *

# http://www.openrobots.org/morse/doc/latest/user/tutorial.html

# For Fake-Laser
sub = Robot('submarine')
sub.translate(x=10, y=0, z=-10.0)
Sick = Sensor('sick')
Sick.translate(x=0.275, z=0.252)
sub.append(Sick)
Sick.properties(Visible_arc = False)
Sick.properties(laser_range = 30.0000)
Sick.properties(resolution = 1.0000)
Sick.properties(scan_window = 180.0000)

# Append b21 robot to the scene
bender = Robot('jido')
bender.translate(x=0, y=3, z=0.0)
bender.rotate(z=3.1415)

human = Human()
human.translate(x=-3, y=-0.3, z=0.0)
#human.rotate(z=-3.0)
human.use_world_camera()

Pose_sensor = Sensor('pose')
Pose_sensor.name = 'Robot_pose'
bender.append(Pose_sensor)

Human_pose = Sensor('pose')
Human_pose.name = 'Human_pose'
human.append(Human_pose)

Odometry = Sensor('odometry')
human.append(Odometry)

# Keyboard control
keyboard = Actuator('keyboard')
keyboard.name = 'keyboard_control'
bender.append(keyboard)

# Waypoint actuator
dest = Actuator('xy_omega')
#dest.properties(Speed = 1.5)
#dest.properties(ObstacleAvoidance = False)
#dest.properties(tolerance = 1.5)

human.append(dest)

#dest.configure_service('ros')
#dest.configure_overlay('ros', 'morse.middleware.ros.overlays.actuator.WayPoint')

# Configuring the middlewares
#Pose_sensor.configure_mw('ros')
Human_pose.configure_mw('ros')
dest.configure_mw('ros')
Odometry.configure_mw('ros')
Sick.configure_mw('ros')

#dest.configure_mw('ros', ['morse.middleware.ros_mw.ROSClass', 'read_waypoint', 'morse/middleware/ros/waypoint2D'])

# Furniture
cb1 = PassiveObject('props/furnitures.blend', 'IKEA_cupboard_BILLY_1')
cb1.translate(x=2.5, y=2.4)
cb1.rotate(z=-1.571)
cb2 = PassiveObject('props/furnitures.blend', 'IKEA_cupboard_BILLY_1')
cb2.rotate(z=-1.571)
cb2.translate(x=2.5, y=-0.3)
cb3 = PassiveObject('props/furnitures.blend', 'IKEA_cupboard_BILLY_1')
cb3.rotate(z=-1.571)
cb3.translate(x=2.5, y=-3)
cb4 = PassiveObject('props/furnitures.blend', 'IKEA_cupboard_BILLY_1')
cb4.translate(y=3.8)
cb4.setgraspable()

# Set scenario
env = Environment('bielefeld/bielefeld')
env.place_camera([-3.1033, -4.9475, 1.6817])
env.aim_camera([1.2, -0.001613, -0.686])
#env.set_stereo('STEREO')


