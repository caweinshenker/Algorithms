class Edge(object):
    
    def __init__(self, one, other, weight=None):
        self.one = one
        self.other = other
        self.weight = weight
    
    def __str__(self):
        return "{} <--> {}".format(self.one, self.other)
    
    def getWeight(self):
        return self.weight
    
    def either(self):
        return self.one
    
    def other(self, node):
        if node == self.one:
            return self.other
        elif node == self.other:
            return self.one
        else:
            raise ValueError("Invalid endpoint")
