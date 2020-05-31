class Publisher:
    def __init__(self, name):
        self.name = name
        self.subscribers = []
    def addSubscriber(self, object):
        self.subscribers.append(object)
    def removeSubscriber(self, object):
        self.subscribers.remove(object)

class CakeShop(Publisher):
    def __init__(self, name):
        Publisher.__init__(self, name)
        self._newcake = ""
    
    @property
    def new(self):
        return self._newcake
    @new.setter
    def new(self, newcake):
        self._newcake = newcake
    def notify(self):
        print('{} is sending out {} cake'.format(self.name, self._newcake))
        for obj in self.subscribers:
            obj.update(self)

class Subscribers:
    def update(self):
        pass
class Girl(Subscribers):
    def update(self, sub):
        print('Girl received a {} cake'.format(sub._newcake))
        if "berry" in sub._newcake:
            print('Girl loves berry cake')
class Lady(Subscribers):
    def update(self, sub):
        print('Lady received a {} cake'.format(sub._newcake))
        if "rum" in sub._newcake:
            print('Lady loves rum cake')



a = CakeShop('SweetLand')
s1 = Girl()
s2 = Lady()
a.addSubscriber(s1)
a.addSubscriber(s2)

a.new = 'strawberry and cream'
a.notify()
a.new = 'rum and raisin'
a.notify()
