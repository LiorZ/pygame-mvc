from collections import defaultdict
class Model:

    def __init__(self):
        self.observers = defaultdict(list)

    def set(self,**kwargs):
        for k,v in kwargs:
            setattr(self,k,v)
        self._notify(kwargs)

    def get(self,kw):
        return getattr(self,kw,None)

    def set(self,kw,val):
        setattr(self,kw,val)
        self._notify({kw:val})

    def registerObserver(self,obs,key_to_observe):
        self.observers[key_to_observe].append(obs)

    def _notify(self,**kwargs):
        keys = kwargs.keys()
        for k in keys:
            for obs in self.observers[k]:
                obs.notify(self.model,{k:kwargs[k]})
