import pprint
import random 
import matplotlib.pyplot as plt
import networkx as nx
from DirectedEdge import DirectedEdge
from EdgeWeightedGraph import EdgeWeightedGraph

class EdgeWeightedDiGraph(EdgeWeightedGraph):
    
    def addEdge(self, v, w, weight):
        self._validateVertex(v)
        self._validateVertex(w)
        self.adj[v].append(DirectedEdge(v, w, weight))
        self.E += 1
    
    def displayGraph(self):
        G = nx.DiGraph()
        M = self.edges()
        edge_colors = range(2, M + 2)
        edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
        for d in self.data:
            G.add_node(d)
            for e in self.adjacent(d):
                v = e.source()
                w = e.sink()
                G.add_edge(v, w, weight=e.weight())
        
        pos = nx.layout.shell_layout
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_nodes(G, pos(G), node_color='blue')
        nx.draw_networkx_edges(G, pos(G), arrowstyle='->', arrowsize=10)
        nx.draw_networkx_labels(G, pos(G))
        nx.draw_networkx_edge_labels(G,pos(G),edge_labels=labels)
        plt.show()
        
    @staticmethod
    def generateRandomGraph(nodes=None, edges=None):
        g = EdgeWeightedDiGraph()
        for i in range(nodes):
            g.addNode(i)
        for i in range(edges):
            t, f = random.randint(0, nodes-1), random.randint(0, nodes-1)
            weight = random.randint(0, 100)
            g.addEdge(t, f, weight=weight)
        return g