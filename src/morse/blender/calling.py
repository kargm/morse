import GameLogic

""" Generic Python Module to be called by all MORSE components.
    It will locate the calling object in the dictionary,
    retrieve the stored instance and call its 'action' method. """

def robot_action(contr):
    """ Call the 'action' method of the correct robot. """
    # Do nothing if morse has not been properly initialised
    try:
        if not GameLogic.morse_initialised:
            return
    except AttributeError as detail:
        return
    
    # Execute only when the sensor is really activated
    if contr.sensors[0].positive:
        obj = contr.owner

        # Get the intance of this objects class
        robot_object = GameLogic.robotDict[obj]
        if robot_object:
            robot_object.action()


def sensor_action(contr):
    """ Call the 'action' method of the correct sensor. """
    # Do nothing if morse has not been properly initialised
    try:
        if not GameLogic.morse_initialised:
            return
    except AttributeError as detail:
        return

    # Execute only when the sensor is really activated
    if contr.sensors[0].positive:
        obj = contr.owner
        
        # Get the intance of this objects class
        sensor_object = GameLogic.componentDict[obj.name]
        if sensor_object:
            sensor_object.action()


def actuator_action(contr):
    """ Call the 'action' method of the correct actuator. """
    # Do nothing if morse has not been properly initialised
    try:
        if not GameLogic.morse_initialised:
            return
    except AttributeError as detail:
        return
    
    # Execute only when the sensor is really activated
    if contr.sensors[0].positive:
        obj = contr.owner

        # Get the instance of this objects class
        actuator_object = GameLogic.componentDict[obj.name]
        if actuator_object:
            actuator_object.action()


def mw_action(contr):
    """ Call the 'action' method of the correct middleware. """
    # TODO: Right now there is nothing the mw should do, so just exit
    return

    #obj = contr.owner
    
    # Get the intance of this objects class
    #mw_object = GameLogic.componentDict[obj.name]
    #mw_object.action()
