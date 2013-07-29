from bge import logic

#co = logic.getCurrentController()
#collision = co.sensors['Collision']
objects = logic.getCurrentScene().objects
human = objects['Human']


def place(): 
    human.worldPosition = (70, -8, 0)
    
