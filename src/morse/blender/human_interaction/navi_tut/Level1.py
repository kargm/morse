from morse.core import blenderapi

#co = logic.getCurrentController()
#collision = co.sensors['Collision']
objects = blenderapi.scene().objects
human = objects['Human']

def place(): 
    human.worldPosition = (0, 0, 0)
