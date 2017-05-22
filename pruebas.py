import search
from utils import *

"""
grafo = search.UndirectedGraph(Dict(
    A=Dict(B=3 , C=2, G=1),
    B=Dict(D=0),
    C=Dict(D=1,F=3,G=2),
    D=Dict(F=3),
    F=Dict(H=4),
    H=Dict(G=2)
))
print grafo.nodes()
a = search.GPSProblem('A','H',grafo)

print search.breadth_first_graph_search(a).path()
print search.depth_first_graph_search(a).path()
"""

grafo = search.UndirectedGraph(Dict(
    A=Dict(B=3,C=2),
    D=Dict()))

a = search.GPSProblem('A','D',grafo)

##print


search.depth_first_graph_search(a)