from .extractor import extractValidAirports, edgesPopulator
from .bfs import breadthFirstSearch, FurthestPointFunction
from .decryptor import DecryptID
from .dijkstra import MinimumTimeFunction
from .visualization import VisualizeRoute, VisualizeEntireGraph,VisualizeRouteInEntireGraph
"""
Terminal menu of Island Hopper: asks the user what to calculate and shows the result and visualization.
"""
def main():
    """
    Running the Island Hopper terminal menu
    """
    print("Connected to main.py succesfully...")
    print()

    # ========================================================
    # Menu selection
    # ========================================================

    print("Which functionality do you want to use?")
    print("1. Visualize the entire airport network")
    print("2. Find the route with the minimum number of flights")
    print("3. Find the route with the minimum travelling time")
    print("4. Find the farthest airport within k flights")
    print("Type in `exit` to stop process.")

    while True:

        choice = str(input("\nEnter your choice: "))
        if choice in ["1","2","3","4"]:
            break

        if choice == "exit":
            break
        print("Invalid choice. Please enter a number between 1 and 4.")

    # ========================================================
    # Maximum flight range validation
    # ========================================================
    if choice != "exit":
        while True:
            userRange = input("Enter the small airplane's maximum flight range (km): ").strip()

            try:
                maxRange = float(userRange)

                if maxRange <= 0:
                    print("The maximum range must be a positive finite number.")
                else:
                    break

            except ValueError:
                print("Invalid input. Please enter a valid numeric range.")

        # ========================================================
        # Build the airport graph
        # ========================================================

        try:
            nodesDict = extractValidAirports()
            graphDict = edgesPopulator(nodesDict, maxRange)

            print(f"\nAirport graph created with a maximum range of {maxRange} km.")

        except Exception as error:
            print(f"Error while creating the airport graph: {error}")
            exit()

        # ========================================================
        # Executing the functionality
        # ========================================================

        match choice:
            case "exit":
                print("Exiting program...")
            case "1":
                # Showing entire graph network (with continents colors)
                VisualizeEntireGraph(graphDict)
                print("Close graph when done viewing to end program.")
            case "2":
                # BFS: minimum stops
                try:
                    result = breadthFirstSearch(graphDict)

                    if result is not None:
                        shortestRoute, timeTaken = result
                        print()
                        print(f"Number of flights: {len(shortestRoute) - 2}")
                        print(f"Time taken: {timeTaken}")

                        print()
                        print("Creating the graph of the flight...")
                        print("Close the graph when done viewing to view the network graph version.")
                        VisualizeRoute(shortestRoute, timeTaken)

                        print()
                        print("Creating the network graph of the flight...")
                        print("Close graph when done viewing to end program.")
                        VisualizeRouteInEntireGraph(shortestRoute, graphDict, timeTaken)

                except ValueError as error:
                    print(f"Could not find route: {error}")
            case "3":
                # Dijkstra: Minimum travelling time
                try:
                    result = MinimumTimeFunction(graphDict)

                    if result is not None:
                        minimumTimePath, minimumTime = result
                        print()
                        print(f"Number of flights: {len(minimumTimePath) - 2}")
                        print(f"Minimum journey time: {round(minimumTime, 2)} hours")


                        print()
                        print("Creating the graph of the flight...")
                        print("Close the graph when done viewing to view the network graph version.")
                        VisualizeRoute(minimumTimePath, minimumTime)

                        print()
                        print("Creating the network graph of the flight...")
                        print("Close graph when done viewing to end program.")
                        VisualizeRouteInEntireGraph(minimumTimePath, graphDict, minimumTime)

                except ValueError as error:
                    print(f"Could not find route: {error}")
            case "4":
                # BFS: Farthest airport within k flights
                try:
                    result = FurthestPointFunction(graphDict)

                    if result is not None:
                        furthestPointInfoTuple, furthestPointPath, furthestPointTime = result
                        furthestAirportId = furthestPointInfoTuple[0]
                        furthestPointDistance = furthestPointInfoTuple[2]
                        print()
                        print(f"Farthest reachable airport: {graphDict[furthestAirportId]['name']}")
                        print(f"Distance from origin: {round(furthestPointDistance, 2)} km")
                        print(f"Number of flights: {len(furthestPointPath) - 2}")
                        print(f"Total journey time: {round(furthestPointTime, 2)} hours")
                        
                        print()
                        print("Creating the graph of the flight...")
                        print("Close the graph when done viewing to view the network graph version.")
                        VisualizeRoute(furthestPointPath,furthestPointTime,furthestPointDistance)

                        print()
                        print("Creating the network graph of the flight...")
                        print("Close graph when done viewing to end program.")
                        VisualizeRouteInEntireGraph(furthestPointPath,graphDict,furthestPointTime,furthestPointDistance)

                except ValueError as error:
                    print(f"Could not find a reachable airport: {error}")

    else:
        print("Exiting program...")


    # Cities example: Sydney, London, New York, Tokyo, Rio De Janeiro, Cape Town
    # rio de janeiro / new york can't be reached with 500 km fuel tank, but can with 750 km

if __name__ == "__main__":
    main()