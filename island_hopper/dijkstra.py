from decryptor import IDToMunicipality,InputSelectorFunction,OutputSelectorFunction

def MinimumTimeFunction(graphDict):

    # Getting the starting airport from the user.
    originAirportId = InputSelectorFunction()
    if originAirportId == None:
        print("Something went wrong!")
        return None

    # Getting the wanted destination of the user.
    wantedDestination = OutputSelectorFunction()
    if wantedDestination == None:
        print("Please enter a valid city!")
        return None

    distances = DistanceDictionaryPopulator(originAirportId,graphDict)

    # Storing the predecessors similarly to the BFS functions.
    # This dictionary constructs the route from the origin airport. The key is the next airport and the value is the predecessor airport.
    predecessors = {}
    predecessors[originAirportId] = None

    # List of all airports which haven't been explored yet and need to be.
    unvisited = list(graphDict.keys())

    destinationCatch = None

    while unvisited:

        # Finds the unvisited airport with the smallest currently known travel time between origin airport and every other airport in the graph
        currentAirport = min(unvisited, key=lambda airport: distances[airport])

        # If the smallest remaining time travel is infinity, then this means that the remaining airports are unreachable from the origin.
        if distances[currentAirport] == float("inf"):
            break

        # Removing the current airport from the unvisited list because it has been visited already and no longer needs to be visited.
        unvisited.remove(currentAirport)

        # Edge case: checking if the input airport is the same as the destination airport.
        if IDToMunicipality(currentAirport) == wantedDestination.lower():
            destinationCatch = currentAirport
            break

        # For-loop used to check the current airport's neighbours.
        for edge in graphDict[currentAirport]["edges"]:
            nextAirport = edge["destination"]

            # Ignoring the airports that have already been visited.
            if nextAirport not in unvisited:
                continue


            # Getting how much traveling time it took + 1 hour to refuel at another airport
            edgeCost = edge["totalTime_hours"]
            if currentAirport != originAirportId:
                edgeCost += 1

            # Comparing new route with the existing one.
            newTime = distances[currentAirport] + edgeCost

            # Comparing the new time with the best time found so far.
            # If the new time is faster, update the distance and remember the route where the plane came from.
            if newTime < distances[nextAirport]:
                distances[nextAirport] = newTime
                predecessors[nextAirport] = currentAirport      

    # Edge case: if the destination ID is never found.
    if destinationCatch is None:
        return None

    # Same reconstruction logic from the BFS functions.
    path = []
    current = destinationCatch
    
    # Reconstructing the route backwards from the destination to the origin.
    while current is not None:
        path.append(current)
        current = predecessors[current]
    # Reversing the output list.
    path.reverse()
    
    return (path, distances[destinationCatch])




def DistanceDictionaryPopulator(originAirportId,graphDict):
    """
    Function that populates the distance dictionary which contains the weight of the edges between the starting node and every single other node in the graph.
    Since it is being initialized the "smallest" possible value that the distances can be is infinity. If the algorithm spots a lower value then it will replace infinity.
    """
    distances = {}

    for airportId in graphDict:
        distances[airportId] = float("inf")

    distances[originAirportId] = 0

    return distances


