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

def get_cake(name):
    # factory method
    if name=='Matcha':
        return MatchaCake()
    if name=='Coffee':
        return CoffeeCake()

cake1 = get_cake('Coffee')
print(cake1.flavor())
print(cake1.price())
cake2 = get_cake('Matcha')
print(cake2.flavor())
print(cake2.price())
