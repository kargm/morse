import logging; logger = logging.getLogger("morse." + __name__)
import morse.core.actuator
from morse.core import status, blenderapi
from morse.helpers import passive_objects
from morse.helpers.components import add_data
from morse.core.services import service, async_service, interruptible


class DoorOpener(morse.core.actuator.Actuator):
    """
    Actuator for opening doors by ``remote control''. I provides services
    open and close.

    .. note::

        This actuator only opens the door without playing any animation. This
        could easily be added when a blender animation is set.
    """

    _name = "DoorOpener"
    _short_desc = "Open doors by remote control"

    add_data('door', None, 'string', "Name of door to be opened or closed")
    add_data('goal_state',True,'bool', "Goal state: true = open, false = closed")


    def identify_object(self):
        for obj in passive_objects.doors():
            logger.info("OBJ is: %s, \nLabel is: %s"%(type(obj), type(blenderapi.persistantstorage().doorsDict[obj]['label'])))
            logger.info("label --- local_data[door]: %s -- %s"%( blenderapi.persistantstorage().doorsDict[obj]['label'], self.local_data['door']))
            if blenderapi.persistantstorage().doorsDict[obj]['label'] == self.local_data['door']:
                return obj

    @interruptible
    @async_service
    def open(self):
        # identify door to open
        door = self.identify_object()

        if door:
            # open door if necessary
            if not door['Open']:     # opens the door
                if door['Door'].lower()=='right':
                    door.applyRotation((0, 0, 1.4), False)
                    # rotation around global Z-Axis - ~80 degrees
                elif door['Door'].lower()=='left':
                    door.applyRotation((0, 0, -1.4), False)
                elif door['Door'].lower()=='bottom-x':
                    door.applyRotation((1.4, 0, 0), False)
                elif door['Door'].lower()=='bottom-y':
                    door.applyRotation((0, 1.4, 0), False)
            door['Open'] = True
            open_status = "Opened door: '%s'"%self.local_data['door']
            self.completed(status.SUCCESS, open_status)
            return door.name
        else:
            open_status = "Did not find door: '%s'"%self.local_data['door']
            self.completed(status.FAILED, open_status)

    @interruptible
    @async_service
    def close(self):
        # identify door to close
        door = self.identify_object()

        if door:
            # close door if necessary
            if door['Open']:     # closes the door
                if door['Door'].lower()=='right':
                    door.applyRotation((0, 0, -1.4), False)
                    # rotation around global Z-Axis - ~80 degrees
                elif door['Door'].lower()=='left':
                    door.applyRotation((0, 0, 1.4), False)
                elif door['Door'].lower()=='bottom-x':
                    door.applyRotation((-1.4, 0, 0), False)
                elif door['Door'].lower()=='bottom-y':
                    door.applyRotation((0, -1.4, 0), False)
            door['Open'] = False
            close_status = "Closed door: '%s'"%self.local_data['door']
            self.completed(status.SUCCESS, close_status)
            return door.name
        else:
            close_status = "Did not find door: '%s'"%self.local_data['door']
            self.completed(status.FAILED, close_status)



