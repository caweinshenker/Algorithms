class DirectedEdge(object):
    
    def __init__(self, fr, to, weight=0):
        self.fr = fr
        self.to = to
        self._weight = weight
        
    def __str__(self):
        return "{} --> {}, {}".format(self.fr, self.to, self._weight)  
    
    def __lt__(self, other):
        return self.weight < other.weight
    
    def __gt__(self, other):
        return self.weight > other.weight
    
    def __eq__(self, other):
        return self.weight == other.weight
    
    def weight(self):
        return self._weight
            
    def source(self):
        return self.fr
    
    def sink(self):
        return self.to