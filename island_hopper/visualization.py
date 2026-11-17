import networkx as nx
import matplotlib.pyplot as plt


def VisualizeGraph(graphDict):

    # Creating the graph.
    G = nx.Graph()

    # Adding the airports as nodes for the graph.
    for airportId, airportSpecs in graphDict.items():
        G.add_node(
            airportId,
            name=airportSpecs["name"],
            country=airportSpecs["country"],
            latitude=airportSpecs["latitude"],
            longitude=airportSpecs["longitude"]
        )

    # Adding the connections between the nodes.
    for airportId, airportSpecs in graphDict.items():
        for edge in airportSpecs["edges"]:
            G.add_edge(
                airportId,
                edge["destination"],
                distance=edge["distance"],
                duration_hours=edge["duration_hours"],
                totalTime_hours=edge["totalTime_hours"]
            )

    # Drawing the graph using matplotlib
    plt.figure(figsize=(16, 12))

    # Creating the nodes and edges.
    nx.draw(G, node_size=8, node_color="blue", edge_color="gray", width=0.3, with_labels=False)
    plt.title("Island Hopper - Airport Network")
    plt.show()


def VisualizeRoute(path):
    """
    Function that takes a route between the airports and visualizes the path using nodes and edges.
    """
    # Creating the graph.
    graph = nx.Graph()

    for airport in range(len(path) - 1):
        graph.add_edge(path[airport],path[airport+1])

    # Creating the nodes and edges.
    nx.draw(graph, with_labels=True, node_color="skyblue")
    plt.show()