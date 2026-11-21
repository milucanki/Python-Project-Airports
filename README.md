a clear and informative README.md file, explaining what the project is about, listing important information (e.g., data sources, libraries), and providing clear instructions on how to setup and run the code;

# ✈️ Island Hopper
Island Hopper is a project that lets you plan the route of a small airplane, through a network of airports.
The route, between an origin and a destination airport, can be the one with the least amount of stops, the one with the least amount of time taken or the one furthest away from the origin.

## What the project does


### How the routes are calculated



## Data sources

- **[OurAirports Dataset](https://ourairports.com/data/) ([Github Version](https://github.com/davidmegginson/ourairports-data))**: the 
- **`data/airports.csv`**: the local file downloaded from the OurAirports dataset.
It contains many airports and their corresponding information.
- **`data/validAirports.csv`**: the local file that was cleaned and filtered from `data/airports.csv`.
All of the airport entries of this CSV file are valid landing spots for the small airplane.
- **`data/regions.csv`**: the local file that was downloaded from the OurAirports dataset.
It contains information about the regions where the airports are, including their codes and associated names.
- **`data/countries.csv`**: the local file that was downloaded from the OurAirports dataset.
It contains information about the countries where the airports are, including their codes and associated names.

## Libraries
| Library | Used for |
|---------|----------|
| `pandas` | accessing the local CSVs and getting data from them |
| `numpy` | applying the Haversine formula  |
| `scipy` | calculating the position of nodes when visualizing the airport networks |
| `matplotlib` | creating the graph, representing airports as nodes and direct flights as edges |
| `ipykernel` | connecting the Jupyter notebook to the Python kernel, allowing Python code to be ran in the notebook |
| `networkx` | drawing and displaying the network and the graphs |
| `jupyterlab` | running the walkthrough notebook |

## Setup



## Run




### The example notebook




## Project structure
```
Python Project Airports/
├── island_hopper/                          # the backend package
│   ├── __init__.py                         # description of package and information of version
│   ├── bfs.py                              # BFS algorithm and farthest airport search
│   ├── decryptor.py                        # decrypts information such as the user input, user output, airport, country or region
│   ├── dijkstra.py                         # the Dijkstra algorithm to find the fastest route
│   ├── extractor.py                        # cleans and filters the database, builds the graph network
│   ├── main.py                             # executes the project
│   ├── visualization.py                    # visualizes the network of the graph and optimized flight routes
│   └── haversine.py                        # calculates distance between airports
├── data/                                   # the data package
│   ├── airports.csv                        # all of the original airports
│   ├── countries.csv                       # the countries of the airports
│   ├── regions.csv                         # the regions of the airports
│   └── validAirports.csv                   # the valid airports
├── notebooks/
│   └── island_hopper_walkthrough.ipynb     # the app, step by step, in a notebook
├── .gitignore
├── requirements.txt
└── README.md
```