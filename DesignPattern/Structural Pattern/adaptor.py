class MatchaCake:
    def __init__(self):
        self.name = 'MatchaCake'

    def matcha_cake_flavor(self):
        return 'Matcha'

class BlackforestCake:
    def blackforest_cake_flavor(self):
        return "Chocolate and cherry"

class Adaptor:
    """adaptor class that translate method"""
    def __init__(self, object, **kwargs):
        self.obj = object
        self.__dict__.update(**kwargs)
    def __getattr__(self, attr):
        """
        Called when an attribute lookup has not found the attribute in the usual places 
        (i.e. it is not an instance attribute nor is it found in the class tree for self ). 
        name is the attribute name. This method should return the (computed) attribute 
        value or raise an AttributeError exception
        """
        return getattr(self.obj,  attr)
    
    
cake = MatchaCake()
cake_adapt = Adaptor(cake, flavor=cake.matcha_cake_flavor)
print(cake.matcha_cake_flavor())
print(cake_adapt.flavor())
#adaptor = Adaptor(MatchaCake, flavor='matcha_cake_flavor')
#print(adaptor.flavor())
        