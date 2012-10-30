from morse.builder.morsebuilder import *
from morse.builder.extensions.pr2extension import PR2


import roslib; roslib.load_manifest("morsetesting")
from morsetesting.msg import *

# http://www.openrobots.org/morse/doc/latest/user/tutorial.html

# Append b21 robot to the scene
bender = Robot('b21')
bender.translate(x=0, y=3, z=0.0)
bender.rotate(z=3.1415)

human = Human()
human.translate(x=-3, y=-0.3, z=0.0)
#human.rotate(z=-3.0)

Pose_sensor = Sensor('pose')
Pose_sensor.name = 'Pose_sensor'
bender.append(Pose_sensor)


Human_pose = Sensor('pose')
Human_pose.name = 'human_sensor'
human.append(Human_pose)

# Keyboard control
keyboard = Actuator('keyboard')
keyboard.name = 'keyboard_control'
bender.append(keyboard)

# Waypoint actuator
dest = Actuator('waypoint')
#dest.properties(Speed = 1.5)
#dest.properties(ObstacleAvoidance = False)
#dest.properties(tolerance = 1.5)

human.append(dest)

dest.configure_service('ros')
dest.configure_overlay('ros', 'morse.middleware.ros.overlays.actuator.WayPoint')

# Configuring the middlewares
Pose_sensor.configure_mw('ros')
Human_pose.configure_mw('ros')
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
env.aim_camera([1.0470, 0, 0.7854])



