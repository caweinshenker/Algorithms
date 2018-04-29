import pprint
import random 
import matplotlib.pyplot as plt
import networkx as nx
from Graph import Graph

class EdgeWeightedGraph(Graph):
    
     def addEdge(self, v, w, weight):
        self._validateVertex(v)
        self._validateVertex(w)
        self.adj[v].append(Edge(v, w, weight))
        self.E += 1
    
    def displayGraph(self):
        Graph.displayGraph
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,Graph.pos(G),edge_labels=labels)
        plt.show()
        
    @staticmethod
    def generateRandomGraph(nodes=None, edges=None):
        g = Graph()
        for i in range(1, nodes):
            g.addNode(i)
        for i in range(edges):
            t, f = random.randint(0, nodes-1), random.randint(0, nodes-1)
            weight = random.random(-1, 1)
            g.addEdge(t, f, weight)
        return g