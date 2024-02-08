import networkx as nx 
import matplotlib.pyplot as mpl

grafo = nx.Graph()

grafo.add_nodes_from([1, 2, 3, 4])

grafo.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4)])

nx.draw(grafo, with_labels=True, font_weight='bold')
mpl.show()
