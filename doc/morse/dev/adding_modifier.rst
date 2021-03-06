Creating a modifier
===================

Creating a modifier is more or less the same than creating a sensor. There are
still two parts, the blender part and the python logic. For the blender part,
it is the same thing than for a sensor / actuator.

Python part 
-----------

There is no strict class hierarchy for modifiers, we rely on python duck
typing. We only expect than a modifier exposes a method ``register_component``,
similarly to middleware, with the following prototype : ::

  def register_component(self, component_name, component_instance, mod_data)

The method is responsible to add the right modifier specified in ``mod_data``
in the list of modifier of ``component_instance`` ( input_modifiers or
output_modifiers ). 

Modifier functions must have the prototype: ::

  def modifier_name(self, component_instance)

In your modifier function, you must only access to the array ``local_data``
of the component.

`GPS_noise.py <http://trac.laas.fr/git/morse/tree/src/morse/modifiers/gps_noise.py>`_ 
shows a simple example for a modifier.

