import matplotlib.pyplot as plt
import networkx as nx
import random
import pprint
 
class Graph(object):
    
    pos = nx.layout.shell_layout
    
    def __init__(self):
        self.data = []
        self.adj = []
        self.V = 0
        self.E = 0
        
    def __str__(self):
        return """
        Nodes: {} 
        
        Edges:
        {}
        """.format(pprint.saferepr(self.data), pprint.saferepr(self.adj))

    def vertices(self):
        return self.V
    
    def edges(self):
        return self.E
    
    def addNode(self, data):
        self.data.append(data)
        self.adj.append([])
        self.V += 1
        
    def addEdge(self, v, w):
        self._validateVertex(v)
        self._validateVertex(w)
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1
    
    def adjacent(self, v):
        self._validateVertex(v)
        return self.adj[v]
    
    def degree(self, v):
        self._validateVertex(v)
        return len(self.adj[v])
    
    def _validateVertex(self, v):
        assert v < self.V
    
    def displayGraph(self):
        
        G = nx.Graph()
        M = self.edges()
        edge_colors = range(2, M + 2)
        edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
        for d in self.data:
            G.add_node(d)
            for e in self.adjacent(d):
                G.add_edge(d, e)
        nx.draw_networkx_nodes(G, Graph.pos(G), node_color='blue')
        nx.draw_networkx_edges(G, Graph.pos(G))
        nx.draw_networkx_labels(G, Graph.pos(G))
        plt.show()
        
    @staticmethod
    def generateRandomGraph(nodes=None, edges=None):
        g = Graph()
        for i in range(nodes):
            g.addNode(i)
        for i in range(edges):
            t, f = random.randint(0, nodes-1), random.randint(0, nodes-1)
            g.addEdge(t, f)
        return g