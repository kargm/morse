import logging; logger = logging.getLogger("morse." + __name__)
import morse.core.actuator
from morse.core import blenderapi
from morse.helpers import passive_objects
from morse.helpers.components import add_data

class DoorOpener(morse.core.actuator.Actuator):
    add_data('door', None, 'string', "Name of door to be opened or closed")
    add_data('goal_state',True,'bool', "Goal state: true = open, false = closed")

    #scene= blenderapi.scene()
    #objects = scene.objects

#~ # load overlay_closed.tga and overlay_open.tga into the global dictionary
#~ if not "open" in  logic.globalDict:
    #~ TexName = "overlay_open.tga"
    #~ filepath = logic.expandPath(os.path.join(os.environ["MORSE_ROOT"], "share","morse","data","props",TexName))
    #~ logic.globalDict["open"] = loadtexture(filepath)
#~
#~ open_id = logic.globalDict.get("open")
#~
#~ if not "closed" in logic.globalDict:
    #~ TexName = "overlay_closed.tga"
    #~ filepath = os.path.join(os.environ["MORSE_ROOT"], "share","morse","data","props",TexName)
    #~ logic.globalDict["closed"] = loadtexture(filepath)
#~
#~ closed_id = logic.globalDict.get("closed")

    def identify_object(self):
        for obj in passive_objects.doors():
            print("OBJ is: %s, \nLabel is: %s"%(type(obj), type(blenderapi.persistantstorage().doorsDict[obj]['label'])))
            print("label --- local_data[door]: %s -- %s"%( blenderapi.persistantstorage().doorsDict[obj]['label'], self.local_data['door']))
            if blenderapi.persistantstorage().doorsDict[obj]['label'] == self.local_data['door']:
                return obj
            
    def open(self):
        # identify door to open
        door = self.identify_object()
        print("[open] door is %s, type: %s"%(door, type(door)))

        # open door if necessary
        if not door['Open']:     # opens the door
            if door['Door'].lower()=='right':
                door.applyRotation((0, 0, 1.4), False)
                # rotation around global Z-Axis - ~80 degrees
            elif door['Door'].lower()=='left':
                door.applyRotation((0, 0, -1.4), False)
        door['Open'] = True

    def close(self):
        # identify door to close
        door = self.identify_object()

        # close door if necessary
        if door['Open']:     # closes the door
            if door['Door'].lower()=='right':
                door.applyRotation((0, 0, -1.4), False)
                # rotation around global Z-Axis - ~80 degrees
            elif door['Door'].lower()=='left':
                door.applyRotation((0, 0, 1.4), False)
        door['Open'] = False

    def default_action(self):
        if self.local_data['goal_state']:
            self.open()
        else:
            self.close()

