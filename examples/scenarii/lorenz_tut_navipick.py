from morse.builder import *

# Append humans to the scene
# Human to be controlled by subject (Human)
human = Human()
human.translate(x=-1.35, y=-2.6, z=0.0)
human.rotate(z=7.91)

humans_pose = Sensor('pose')
humans_pose.name = 'pose_subject'
humans_pose.frequency(10.0)
human.append(humans_pose)

# Keyboard control
keyboard = Actuator('keyboard')
keyboard.name = 'keyboard_control'
human.append(keyboard)

#cup1 = PassiveObject('props/kitchen_objects.blend', 'Cup_Blue')
#cup1.setgraspable()
#cup1.translate(x=43, y=7, z=1.07)
#cup1.rotate(z=0.1)


# Interferer human (Human.001)
# human = Human()
# human.translate(x=0.7, y=-0.46, z=0.0)
# human.rotate(z=-3.0)

# humani_pose = Sensor('pose')
# humani_pose.name = 'pose_interferer'
# human.append(humani_pose)

# Just one of the humans should be controllable via keyboard
# http://www.openrobots.org/morse/doc/latest/user/others/human.html
# human.disable_keyboard_control()

# creates a new instance of the actuator
# waypoint_interferer = Actuator('waypoint')
# waypoint_interferer.name = 'waypoint_interferer'

# place your component at the correct location
# waypoint_interferer.translate(x=0.7, y=-0.46, z=0.0)
# waypoint_interferer.rotate(z=-3.0)

# human.append(waypoint_interferer)

# creates a new instance of the actuator
# destination = Destination()
# destination_interferer = Actuator('destination')
# destination_interferer.name = 'destination_interferer'

# place your component at the correct location
# destination_interferer.translate(x=0.7, y=-0.46, z=0.0)
# destination_interferer.rotate(z=-3.0)

# human.append(destination_interferer)

# Configuring the middlewares
# humani_pose.configure_mw('ros')
humans_pose.configure_mw('ros')
# waypoint_interferer.configure_mw('socket')
# destination_interferer.configure_mw('ros')

# Set scenario
env = Environment('lorenz/navipick')
env.aim_camera([1.0470, 0, 0.7854])
