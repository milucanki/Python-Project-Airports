# ✈️ Island Hopper
Island Hopper is a project that lets you plan the route of a small airplane, through a network of airports.
The route, between an origin and a destination airport, can be the one with the least amount of stops, the one with the least amount of time taken or the one furthest away from the origin.

## What the project does

The project allows you to get the best flight route between 2 airports that a small airplane can take. These flight routes can also get visualized using graphs. The flight routes are:
- How many stops are needed at minimum, from an origin airport, to reach a specific destination airport? (`island_hopper/bfs.py`) (Visualization: `island_hopper/visualization.py`)
- How much time is needed at minimum, from an origin airport, to reach a specific destination airport? (`island_hopper/dijkstra.py`) (Visualization: `island_hopper/visualization.py`)
- Which is the farthest airport that you can reach with at most 10 stops, from an origin airport? (`island_hopper/bfs.py`) (Visualization: `island_hopper/visualization.py`)

Alongside the route, the project allows you to see a network of all possible airports which this small airplane can land on and how the previously mentioned flight routes look in the entire network. (Visualization: `island_hopper/visualization.py`)

### How the routes are calculated

The original **OurAirports Dataset** data source was cleaned and filtered to retain only the valid landing locations of the small airplane.
Each airport is then represented as a node in a graph (`island_hopper/extractor.py`). Airports within the small airplane's maximum flight range are connected by weighted edges. The weight is the estimated flight time.

| Flight route | How it's calculated |
|------|-----------------|
| **Minimum number of flights** (`island_hopper/bfs.py`) | Calculated using the Breadth-First Search algorithm to find the route with the fewest flights.|
| **Minimum travelling time** (`island_hopper/dijkstra.py`) | Calculated using the Dijkstra algorithm to find the route with the lowest total travelling time.|
| **Farthest reachable airport** (`island_hopper/bfs.py`) | Calculated by modifying the Breadth-First Search algorithm and exploring all airports within the specified number of flights, then selects the farthest airport.  |

## Data sources

- **[OurAirports Dataset](https://ourairports.com/data/) ([Github Version](https://github.com/davidmegginson/ourairports-data))**: the original data source that contains the CSV files.
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

1. Clone the repository and enter the folder:
   ```bash
   git clone https://github.com/<your-user>/Python-Project-Airports.git
   cd Python-Project-Airports
   ```
   
2. Create a virtual environment and install the dependencies
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # on Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Run

Start the application from the project folder:
```
python -m island_hopper.main
```
Follow the terminal prompts' instructions and choose which values you want to insert or what functionality you want to use. After making your choices, the application calculates the requested route type using BFS or Dijkstra and displays the data about this route, together with the corresponding visualization.

### The example notebook

[`notebooks/island_hopper_walkthrough.ipynb`](notebooks/island_hopper_walkthrough.ipynb) demonstrates the project step by step. It shows how the airport data was cleaned, the graph construction and visualization. Algorithms such as BFS and Dijkstra are also explained.

Start Jupyter from the project folder and open it:

```bash
jupyter lab
```

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

Everything in `island_hopper/` is Python code that can be reused in the Jupyter notebook (`notebooks/`) or a script.
The main program (`main.py`) handles user interaction through the terminal.