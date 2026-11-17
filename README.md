
8. Island Hopper

Consider the OurAirports dataset, describing airports all over the world. Assume that you have a small plane, which can only land at large and medium airports,
and that has a predefined maximum range of kilometers. Each flight takes 1 hour every 500 km, plus 1 hour for refuelling at each stop; in addition, some time
is needed for customs whenever you land in a different country than the one you departed from. Starting from Milan Malpensa (or any other airport of your
choice), is it possible to reach Sydney? How many stops and how much time are needed at minimum? And which is the farthest airport that you can reach with at
most 10 stops?


Github page for database: https://github.com/davidmegginson/ourairports-data

Website: https://ourairports.com/data/

Ideas:
do a function that simulates the planes flights: if the planes tank is < 500 km, must find a nearby L and M airport to park and refuel for 1 hour

predefined maximum range of kilometers!

Each flight takes 1 hour every 500 km, 
plus 1 hour for refuelling at each stop; 
in addition, some time is needed for customs whenever you land in a different country than the one you departed from.

Starting from Milan Malpensa (or any other airport of your choice), is it possible to reach Sydney?

How many stops and how much time are needed at minimum? 

And which is the farthest airport that you can reach with at most 10 stops?

use the latitude and longitude to calculate the distance between airports to get the furthest airport

look through the csv file airport and cut out all airports that aren't medium_airport or large_airport

use the countries csv file to compare the countries' ids with their actual name

the only csv files you need are: airport.csv, airport-frequencies.csv, countries.csv

use breadth/depth search
use the class object thingy you couldn't understand in acsai
draw a graph showing each location for the nodes and weight for every edge
maybe show a graph that shows the best 5 routes idk

use the haversine formula to calculate distance between airports using lat, long, alt

maybe a networking :eyes (no the networking will be too big)

whatever input x of the airplane's total gas tank, affects and changes the calculation

the airplane decides which airport to choose by comparing the weight of each edge with the 500 km limit
the airplane tries to make it as close as possible to the 500 km
but will it be worth it aaaaaa
Dijkstra's algorithm but the limit is 500 km


steps:
1. clean up the csv file with all airports, only consider large and medium airports 
2. figure out if the airplane can go to any single airport from malpensa or if the airports have a connection hierarchy between them
3. create the function that gets the distance between 2 sets of alt, long, lat ()

phase 1: cleaning up the original data
getting only the records which actually interests the plane: large/medium
from these records the only attributes the plane cares about is: "id","ident","type","name","latitude_deg","longitude_deg","elevation_ft","continent","iso_country","iso_region","municipality",
"iata_code" (MXP)
if the record doesn't have a iata_code but it has a name (plus it has everything else), we consider it.
the only attributes which CANNOT be null are "latitude_deg","longitude_deg","elevation_ft"




The project will be evaluated based on the following criteria, each designed to assess a key skill covered in the course.
1. GitHub Usage

This criterion assesses your ability to use Git and GitHub for version control, a fundamental practice in modern software and data science development. The project should be hosted in a GitHub repository with: a clear and informative README.md file, explaining what the project is about, listing important information (e.g., data sources, libraries), and providing clear instructions on how to setup and run the code; a well-configured .gitignore file to exclude unnecessary files; a meaningful commit history, with frequent and atomic commits, having descriptive messages.
2. Project Organization

This criterion evaluates the structure and quality of your codebase. A well-organized project should: be logically organized into modules/scripts; have functions and classes with clear docstrings explaining their purpose, parameters, and return values; respect Python style guide, using consistent naming conventions, proper indentation, and clear variable names; provide a requirements.txt file, listing all the necessary Python libraries and their versions.
3. Input/Output

This criterion assesses your ability to work with data from external sources. The project should successfully load data from at least one external source (e.g., CSV, JSON, Excel, a database, or an API). The chosen data source should be appropriate for the analytical goals of the project. The code should handle data loading cleanly, addressing possible errors. The project may also demonstrate output capabilities by saving or displaying results, such as a summary table or generated plots.
4. Data Manipulation

This criterion focuses on the core task of handling data, evaluating your ability to use a data manipulation library like pandas to clean, transform, reshape, and prepare your data for the analysis and visualization stages.
5. Scientific Computing

This criterion assesses your ability to perform numerical and statistical computations on your data, using libraries like numpy or scipy to extract quantitative insights, perform calculations, and prepare data for more complex modeling.
6. Visualisation

This criterion evaluates your ability to communicate your findings visually. This involves creating clear and informative plots that reveal patterns, trends, and insights using a visualisation library, such as matplotlib or seaborn.
7. Presentation

This criterion evaluates how your work is presented, either through a Jupyter notebook or a web application. The notebook or the application should use the code of your project (not duplicate it), and guide the audience through your analysis in a clear way. Wrapping your analysis in an interactive web application, using a framework like streamlit, is not mandatory but it is appreciated.


minimize for efficiency all of the airports/nodes just to be (id, lat, long)
starting from malpensa, get all possible locations it can go to aka use the halvesine function and eliminate any airport with >500 km distance away from malpensa
extractor.py function goes through the csv and makes a dictionary of all nodes/airports
graph = {
    4735: {
        "name": "Milan Malpensa",
        "latitude": 45.6306,
        "longitude": 8.72811,
        "country": "IT",
        "edges": []
    },

    1823: {
        "name": "Airport B",
        "latitude": 48.0,
        "longitude": 10.0,
        "country": "DE",
        "edges": []
    }
}
graph[4735]["edges"].append({
    "destination": 1823,
    "distance": 600
})
maybe also add a check if it's in a different country
{
    "destination": 1823,
    "distance": 600,
    "flight_time": 1.2,
    "customs_time": 1
}