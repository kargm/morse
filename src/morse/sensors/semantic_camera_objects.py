import logging; logger = logging.getLogger("morse." + __name__)
from morse.core import blenderapi

import morse.sensors.camera
import morse.helpers.colors
import morse.sensors.semantic_camera_generic

from morse.helpers import passive_objects
from morse.helpers.components import add_data, add_property

class SemanticCameraObjects(morse.sensors.semantic_camera_generic.SemanticCameraGeneric):
    """
    This sensor is a special semantic camera that only returns objects.

    It tracks all objects (objects
    marked with a **Logic Property** called ``Object``, cf documentation
    on :doc:`passive objects <../others/passive_objects>` for more on
    that). If the ``Label`` property is defined, it is used as exported
    name. Else the Blender object name is used. If the ``Type`` property
    is set, it is exported as well.

    The cameras make use of Blender's **bge.texture** module, which
    requires a graphic card capable of GLSL shading. Also, the 3D view
    window in Blender must be set to draw **Textured** objects.
    """

#    def __init__(self, obj, parent=None):
#        """ Constructor method.
#
#        Receives the reference to the Blender object.
#        The second parameter should be the name of the object's parent.
#        """
#        logger.info('%s initialization' % obj.name)
#        # Call the constructor of the parent class
#        super(self.__class__, self).__init__(obj, parent)

    def store_objects_to_track(self):
        # TrackedObject is a dictionary containing the list of tracked objects
        # (->meshes with a class property set up) as keys
        #  and the bounding boxes of these objects as value.
        if not 'trackedObjects' in blenderapi.persistantstorage():
            logger.info('Initialization of tracked objects:')
            blenderapi.persistantstorage().trackedObjects = \
                            dict.fromkeys(passive_objects.active_objects())

            # Store the bounding box of the marked objects
            for obj in blenderapi.persistantstorage().trackedObjects.keys():

                # bound_box returns the bounding box in local space
                #  instead of world space.
                blenderapi.persistantstorage().trackedObjects[obj] = \
                                    blenderapi.objectdata(obj.name).bound_box

                details = passive_objects.details(obj)
                logger.info('    - {%s} (type:%s)'%
                            (details['label'], details['type']))


    def get_obj_dict(self,obj):
        return {'name': passive_objects.label(obj),
                'description': obj.get('Description', ''),
                'type': obj.get('Type', ''),
                'position': obj.worldPosition,
                'orientation': obj.worldOrientation.to_quaternion()}

    def get_tracked_objects(self,obj):
        return blenderapi.persistantstorage().trackedObjects[obj]

    def get_tracked_object_keys(self):
        return blenderapi.persistantstorage().trackedObjects.keys()

