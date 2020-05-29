class MatchaCake:
    # product
    def flavor(self):
        return "Matcha"
    def price(self):
        return 15

class CoffeeCake:
    # product
    def flavor(self):
        return "Coffee"
    def price(self):
        return 12

class MatchaCakeFactory:
    # concrete factory
    def getCake(self):
        return MatchaCake()

class CoffeeCakeFactory:
    # concrete factory
    def getCake(self):
        return CoffeeCake()

class CakeShop:
    # abstract factory
    def __init__(self, factory_name):
        self._factory = factory_name
    def show_cake(self):
        cake = self._factory.getCake()
        flavor = cake.flavor()
        price = cake.price()
        print(flavor)
        print(price)

factory = MatchaCakeFactory() # concrete factory
cakeshop = CakeShop(factory) # abstract factory 
cakeshop.show_cake()