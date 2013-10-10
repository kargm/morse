import logging; logger = logging.getLogger("morse." + __name__)
from morse.core import blenderapi

import morse.sensors.camera
import morse.helpers.colors
import morse.sensors.semantic_camera_generic

from morse.helpers import passive_objects
from morse.helpers.components import add_data, add_property

class SemanticCameraDrawers(morse.sensors.semantic_camera_generic.SemanticCameraGeneric):
    """
    This sensor is a special semantic camera that only returns drawers and their state (open/closed).

    It tracks all drawers (objects
    marked with a **Logic Property** called ``Drawer``, cf documentation
    on :doc:`passive objects <../others/passive_objects>` for more on
    that). If the ``Label`` property is defined, it is used as exported
    name. Else the Blender object name is used. If the ``Type`` property
    is set, it is exported as well.

    The cameras make use of Blender's **bge.texture** module, which
    requires a graphic card capable of GLSL shading. Also, the 3D view
    window in Blender must be set to draw **Textured** objects.
    """


    def store_objects_to_track(self):
        # TrackedDrawers is a dictionary containing the list of tracked drawers
        # (->meshes with a class property set up) as keys
        #  and the bounding boxes of these objects as value.
        if not 'trackedDrawers' in blenderapi.persistantstorage():
            logger.info('Initialization of tracked drawers:')
            blenderapi.persistantstorage().trackedDrawers = \
                            dict.fromkeys(passive_objects.drawers())

            # Store the bounding box of the marked objects
            for obj in blenderapi.persistantstorage().trackedDrawers.keys():

                # bound_box returns the bounding box in local space
                #  instead of world space.
                blenderapi.persistantstorage().trackedDrawers[obj] = \
                                    blenderapi.objectdata(obj.name).bound_box

                details = blenderapi.persistantstorage().drawersDict[obj]
                logger.info('    - {%s} '%
                            (details['label']))


    def get_obj_dict(self,obj):
        # Create dictionaries
        return {'name': passive_objects.label(obj),
                'description': obj.get('Description', ''),
                'open': obj.get('Open', '')}


    def get_tracked_objects(self,obj):
        return blenderapi.persistantstorage().trackedDrawers[obj]

    def get_tracked_object_keys(self):
        return blenderapi.persistantstorage().trackedDrawers.keys()

