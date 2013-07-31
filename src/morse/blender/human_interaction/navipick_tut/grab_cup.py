from morse.core import blenderapi

co = blenderapi.controller()
ow = co.owner

objects = blenderapi.scene().objects
objects['Tut_Script_Holder']

def test():
    if ow.parent and scriptHolder['Level'] == 4:
        if not 'init' in ow:
            ow['init'] = True
            scriptHolder['Level'] = 5
        
            
