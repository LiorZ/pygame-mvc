
class View:

    def __init__(self):
        self.funcs = dict()

    def notify(self,model,key,oldval,newval):
        func = self.funcs[key]
        func(model,key,oldval,newval)
    def bind(self,key,func):
        self.funcs[key] = func


