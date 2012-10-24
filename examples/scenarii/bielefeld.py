from morse.builder.morsebuilder import *
from morse.builder.extensions.pr2extension import PR2

# http://www.openrobots.org/morse/doc/latest/user/tutorial.html

# Append b21 robot to the scene
bender = Robot('b21')
bender.translate(x=0, y=3, z=0.0)
bender.rotate(z=3.1415)

human = Human()
human.translate(x=-3, y=0.2, z=0.0)
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

# Configuring the middlewares
Pose_sensor.configure_mw('ros')

# Set scenario
env = Environment('bielefeld/bielefeld')
env.aim_camera([1.0470, 0, 0.7854])



