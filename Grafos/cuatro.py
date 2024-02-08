import networkx as nx 
import matplotlib.pyplot as mpl

grafo = nx.Graph()

grafo.add_nodes_from([1, 2, 3, 4])

grafo.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (2, 6),(3, 4), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6) ])

nx.draw(grafo, with_labels=True, font_weight='bold')
mpl.show()