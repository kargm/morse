from morse.core import blenderapi

#co = logic.getCurrentController()
#collision = co.sensors['Collision']
objects = blenderapi.scene().objects
human = objects['POS_EMPTY']


def place(): 
    human.worldPosition = (70, -8, 0)
    
