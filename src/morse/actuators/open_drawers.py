import logging; logger = logging.getLogger("morse." + __name__)
import morse.core.actuator
from morse.core import status, blenderapi
from morse.helpers import passive_objects
from morse.helpers.components import add_data
from morse.core.services import service, async_service, interruptible

logger.setLevel(logging.DEBUG)

class DrawerOpener(morse.core.actuator.Actuator):
    """
    Actuator for opening drawers by ``remote control''. I provides services
    open and close. It just plays the respective animation in blender and
    sets the status
    """

    _name = "DrawerOpener"
    _short_desc = "Open drawers by remote control"

    add_data('drawer', None, 'string', "Name of drawer to be opened or closed")
    #~ add_data('goal_state',True,'bool', "Goal state: true = open, false = closed")


    def identify_object(self):
        for obj in passive_objects.drawers():
            logger.info("OBJ is: %s, \nLabel is: %s"%(type(obj), type(blenderapi.persistantstorage().drawersDict[obj]['label'])))
            logger.info("label --- local_data[drawer]: %s -- %s"%( blenderapi.persistantstorage().drawersDict[obj]['label'], self.local_data['drawer']))
            if blenderapi.persistantstorage().drawersDict[obj]['label'] == self.local_data['drawer']:
                return obj

    @interruptible
    @async_service
    def open(self):
        # identify drawer to open
        drawer = self.identify_object()
        logger.debug("[open] drawer is %s, type: %s"%(drawer, type(drawer)))

        if drawer:
            # open drawer if necessary
            if not drawer['Open']:     # opens the drawer
                drawer.sensors['Open'].value='True'
            drawer['Open'] = True
            open_status = "Opened drawer: '%s'"%self.local_data['drawer']
            self.completed(status.SUCCESS, open_status)
            return drawer.name
        else:
            open_status = "Did not find drawer: '%s'"%self.local_data['drawer']
            self.completed(status.FAILED, open_status)

    @interruptible
    @async_service
    def close(self):
        # identify drawer to open
        drawer = self.identify_object()
        logger.debug("[open] drawer is %s, type: %s"%(drawer, type(drawer)))

        if drawer:
            # open drawer if necessary
            if drawer['Open']:     # opens the drawer
                drawer.sensors['Close'].value='False'
            drawer['Open'] = False
            open_status = "Closed drawer: '%s'"%self.local_data['drawer']
            self.completed(status.SUCCESS, open_status)
            return drawer.name
        else:
            open_status = "Did not find drawer: '%s'"%self.local_data['drawer']
            self.completed(status.FAILED, open_status)

