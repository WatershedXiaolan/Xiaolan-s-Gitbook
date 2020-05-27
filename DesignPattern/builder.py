class Director:
    # the action of construct
    def __init__(self, builder):
        self._builder = builder
    def construct_cake(self):
        # create a product through abstract builder
        # put actions from concrete builder
        self._builder.build_cake()
        self._builder.add_flavor()
        self._builder.add_topping()
    
    def get_cake(self):
        return self._builder.cake

class Builder:
    # separate initialize object from constructing object
    def __init__(self):
        self.cake = None

    def build_cake(self):
        self.cake = Cake()


class Strawberry_pearl(Builder):
    # concrete builder

    def add_flavor(self):
        self.cake.flavor = 'strawberry'
    def add_topping(self):
        self.cake.topping = 'pearl'


class Blackforest(Builder):
    # concrete builder

    def add_flavor(self):
        self.cake.flavor = 'choclate'
    def add_topping(self):
        self.cake.topping = 'cherry'       

class Cake:
    # defines the field of object, but not the details
    def __init__(self):
        self.flavor = None
        self.topping = None
    
    def __str__(self):
        return 'This is a {} cake with {} topping'.format(self.flavor, self.topping)

builder = Strawberry_pearl() # select a concrete builder
director = Director(builder) # assign a director who is going to build the product
director.construct_cake()
cake = director.get_cake()
print(cake)

builder2 = Blackforest()
director2 = Director(builder2)
director2.construct_cake()
cake2 = director2.get_cake()
print(cake2)
