from functools import wraps

# decorate function

# decorator takes nested function format
def AddTopping(function):

    """Defines a dectorator"""
    
    #makes dectorator transparent in terms of name and documentation
    @wraps(function)
    def dectorator(*args, **kwargs):
        # grab the return value of function being decorated
        ret = function(*args, **kwargs)
        return ret + ' with yogurt topping'
    return dectorator

# the function being decorated

@AddTopping
def cake(name):
    """function being decorated"""
    return "This is a {} cake".format(name)
 
print(cake('Matcha'))