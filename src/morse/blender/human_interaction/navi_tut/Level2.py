from morse.core import blenderapi

objects = blenderapi.scene().objects
print("O: %s"%objects)
human = objects['POS_EMPTY']
cube = objects['CubeSelect']

def place(): 
    human.worldPosition = (40, 0, 0)
    cube.worldPosition = (45, -6, 0)

def place2(): 
    human.worldPosition = (40, 0, 0)
