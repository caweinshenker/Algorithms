class DirectedEdge(object):
    
    def __init__(self, f, t, weight=None):
        self.f = f
        self.to = to
        self.weight = weight
        
    def __str__(self):
        return "{} --> {}".format(self.one, self.other)   
    
    def getWeight(self):
        return self.weight
            
    def f(self):
        return self.f
    
    def t(self):
        return self.t