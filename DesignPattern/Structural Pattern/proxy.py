import time
class Chef:
    """class takes resource to instantiate."""
    def idle(self):
        print("Welcome. Chef is waiting for you!")

class Waiter:
    """class act as proxy."""
    def __init__(self):
        self.status = 'busy'
    
    def get_chef(self):
        if self.status == 'busy':
            # dont instantiate 
            print('Chef is busy. Please come back later')
        else:
            chef = Chef()
            time.sleep(2)
            chef.idle()

waiter = Waiter()
waiter.get_chef()
waiter.status = 'free'
waiter.get_chef()


