class Component:
    """abstract class, host methods shared by both submenu and class"""
    def __init__(self, name):
        self.name = name
    def print_menu(self):
        print('You reached {}'.format(self.name))

class Child(Component):
    """concrete class that is the leaf"""
    def __init__(self, name):
        Component.__init__(self, name)
    def print_menu(self):
        print('You reached a component {}'.format(self.name))
        
class Composite(Component):
    """concrete class that acts as substructure"""
    def __init__(self, name):
        Component.__init__(self, name)
        self._objects = []
    def register_child(self, obj):
        self._objects.append(obj)
    def remove_child(self, obj):
        self._objects.remove(obj)
    def print_menu(self):
        print('You reached a menu component {}'.format(self.name))
        for obj in self._objects:
            obj.print_menu()
         
cake1 = Child('Matcha Cake')
cake2 = Child('Yogurt Cake')
sub_menu1 = Composite('Cake Menu')
sub_menu2 = Composite('Drink Menu')

sub_menu1.register_child(cake1)
sub_menu1.register_child(cake2)

top_menu = Composite('Sweet Cloud')
top_menu.register_child(sub_menu1)
top_menu.register_child(sub_menu2)

top_menu.print_menu()

