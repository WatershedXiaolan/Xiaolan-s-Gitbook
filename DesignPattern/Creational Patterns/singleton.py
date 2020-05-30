class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state # make it an attribute dictionary
    
class Singleton(Borg):
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_state.update(**kwargs)
    def __str__(self):
        return str(self._shared_state)
a = Singleton()
print(a)
b = Singleton(mm=5)
print(b)
c = Singleton(nn=5)
print(c)



        