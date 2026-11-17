from decryptor import DecryptID, IDToMunicipality, InputSelectorFunction,OutputSelectorFunction,CalculateRouteTime
from haversine import haversineFormula

def breadthFirstSearch(graphDict):
    """
    In order to find the lowest possible amount of stops between a starting and ending airport, a Breadth First Search algorithm was used.
    The BFS starts identifying airports, starting from an airport that the user has chosen, until it spots an airport ID that is from the same
    municipality/city (Sydney) as the user wants.
    Then, the function follows the dictionary that the BFS algorithm did from the end to the start in order to get the route that was taken by the algorithm.
    """
    # Getting the starting airport from the user.
    originAirport = InputSelectorFunction()
    if originAirport == None:
        print("Something went wrong!")
        return None


    # Getting the wanted destination of the user.
    wantedDestination = OutputSelectorFunction()
    if wantedDestination == None:
        print("Please enter a valid city!")
        return None

    # Checking if the input airport is the destination
    if IDToMunicipality(originAirport) == wantedDestination.lower():
        return [DecryptID(originAirport)]

    # The queue is a list that holds every single airport ID that needs to get explored. The BFS processes them as if it is going level by level down the graph.
    queue = []
    queue.append(originAirport)

    # Stores airports that have already been discovered, so that the algorithm doesn't visit them again.
    visited = set()
    visited.add(originAirport)

    # This dictionary constructs the route from the origin airport. The key is the next airport and the value is the predecessor airport.
    allBFSExploredPaths = {}
    allBFSExploredPaths[originAirport] = None

    # Variable that is used to break out of the while-loop when the wanted airport gets found.
    breakWhileCheck = False

    # Empty variable used to "catch" the first airport that was spotted in the wanted destination (ex: Sydney)
    destinationCatch = None    

    while queue:
        if breakWhileCheck:
            # Getting out of the while-loop.
            break
        currentAirport = queue.pop(0)

        # The variable nextPossibleDest is the list of all possible next nodes that the origin node can go to / starting from this node, the next level of the graph.
        # It is taken from the graph dictionary's "edges" value.
        nextPossibleDest = graphDict[currentAirport]["edges"]

        for destination in nextPossibleDest:
            """
            Every possible airport ID that the origin airport can go to gets processed. This means that it gets checked whether it has already been visited. 
            If it has, skip it. Otherwise, mark it as visited.
            Then, that node gets documented in the allBFSExploredPaths dictionary as a key, while its predecessor is the value. This way it is possible to create the route of nodes.
            Then the queue gets the airport's connections, which will be explored later. 
            """
            idNextNode = destination["destination"]
            if idNextNode in visited:
                continue
            visited.add(idNextNode)
            allBFSExploredPaths[idNextNode] = currentAirport
            queue.append(idNextNode)
            if IDToMunicipality(idNextNode) == wantedDestination.lower():
                # Checking if the ID is the same as the destination one. If it is, the BFS algorithm is done and can get broken.
                breakWhileCheck = True
                destinationCatch = idNextNode
                break

    # Edge case if the destination is unreachable or not in the database.
    if destinationCatch is None:
        return None

    
    path = []
    current = destinationCatch

    # Reconstructing the route backwards from the destination to the origin.
    while current is not None:
        path.append(current)
        current = allBFSExploredPaths[current]
    # Reversing the output list.
    path.reverse()

    # Calculating the time it takes for this path to be realized.
    totalTime = CalculateRouteTime(path,graphDict)

    return (path,totalTime)


def FurthestPointFunction(graphDict):
    """
    Modified version of the BFS algorithm from up. Instead of checking for a specific node down the BFS graph level, the algorithm goes down "wantedNodeLevel" levels and takes in consideration
    all of the nodes on that level and the ones before, also. Then, the Haversine function is applied to every node and the airport with the highest distance between it and the origin
    airport gets returned.
    """
    # Getting the starting airport from the user.
    originAirport = InputSelectorFunction()
    if originAirport == None:
        print("Something went wrong!")
        return None

    # Getting the graph level wanted by the user.
    user_level = input("Enter the number of stops the airplane needs to reach: ")
    try:
        wantedNodeLevel = int(user_level)
    except ValueError:
        print("Please enter an integer number as the level.")
        return None

    # Initiating the variables for the BFS algorithm.
    queue = []
    queue.append(originAirport)

    visited = set()
    visited.add(originAirport)

    allBFSExploredPaths = {}
    allBFSExploredPaths[originAirport] = None

    wantedLevelCount = 0

    while queue and wantedLevelCount < wantedNodeLevel+1:
        nodesInCurrentLevel = len(queue)

        # This for-loop makes sure I only process the airports belonging to the current BFS level, before moving to the next one.
        for _ in range(nodesInCurrentLevel):
            currentAirport = queue.pop(0)

            # The variable nextPossibleDest is the list of all possible next nodes that the origin node can go to.
            # It is taken from the graph dictionary's "edges" value.
            nextPossibleDest = graphDict[currentAirport]["edges"]

            for destination in nextPossibleDest:
                idNextNode = destination["destination"]
                if idNextNode in visited:
                    continue
                visited.add(idNextNode)
                allBFSExploredPaths[idNextNode] = currentAirport
                queue.append(idNextNode)
        wantedLevelCount += 1
        

    
    # Initializing the information about the origin airport.
    decryptedOrigin = DecryptID(originAirport)
    decryptedOriginName = decryptedOrigin[list(decryptedOrigin.keys())[0]]
    latOrigin, longOrigin = decryptedOriginName["latitude"],decryptedOriginName["longitude"]

    # Initializing the variables that will hold the information about the furthest airport.
    # If there is no furthest airport, then the furthest airport from the origin is the origin itself.
    furthestAirportId = originAirport
    furthestAirport = decryptedOrigin
    biggestDistance = -1

    
    # Checking the distance between all of the IDs which were visited and the origin airport
    # "visited" is being considered because the task is "the farthest airport that you can reach with AT MOST 10 (x) stops"
    # One thought process is to take all of the airports from level 10, but that is wrong because there is a chance that the furthest airport can be present in level 5 instead of level 10
    for id in visited:
        decryptedId = DecryptID(id)
        airportDestinationName = decryptedId[list(decryptedId.keys())[0]]

        latDest,longDest = airportDestinationName["latitude"],airportDestinationName["longitude"]

        distanceBetweenOriginDestination = haversineFormula(latOrigin,longOrigin,latDest,longDest)

        if biggestDistance < distanceBetweenOriginDestination:
            biggestDistance = distanceBetweenOriginDestination
            furthestAirportId = id
            furthestAirport = decryptedId

    """
    furthestAirportId = ID of the furthest airport
    furthestAirport = dictionary information about this airport
    biggestDistance = distance between origin airport and the destination airport
    """

    # Same path reversing process as the previous BFS function.
    path = []
    current = furthestAirportId

    # Reconstructing the route backwards from the destination to the origin.
    while current is not None:
        predecessorNode = allBFSExploredPaths[current]
        path.append(current)
        current = predecessorNode
    path.reverse()

    # Calculating the time it takes for this path to be realized.
    totalTime = CalculateRouteTime(path,graphDict)

    # Returning a tuple that contains the ID, information and distance from the origin of it of the furthest airport, including the path it took to get there.
    return [(furthestAirportId,furthestAirport,biggestDistance),path,totalTime]
