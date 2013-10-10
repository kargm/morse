import logging; logger = logging.getLogger("morse." + __name__)
from morse.core import blenderapi

import morse.sensors.camera
import morse.helpers.colors

from morse.helpers import passive_objects
from morse.helpers.components import add_data, add_property

class SemanticCameraGeneric(morse.sensors.camera.Camera):
    """
    This sensor emulates a hight level camera that outputs the names and
    properties of the objects that are located within the field of view of
    the camera. This sensor is a generic sensor that has to be specialized
    to track a specific type of object such as graspable objects or doors.

    The sensor determines first which objects are to be tracked. This has
    to be specified in the respective subclasses as well as the properties
    to be exported.

    Then a test is made to identify which of these objects are inside of
    the view frustum of the camera. Finally, a single visibility test is
    performed by casting a ray from the center of the camera to the
    center of the object. If anything other than the test object is
    found first by the ray, the object is considered to be occluded by
    something else, even if it is only the center that is being blocked.
    This last check is a bit costly and can be deactivated by setting the
    sensor property ``noocclusion`` to ``True``.

    The cameras make use of Blender's **bge.texture** module, which
    requires a graphic card capable of GLSL shading. Also, the 3D view
    window in Blender must be set to draw **Textured** objects.
    """

    _name = "Semantic camera generic"
    _short_desc = "A smart camera allowing to retrieve objects in its \
    field of view"

    add_data('visible_objects', [], 'list<objects>',
           "A list containing the different objects visible by the camera. \
            Each object is represented by a dictionary composed of: \n\
                - **name** (String): the name of the object \n\
                - **type** (String): the type of the object \n\
                - **position** (vec3<float>): the position of the \
                  object, in meter, in the blender frame       \n\
                - **orientation** (quaternion): the orientation of the \
                  object, in the blender frame")

    add_property('noocclusion', False, 'noocclusion', 'bool', 'Do not check for'
                 ' objects possibly hiding each others (faster but less '
                 'realistic behaviour)')

    def __init__(self, obj, parent=None):
        """ Constructor method.

        Receives the reference to the Blender object.
        The second parameter should be the name of the object's parent.
        """
        logger.info('%s initialization' % obj.name)
        # Call the constructor of the parent class
        super(SemanticCameraGeneric, self).__init__(obj, parent)

        # Locate the Blender camera object associated with this sensor
        main_obj = self.bge_object
        for cobj in main_obj.children:
            if hasattr(cobj, 'lens'):
                self.blender_cam = cobj
                logger.info("Camera object: {0}".format(self.blender_cam))
                break
        if not self.blender_cam:
            logger.error("no camera object associated to the semantic camera. \
                         The semantic camera requires a standard Blender  \
                         camera in its children.")
        # depending on the subclass store relevant objects in a dictionary and
        # initialize them with bounding box
        self.store_objects_to_track()

        if self.noocclusion:
            logger.info("Semantic camera running in 'no occlusion' mode (fast mode).")
        logger.info("Component initialized, runs at %.2f Hz ", self.frequency)

    def store_objects_to_track(self):
        logger.error("This method has to be specified in a non-generic semantic camera class.")

    def default_action(self):
        """ Do the actual semantic 'grab'.

        Iterate over all the tracked objects, and check if they are
        visible for the robot.  Visible objects must have a bounding box
        and be active for physical simulation (have the 'Actor' checkbox
        selected)
        """
        # Call the action of the parent class
        super(SemanticCameraGeneric, self).default_action()

        # Create dictionaries
        self.local_data['visible_objects'] = []
        for xobj in self.get_tracked_object_keys():
            if self._check_visible(xobj):
                # Create dictionary to contain object name, type,
                # description, position and orientation
                self.local_data['visible_objects'].append(self.get_obj_dict(xobj))

        logger.debug("Visible objects: %s" % self.local_data['visible_objects'])

    def get_obj_dict(self,obj):
      return {'name': passive_objects.label(obj),
              'description': obj.get('Description', ''),
              'type': obj.get('Type', '')}

    def _check_visible(self, obj):
        """ Check if an object lies inside of the camera frustum.

        The behaviour of this method is impacted by the sensor's
        property 'noocclusion': if true, only checks the object is in the
        frustum. Does not check it is actually visible (ie, not hidden
        away by another object).
        """
        # TrackedObjects was filled at initialization
        #  with the object's bounding boxes
        bb = self.get_tracked_objects(obj)
        pos = obj.position
        bbox = [[bb_corner[i] + pos[i] for i in range(3)] for bb_corner in bb]

        if logger.isEnabledFor(logging.DEBUG):
            logger.debug("\n--- NEW TEST ---")
            logger.debug("OBJECT '{0}' AT {1}".format(obj, pos))
            logger.debug("CAMERA '{0}' AT {1}".format(
                                    self.blender_cam, self.blender_cam.position))
            logger.debug("BBOX: >{0}<".format(bbox))
            logger.debug("BBOX: {0}".format(bb))

        # Translate the bounding box to the current object position
        #  and check if it is in the frustum
        if self.blender_cam.boxInsideFrustum(bbox) != self.blender_cam.OUTSIDE:

            if not self.noocclusion:
                # Check that there are no other objects between the camera
                # and the selected object
                # NOTE: This is a very simple test. Hiding only the 'center'
                # of an object will make it invisible, even if the rest is
                # still seen from the camera
                closest_obj = self.bge_object.rayCastTo(obj)
                if closest_obj in [obj] + list(obj.children):
                    return True
            else:
                return True

        return False

    def get_tracked_objects(self,obj):
        logger.error("This method has to be specified in a non-generic semantic camera class.")

    def get_tracked_object_keys(self):
        logger.error("This method has to be specified in a non-generic semantic camera class.")
