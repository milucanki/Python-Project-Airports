"""
island_hopper - a Python project that models an airport graph network and finds optimal flight routes for a small airplane from one airport to another.

The package is organised in modules, each one with responsibilities:

- extractor: airport database cleaning and filtering, creating the entire graph network of airports
- haversine: calculating the distance between 2 airports using their geographic coordinates
- bfs: Breadth-First Search
- dijkstra: shortest time to an airport algorithm
- decryptor: user input, user output, airport, country and region decryption
- visualization: visualizations of the graph network and routes
"""

__version__ = "0.1.0"