class Shop:
    def __init__(self, name):
        self.name = name
    def accept(self, visitor):
        pass

class CakeShop(Shop):
    def accept(self, visitor):
        visitor.visit_CakeShop(self)
    def buyCake(self, name):
        print('Thanks for your {} cake order!'.format(name))

class FlowerShop(Shop):
    def accept(self, visitor):
        visitor.visit_FlowerShop(self)
    def buyFlower(self, name):
        print('Thanks for your {} flower order!'.format(name))

class Visitor:
    def __init__(self, name):
        self.name = name

class LittleGirl(Visitor):
    def visit_CakeShop(self, cakeShop):
        cakeShop.buyCake('StrawberryCream')
    def visit_FlowerShop(self, flowerShop):
        flowerShop.buyFlower('Daisy')

class Lady(Visitor):
    def visit_CakeShop(self, cakeShop):
        cakeShop.buyCake('RumRaisin')
    def visit_FlowerShop(self, flowerShop):
        flowerShop.buyFlower('Rose')    

cakeshop = CakeShop('SweetLand')
flowerShop = FlowerShop('ForestHill')
girl = LittleGirl('Tiffy')
lady = Lady('Maive')

cakeshop.accept(girl)
flowerShop.accept(lady)




