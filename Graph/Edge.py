class Edge(object):
    
    def __init__(self, v, w, weight=None):
        self.v = v
        self.w = w
        self._weight = weight
    
    def __str__(self):
        return "{} <--> {}, weight: {}".format(self.v, self.w, self._weight)
    
    def __lt__(self, edge):
        return self.weight() < edge.weight()
    
    def __le__(self, edge):
        return self.weight() <= edge.weight()
    
    def __gt__(self, edge):
        return self.weight() > edge.weight()
    
    def __ge__(self, edge):
        return self.weight() >= edge.weight()

    def __eq__(self, edge):
        return self.weight() == edge.weight()
    
    def weight(self):
        return self._weight
    
    def either(self):
        return self.v
    
    def other(self, node):
        if node == self.v:
            return self.w
        elif node == self.w:
            return self.v
        else:
            raise ValueError("Invalid endpoint")
