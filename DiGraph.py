import pprint
import random 
import matplotlib.pyplot as plt
import networkx as nx
from Graph import Graph


class DiGraph(Graph):
    
    def __init__(self):
        Graph.__init__(self)
        self.indegree = []
    
    def addNode(self, data):
        Graph.addNode(self, data)
        self.indegree.append(0)
    
    def addEdge(self, v, w):
        self._validateVertex(v)
        self._validateVertex(w)
        self.adj[v].append(w)
        self.indegree[w] += 1
        self.E += 1
    
    def indegree(self, v):
        self._validateVertex(v)
        return self.indegree[v]
    
    def displayGraph(self):
        G = nx.DiGraph()
        M = self.edges()
        edge_colors = range(2, M + 2)
        edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
        for d in self.data:
            G.add_node(d)
            for e in self.adjacent(d):
                G.add_edge(d, e)
        nx.draw_networkx_nodes(G, Graph.pos(G), node_color='blue')
        nx.draw_networkx_edges(G, Graph.pos(G), arrowstyle='->', arrowsize=10)
        nx.draw_networkx_labels(G, Graph.pos(G))
        plt.show()
   
    @staticmethod
    def generateRandomGraph(nodes=None, edges=None):
        g = DiGraph()
        for i in range(nodes):
            g.addNode(i)
        for i in range(edges):
            t, f = random.randint(0, nodes-1), random.randint(0, nodes-1)
            g.addEdge(t, f)
        return g