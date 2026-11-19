import networkx as nx
import matplotlib.pyplot as plt
from decryptor import DecryptID

def VisualizeEntireGraph(graphDict):
    """
    Function that is used by the entire graph dictionary in order to create a network visualization of all of the nodes and their edges.
    The output visualization has the nodes colored in different ways based on their continent.
    """
    # Creating the graph.
    graph = nx.Graph()

    continentColors = {
        "EU": "blue",
        "NA": "red",
        "AS": "green",
        "SA": "orange",
        "OC": "yellow",
        "AF": "purple",
        "AN": "brown",
    }

    nodeColors = []

    # Adding the airports as nodes for the graph.
    for airportId in graphDict:
        graph.add_node(airportId)
        continent = graphDict[airportId]["continent"]
        nodeColors.append(continentColors.get(continent, "gray"))

    # Adding the connections between the nodes.
    for airportId in graphDict:
        for edge in graphDict[airportId]["edges"]:
            graph.add_edge(airportId, edge["destination"])


    # Drawing the graph using matplotlib.
    plt.figure(figsize=(16, 12))

    # Creating the nodes and edges.
    nx.draw(graph, node_size=8, node_color=nodeColors, edge_color="gray", width=0.3, with_labels=False)
    plt.title("Island Hopper - Airport Network")


    # Adding information to the visualization using Matplotlib.
    plt.figtext(
            0.75, 0.90,
            "Airport Network\n\n"
            "Blue nodes: Europe\n"
            "Red nodes: North America\n"
            "Green nodes: Asia\n"
            "Orange nodes: South America\n"
            "Yellow nodes: Oceania\n"
            "Purple nodes: Africa\n"
            "Black nodes: Antarctica\n",
            fontsize=11,
            verticalalignment="center"
        )

    plt.show()

def VisualizeRouteInEntireGraph(path,graphDict,flightTime="",biggestDistance=""):
    """
    Function that takes as input the entire graph with all nodes and edges and a route in this graph.
    The output is a visualization of the route highlighted in the overall network.
    """
    graph = nx.Graph()

    # Add airports as nodes.
    for airportId in graphDict:
        graph.add_node(airportId)

    # Add connections between airports.
    for airportId in graphDict:
        for edge in graphDict[airportId]["edges"]:
            graph.add_edge(airportId, edge["destination"])

    # Calculating node positions
    pos = nx.spring_layout(graph, seed=42)

    # Draw the entire network.
    plt.figure(figsize=(16, 12))
    nx.draw(graph,pos, node_size=8, node_color="dimgray",edge_color="gray",width=0.2, with_labels=False)

    # Drawing the nodes of the route in blue.
    nx.draw_networkx_nodes(graph, pos, nodelist=path, node_color="blue", node_size=20)

    # Drawing the input route's edges into the network map.
    for i in range(len(path) - 1):
        nx.draw_networkx_edges(graph, pos, edgelist=[(path[i], path[i+1])], edge_color="red", width=0.4)

    # Getting information about the route based on the task.
    if flightTime != "":
        flightTime = "Flight time: "+str(round(flightTime, 2)) + " hours"
    if biggestDistance != "":
            biggestDistance = "Distance from origin: "+str(round(biggestDistance, 2)) + " km"
    stops = "Number of stops: " + str(len(path) - 2)

    plt.title("Island Hopper - Specific Route")


    # Adding information to the visualization using Matplotlib.
    plt.figtext(
        0.75, 0.90,
        "Route information:\n\n"
        "Blue nodes: Airports in the selected route\n"
        "Red lines: Flights in the selected route\n"
        "Grey nodes: Other airports\n\n"
        + stops + "\n"
        + flightTime + "\n"
        + biggestDistance,
        fontsize=11,
        verticalalignment="center"
    )

    plt.show()

def VisualizeRoute(path,flightTime="",biggestDistance=""):
    """
    Function that takes a route between 2 airports and visualizes the path using nodes and edges.
    It does this by using NetworkX to create the graph and it uses Matplotlib to draw it.
    """
    # Creating the graph.
    graph = nx.Graph()

    # Dictionary that holds the display for each node.
    labels = {}

    # Getting airport information.
    for airportId in path:
        airport = DecryptID(airportId)
        name = list(airport.keys())[0]
        municipality = airport[name]["municipality"]
        country = airport[name]["country"]
        continent = airport[name]["continent"]

        # Associating airport ID with its display 
        labels[airportId] = f"{name} - {municipality} - {country} - {continent}"

    for edges in range(len(path) - 1):
        graph.add_edge(path[edges],path[edges+1])

    # This line is a layout algorithm that was added in order to make the end graph readable.
    pos = nx.kamada_kawai_layout(graph)

    # Creating the nodes and edges.
    nx.draw(graph, pos=pos, labels=labels, with_labels=True, node_color="skyblue",font_size=6)


    # Getting information about the route based on the task.
    if flightTime != "":
        flightTime = "Flight time: "+str(round(flightTime, 2)) + " hours"
    if biggestDistance != "":
        biggestDistance = "Distance from origin: "+str(round(biggestDistance, 2)) + " km"
    stops = "Number of stops: " + str(len(path) - 2)

    # Adding information to the visualization using Matplotlib.
    plt.figtext(
        0.75, 0.10,
        "Route information:\n\n"
        + stops + "\n"
        + flightTime + "\n"
        + biggestDistance,
        fontsize=11,
        verticalalignment="center"
        )

    plt.show()