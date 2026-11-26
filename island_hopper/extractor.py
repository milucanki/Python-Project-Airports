
import csv
from .haversine import haversineFormula as haversine
import os
"""
Cleans the OurAirports data and builds the airport graph: airports are nodes and flights within the plane's range are weighted edges.
"""

# Defining project and CSV paths.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ORIGINAL_CSV = os.path.join(PROJECT_ROOT, "data", "airports.csv")
VALID_CSV = os.path.join(PROJECT_ROOT, "data", "validAirports.csv")

def cleanAirports():
    """
    Function that returns the length of the final valid database.
    Starting by cleaning the original CSV file. Since the project does not require all of the attributes of the CSV file, a new CSV file will be created which only contains the 
    neccesary attributes. The final, usable CSV file will need all of its attributes to have a value.
    """
    validAirportsList = []
    with open(ORIGINAL_CSV, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=",")

        # Argument used to append and skip the row that contains the attribute names.
        validAirportsList.append(next(reader))

        # Getting a list with all of the valid rows.
        for validRow in reader:
            # Making sure that the neccessary attributes are not empty.
            recordId, airportId, airportType, airportName, airportLatitude, airportLongitude, airportAltitude, airportContinent, airportCountry, airportRegion, airportMunicipality, airportIataCode = validRow[0],validRow[1],validRow[2],validRow[3],validRow[4],validRow[5],validRow[6],validRow[7],validRow[8],validRow[9],validRow[10],validRow[13]
            emptyAttributesCheck = recordId == "" or airportId == "" or airportName == "" or airportLatitude == "" or airportLongitude == "" or airportContinent == "" or airportCountry == "" or airportRegion == "" or airportMunicipality == "" or airportIataCode == ""
            # Only checking for medium or large airports because those are the only airports the plane can land on.
            if airportType == "medium_airport" or airportType == "large_airport":
                if not(emptyAttributesCheck):
                    validAirportsList.append(validRow)

    # Writing the list into the final CSV file, which will be used later.
    with open(VALID_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(validAirportsList)

    return len(validAirportsList) - 1

def extractValidAirports():
    """
    This function takes the attributes from the valid aiport CSV file and inserts them into a dictionary in a specific format, returning them.
    """
    outputNodesDictionary = {}
    with open(VALID_CSV, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=",")
        # Skipping the attributes names row.
        next(reader)
        for row in reader:
            idNode, nameNode, latNode, longNode, countryNode, continentNode = row[0],row[3],row[4],row[5],row[8],row[7]
            # The specific dictionary format. The key of each entry is the ID of that airport and the value of the key is a dictionary that contains the information of that airport.
            # The "edges" key's values will be a list of all possible airports that the small airplane can fly to based on the fuel tank / max range that it has.
            # The latitude and the longitude must have the float data type in order to make the Haversine formula output a result that is as accurate as possible.
            outputNodesDictionary[idNode] = {
                "name": nameNode,
                "latitude": float(latNode),
                "longitude": float(longNode),
                "country": countryNode,
                "continent": continentNode,
                "edges": []
            }
    return outputNodesDictionary

def edgesPopulator(nodesDict, maxRange):
    """
    Based on the fuel tank / max range of the airplane, this function populates the "edges" key's value from extractValidAirports()'s output with all of the possible other airports
    the plane can go to from the current one it is at. The output of this function creates a "graph" with the airports as nodes and the distances between the airports as weighted edges 
    (the weight being the time it takes to fly from one airport to another + customs + refuelling).
    """

    # Using a lambda function in order to check if the country of the origin airport is the same as the country of the destination airport
    # If they are the same, then 1 (hour) isn't added to the total time it takes for this edge between these 2 nodes.
    # Else, 1 is added.
    isCountryDifferent = lambda firstCountry,secondCountry: 1 if firstCountry != secondCountry else 0

    # Putting all of the airport IDs in the airportIds list
    airportIds = list(nodesDict.keys())

    # Iterating through every airport, including the list index of them.
    for indexOrigin, idOrigin in enumerate(airportIds) :
        
        # Getting the original airport's information.
        airportSpecsValue = nodesDict[idOrigin]
        latitudeOrigin,longitudeOrigin, countryOrigin, edgesOrigin = airportSpecsValue["latitude"], airportSpecsValue["longitude"], airportSpecsValue["country"],airportSpecsValue["edges"]

        # Only iterate through the airports appearing after the current origin.
        # This happens because when there is an edge between a starting airport and a destination airport, it will get placed in the starting airport's "edges" list, but the airplane can also
        # come from the destination airplane (in the future) to the starting airplane. The graph is undirected.
        # It avoids comparing the same airport pair twice.
        for idDestination in airportIds[indexOrigin+1:]:

            specsDestination = nodesDict[idDestination]

            latitudeDestination, longitudeDestination, countryDestination, edgesDestination = specsDestination["latitude"], specsDestination["longitude"], specsDestination["country"], specsDestination["edges"]
            
            distanceBetweenAirports = haversine(latitudeOrigin,longitudeOrigin,latitudeDestination,longitudeDestination)
            
            if distanceBetweenAirports <= maxRange:
                # If the distance between the airports is smaller or equal to than the max range that the airplane can travel, then it is considered as a valid edge between the 2 airports/nodes.
                # The edge is added to the possible edge dictionary of the origin node and the destination one also.
                # The time is also taken in account for. The small plane takes 1 hour every 500 km, takes 1 hour for refuelling at each airport and has to do customs, if neccesary.
                airportSpecsValue["edges"].append({
                    "destination": idDestination,
                    "distance": distanceBetweenAirports,
                    "duration_hours": distanceBetweenAirports/500,
                    "customs_hour": isCountryDifferent(countryOrigin,countryDestination),
                    "totalTime_hours": isCountryDifferent(countryOrigin,countryDestination)+distanceBetweenAirports/500
                })

                specsDestination["edges"].append({
                    "destination": idOrigin,
                    "distance": distanceBetweenAirports,
                    "duration_hours": distanceBetweenAirports/500,
                    "customs_hour": isCountryDifferent(countryOrigin,countryDestination),
                    "totalTime_hours": isCountryDifferent(countryOrigin,countryDestination)+distanceBetweenAirports/500
                })
    return nodesDict

