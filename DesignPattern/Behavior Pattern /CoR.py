class Handlers:
    def __init__(self):
        self._successor = None
    @property
    def successor(self):
        return self._successor
    @successor.setter
    def successor(self, successor):
        self._successor = successor
    def handle(self):
        pass

class CakeTopping(Handlers):
    def handle(self, request):
        if request.lower() == 'cake':
            print("Add strawnberry topping")
        else:
            self._successor.handle(request)

class RamenTopping(Handlers):
    def handle(self, request):
        if request.lower() == 'ramen':
            print("Add Chashu and egg")
        else:
            self._successor.handle(request)

class DefaultHandle(Handlers):
    def handle(self, request):
        print('No availble topping for {}'.format(request))

ch = CakeTopping()
rh = RamenTopping()
dh = DefaultHandle()
ch.successor = rh
rh.successor = dh

r = 'cake'
ch.handle(r)

r = 'ramen'
ch.handle(r)

r = 'dayong'
ch.handle(r)


