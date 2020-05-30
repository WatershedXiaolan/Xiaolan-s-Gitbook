# bridge: separate abstraction and implementation

class Shape:
    """abstract class that define a shape"""
    def __init__(self, x, y):
        self._x = x
        self._y = y

class Circie(Shape):
    """concrete class that inherits shape and defines a circle"""
    def __init__(self, x, y, r, api):
        """
        When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
        Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
        To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
        """
        Shape.__init__(self, x, y)
        self._radius = r
        self._api = api
    def draw(self):
        self._api.draw(self._x, self._y, self._radius)


class DrawingAPI:
    def draw(self, x, y, r):
        print('Draw at {} and {} with radius {}'.format(x, y, r))

    

c = Circie(1,2,3, DrawingAPI())
c.draw()
