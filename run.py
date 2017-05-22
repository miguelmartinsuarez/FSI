# Search methods

import search
am = search.GPSProblem('A', 'M', search.romania)
au=search.GPSProblem('A', 'U', search.romania)
ab=search.GPSProblem('A', 'B', search.romania)
em=search.GPSProblem('E', 'M', search.romania)
rg=search.GPSProblem('R', 'G', search.romania)

#print ab.graph.nodes()

search.breadth_first_graph_search(am)
amSA=am
am = search.GPSProblem('A', 'M', search.romania)
search.depth_first_graph_search(am)
amSP=am
am = search.GPSProblem('A', 'M', search.romania)
search.min_value_graph_search(am)
amSRA=am
am = search.GPSProblem('A', 'M', search.romania)
search.min_value_graph_search_heuristic(am)
amSRAS=am
#----------------------------------------------

search.breadth_first_graph_search(au)
auSA=au
au = search.GPSProblem('A', 'U', search.romania)
search.depth_first_graph_search(au)
auSP=au
au = search.GPSProblem('A', 'U', search.romania)
search.min_value_graph_search(au)

auSRA=au
au = search.GPSProblem('A', 'U', search.romania)
search.min_value_graph_search_heuristic(au)
auSRAS=au

#----------------------------------------------------

search.breadth_first_graph_search(ab)
abSA=ab
ab = search.GPSProblem('A', 'B', search.romania)
search.depth_first_graph_search(ab)
abSP=ab
ab = search.GPSProblem('A', 'B', search.romania)
search.min_value_graph_search(ab)

abSRA=ab
ab = search.GPSProblem('A', 'B', search.romania)
search.min_value_graph_search_heuristic(ab)
abSRAS=ab

#---------------------------------------
search.breadth_first_graph_search(em)
emSA=em
em = search.GPSProblem('E', 'M', search.romania)
search.depth_first_graph_search(em)
emSP=em
em = search.GPSProblem('E', 'M', search.romania)
search.min_value_graph_search(em)

emSRA=em
em = search.GPSProblem('E', 'M', search.romania)
search.min_value_graph_search_heuristic(em)
emSRAS=em

#---------------------------------------
search.breadth_first_graph_search(rg)
rgSA=rg
rg = search.GPSProblem('R', 'G', search.romania)
search.depth_first_graph_search(rg)
rgSP=rg
rg = search.GPSProblem('R', 'G', search.romania)
search.min_value_graph_search(rg)

rgSRA=rg
rg = search.GPSProblem('R', 'G', search.romania)
search.min_value_graph_search_heuristic(rg)
rgSRAS=rg


print "Camino de A-M"
print "                 Anchura         Profundidad         Ramificacion y acotacion         Ramificacion y acotacion con subestimacion"

print "Profundidad          %d              %d                  %d                                 %d          " % (amSA.prof,amSP.prof,amSRA.prof,amSRAS.prof)

print "Nodos Expandidos     %d              %d                  %d                                 %d          " %  (amSA.expandnode,amSP.expandnode,amSRA.expandnode,amSRAS.expandnode)


print "Camino de A-B"
print "                 Anchura         Profundidad         Ramificacion y acotacion         Ramificacion y acotacion con subestimacion"

print "Profundidad          %d              %d                  %d                                 %d          " % (abSA.prof,abSP.prof,abSRA.prof,abSRAS.prof)

print "Nodos Expandidos     %d              %d                  %d                                 %d          " %  (abSA.expandnode,abSP.expandnode,abSRA.expandnode,abSRAS.expandnode)



print "Camino de A-U"
print "                 Anchura         Profundidad         Ramificacion y acotacion         Ramificacion y acotacion con subestimacion"

print "Profundidad          %d              %d                  %d                                 %d          " % (auSA.prof,auSP.prof,auSRA.prof,auSRAS.prof)

print "Nodos Expandidos     %d              %d                  %d                                 %d          " % (auSA.expandnode,auSP.expandnode,auSRA.expandnode,auSRAS.expandnode)

print "Camino de E-M"
print "                 Anchura         Profundidad         Ramificacion y acotacion         Ramificacion y acotacion con subestimacion"

print "Profundidad          %d              %d                  %d                                 %d          " % (emSA.prof,emSP.prof,emSRA.prof,emSRAS.prof)

print "Nodos Expandidos     %d              %d                  %d                                 %d          " % (emSA.expandnode,emSP.expandnode,emSRA.expandnode,emSRAS.expandnode)


print "Camino de R-G"
print "                 Anchura         Profundidad         Ramificacion y acotacion         Ramificacion y acotacion con subestimacion"

print "Profundidad          %d              %d                  %d                                 %d          " % (rgSA.prof,rgSP.prof,rgSRA.prof,rgSRAS.prof)

print "Nodos Expandidos     %d              %d                  %d                                 %d          " % (rgSA.expandnode,rgSP.expandnode,rgSRA.expandnode,rgSRAS.expandnode)

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
