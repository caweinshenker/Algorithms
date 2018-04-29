class DirectedEdge(object):
    
    def __init__(self, fr, to, weight=None):
        self.fr = fr
        self.to = to
        self.weight = weight
        
    def __str__(self):
        return "{} --> {}".format(self.fr, self.to)  
    
    def __lt__(self, other):
        return self.weight < other.weight
    
    def __gt__(self, other):
        return self.weight > other.weight
    
    def __eq__(self, other):
        return self.weight == other.weight
    
    def getWeight(self):
        return self.weight
            
    def source(self):
        return self.fr
    
    def sink(self):
        return self.to