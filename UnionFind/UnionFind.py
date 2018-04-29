import matplotlib.pyplot as plt
import networkx as nx

class UnionFind(object):
    
    def __init__(self, n):
        self.n = n
        self.root = list(range(n))
        self._rank = [0 for i in range(n)]
        
    def find(self, u):
        self._validateRoot(u)
        while self.root[u] != u:
            u = self.root[u]
        return u
    
    def rank(self, u):
        return self._rank[self.find(u)]
    
    def connected(self, u, v):
        return self.find(u) == self.find(v)
    
    def union(self, u, v):
        self._validateRoot(u)
        self._validateRoot(v)
        
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU == rootV: return
    
        if self.rank(rootU) > self.rank(rootV):
            self.root[rootV] = rootU
        elif self.rank(rootU) < self.rank(rootV):
            self.root[rootU] = rootV
        else:
            self.root[rootV] = rootU
            self._rank[rootU] += 1
        
    def _validateRoot(self, u):
        assert u < self.n
        
    def display(self):
        G = nx.Graph()
        for i in range(self.n):
            G.add_node(i)
            while self.root[i] != i:
                G.add_edge(i, self.root[i])
                i = self.root[i]
        pos = nx.layout.shell_layout
        nx.draw_networkx_nodes(G, pos(G), node_color='blue')
        nx.draw_networkx_edges(G, pos(G))
        nx.draw_networkx_labels(G, pos(G))
        plt.show()
        