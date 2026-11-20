from extractor import extractValidAirports, edgesPopulator
from bfs import breadthFirstSearch, FurthestPointFunction
from decryptor import DecryptID
from dijkstra import MinimumTimeFunction
from visualization import VisualizeRoute, VisualizeEntireGraph,VisualizeRouteInEntireGraph

# ========================================================
# Showing entire graph network (with continents colors)
nodesDict = extractValidAirports()
graphDict = edgesPopulator(nodesDict, 750.00)
#VisualizeEntireGraph(graphDict)
# ========================================================

# Cities example: Sydney, London, New York, Tokyo, Rio De Janeiro, Cape Town
# rio de janeiro / new york can't be reached with 500 km fuel tank, but can with 750 km

# ========================================================
# Minimum stops needed from origin (Milan) to destination (Sydney)
#shortestRouteToCity,timeItTakes = breadthFirstSearch(graphDict)
#VisualizeRoute(shortestRouteToCity,timeItTakes)
#VisualizeRouteInEntireGraph(shortestRouteToCity,graphDict,timeItTakes)
# ========================================================

# ========================================================
# Minimum time needed from origin (Milan) to destination (Sydney)
#minTimePath, minTime = MinimumTimeFunction(graphDict)
#VisualizeRoute(minTimePath,minTime)
#VisualizeRouteInEntireGraph(minTimePath,graphDict,minTime)
# ========================================================

# ========================================================
# Farthest airport that you can reach with at most k (10) stops
#furthestPointInfoTuple,furthestPointPath,furthestPointTime = FurthestPointFunction(graphDict)
#furthestPointDistance = furthestPointInfoTuple[2]
#VisualizeRoute(furthestPointPath,furthestPointTime,furthestPointDistance)
#VisualizeRouteInEntireGraph(furthestPointPath,graphDict,furthestPointTime,furthestPointDistance)
# ========================================================