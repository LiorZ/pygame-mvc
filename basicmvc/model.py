from collections import defaultdict
import sys
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
        oldval = getattr(self,kw,None)
        setattr(self,kw,val)
        self._notify(kw,oldval,val)

    def registerObserver(self,obs,key_to_observe):
        self.observers[key_to_observe].append(obs)

    def _notify(self,key,oldval,newval):
        for obs in self.observers[key]:
            obs.notify(self,key,oldval,newval)
