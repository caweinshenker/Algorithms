import pprint
import random 
import matplotlib.pyplot as plt
import networkx as nx
from Edge import Edge
from Graph import Graph

class EdgeWeightedGraph(Graph):
    
    def addEdge(self, v, w, weight):
        self._validateVertex(v)
        self._validateVertex(w)
        self.adj[v].append(Edge(v, w, weight))
        self.adj[w].append(Edge(w, v, weight))
        self.E += 1
    
    def __str__(self):
        return pprint.saferepr(
            """
            Nodes: {}
            Edges: {}
            """.format(pprint.saferepr(self.data), \
                       pprint.saferepr([str(x) for x in self.adj])))
        
    def displayGraph(self):
        G = nx.Graph()
        M = self.edges()
        edge_colors = range(2, M + 2)
        edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
        for d in self.data:
            G.add_node(d)
            for e in self.adjacent(d):
                v = e.either()
                w = e.other(v)
                G.add_edge(v, w, weight=e.weight())
        
        labels = nx.get_edge_attributes(G, 'weight')
        print(labels)
        nx.draw_networkx_nodes(G, Graph.pos(G), node_color='blue')
        nx.draw_networkx_edges(G, Graph.pos(G))
        nx.draw_networkx_labels(G,Graph.pos(G))
        nx.draw_networkx_edge_labels(G,Graph.pos(G),edge_labels=labels)
        plt.show()
        
    @staticmethod
    def generateRandomGraph(nodes=None, edges=None):
        g = EdgeWeightedGraph()
        for i in range(nodes):
            g.addNode(i)
        for i in range(edges):
            t, f = random.randint(0, nodes-1), random.randint(0, nodes-1)
            weight = random.randint(0, 100)
            g.addEdge(t, f, weight=weight)
        return g