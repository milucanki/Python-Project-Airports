from extractor import extractValidAirports, edgesPopulator
from bfs import breadthFirstSearch, FurthestPointFunction
from decryptor import DecryptID
from dijkstra import MinimumTimeFunction
from visualization import VisualizeRoute, VisualizeGraph

nodesDict = extractValidAirports()

graphDict = edgesPopulator(nodesDict, 500.00)
"""
shortestRouteToCity,timeItTakes = breadthFirstSearch(graphDict)

for airport in shortestRouteToCity:
    print(DecryptID(airport))
print(timeItTakes)
"""
#print("The length of the shortest route to Sydney is: ",len(shortestRouteToSydney)-1)

#furthestPoint = FurthestPointFunction(graphDict)
#VisualizeRoute(furthestPoint[1])

#minTimeTuple = MinimumTimeFunction(graphDict)
#VisualizeRoute(minTimeTuple[0])



VisualizeGraph(graphDict)


"""
plan:
8. realize how to do the github/jupyter part ffs
9. comment everything
"""
