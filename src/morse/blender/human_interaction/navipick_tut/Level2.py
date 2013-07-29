from bge import logic

#co = logic.getCurrentController()
#collision = co.sensors['Collision']
objects = logic.getCurrentScene().objects
human = objects['Human']
cube = objects['Cube']

def place(): 
    human.worldPosition = (40, 0, 0)
    cube.worldPosition = (45, -6, 0)

def place2(): 
    human.worldPosition = (40, 0, 0)
