class Prototype:
    # used to register/unregister object and return registered object
    def __init__(self):
        self._objects = {}
    def register(self, name, obj):
        self._objects[name] = obj
    def unregister(self, name):
        del self._objects[name]
    def clone(self, name):
        return self._objects[name]

class MatchaCake:
    def flavor(self):
        return "Matcha"

cake = MatchaCake() # create an object
print(cake.flavor())
prototype = Prototype() # create a prototype
prototype.register('Matcha', cake) # register object
cake2 = prototype.clone('Matcha') # clone an object
print(cake2.flavor())
prototype.unregister('Matcha') # unregister an object
cake3 = prototype.clone('Matcha') # would return error 
