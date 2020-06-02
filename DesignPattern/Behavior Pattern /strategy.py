class Navigator:
    def __init__(self, name):
        self.name = name
    def rout(self, strategy, a, b):
        # context object communicates with strategy only via the interface
        strategy.routing(a, b)

class Biking:
    def routing(self, a, b):
        print("Please go through Lake side from {} to {}".format(a, b))

class Hiking:
    def routing(self, a, b):
        print("Please go through forest hill from {} to {}".format(a, b))

map = Navigator('XLmap')
a = 'A'
b = 'B'
map.rout(Biking(), a, b)
map.rout(Hiking(), a, b)