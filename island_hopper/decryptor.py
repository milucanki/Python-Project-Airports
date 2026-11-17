import pandas as pd

def GetCountry(inputCountry):
    """
    Function that takes the input the code of a country and outputs what is the name of the country.
    It is done by traversing the "countries.csv" and finding the record that contains the same country code as the input.
    Afterwards, from this row, the "name" attribute is selected and returned.
    """
    countries = pd.read_csv("data/countries.csv")

    inTableCheck = countries["code"] == inputCountry

    # If the table has any True value, corresponding to the input, then the output gets the value of the country.
    if inTableCheck.any():
        outputCountry = countries.loc[inTableCheck, "name"].iloc[0]
        return outputCountry

    # If not, then None is returned which means that the country code is unknown.
    return None

def GetRegion(inputRegion):
    """
    Function that takes the input the code of a region and outputs what is the name of the region.
    It is done by traversing the "regions.csv" and finding the record that contains the same region code as the input.
    Afterwards, from this row, the "name" attribute is selected and returned.
    """
    regions = pd.read_csv("data/regions.csv")

    inTableCheck = regions["code"] == inputRegion

    # If the table has any True value, corresponding to the input, then the output gets the value of the country.
    if inTableCheck.any():
        outputRegion = regions.loc[inTableCheck, "name"].iloc[0]
        return outputRegion

    # If not, then None is returned which means that the country code is unknown.
    return None

def IDToMunicipality(inputId):
    """
    Function that takes the input the ID of an airport and outputs what municipality it is from.
    It is done by traversing the "validAirports.csv" and finding the record that shares the same ID with the input one.
    Afterwards, from this row, the "municipality" attribute is selected and returned.
    """
    airports = pd.read_csv("data/validAirports.csv", keep_default_na=False)

    # Since the database already has an attribute that deals with the unique ID of each entry, Pandas will just use that row as the ID.
    by_id = airports.set_index("id")

    # Edge case to check if the value of the unknown ID is not in the database.
    if int(inputId) not in by_id.index:
        return None

    airportRecord = by_id.loc[int(inputId)]

    if airportRecord["municipality"] == "":
        return None

    return airportRecord["municipality"].lower()

def DecryptID(unknownId):
    """
    Function that gets an input the ID of an airport and returns in which municipality this airport is in.
    It checks the ID with each of the records of  the original airports.csv file and, when there is a match, it gives the municipality as an output.
    games = pd.read_csv("data/games.csv")
    """
    outputDictionary = {}
    airports = pd.read_csv("data/validAirports.csv", keep_default_na=False)
    by_id = airports.set_index("id")

    """
    Edge case to check if the value of the unknown ID is even in the database.
    If not, return None.
    """
    if int(unknownId) not in by_id.index:
        return None

    airport = by_id.loc[int(unknownId)]

    # Using a lambda function to decrypt every possible continent code.
    continentDecryptor = lambda x: "Europe" if x == "EU" else "Asia" if x == "AS" else "North America" if x == "NA" else "Oceania" if x == "OC" else "South America" if x == "SA" else "Africa" if x == "AF" else "Antarctica" if x == "AN" else "None"

    outputDictionary[airport["name"]] = {
        "iata_code": airport["iata_code"],
        "type": airport["type"],
        "country": GetCountry(airport["iso_country"]),
        "municipality": airport["municipality"],
        "region": GetRegion(airport["iso_region"]),
        "continent": continentDecryptor(airport["continent"]),
        "latitude": float(airport["latitude_deg"]),
        "longitude": float(airport["longitude_deg"])
    }

    return outputDictionary


def InputSelectorFunction():
    """
    Function that realizes which airport of origin the small airplane will start from and outputs the ID of that airport in order for the BFS and Dijkstra functions to use it.
    """
    ui = str(input("Enter a city origin: "))
    userInput = ui.lower()
    # Initializing a list in which the user will have to choose from.
    possibleOutputList = []

    airports = pd.read_csv("data/validAirports.csv", keep_default_na=False)

    # Checking the database to see if any keywords of the airports correlate to the user's input.
    for idAirports,airport in enumerate(airports["name"]):
        if userInput in airports["keywords"][idAirports].lower() or userInput in airport.lower():
            possibleOutputList.append([airport,airports["municipality"][idAirports], int(airports["id"][idAirports])])

    if possibleOutputList == []:
        print("Could not find any airports!")
        return None

    for index, port in enumerate(possibleOutputList, start=1):
        print("Choose from which airport you want to leave from: ")
        print(f"{index}. {port[0]} - {port[1]}")

    try:
        selectionIndex = int(input("Select an airport using the index: "))
        if selectionIndex < 1 or selectionIndex > len(possibleOutputList):
            raise ValueError
        selectedAirportId = str(possibleOutputList[selectionIndex - 1][2])
    except ValueError:
        print("Please choose a valid index!")
        return None
    
    return selectedAirportId

def OutputSelectorFunction():
    """
    Function that realizes which airport of destination the small airplane will arrive on and outputs the municipality name of it.
    """
    ui = str(input("Enter a city destination: "))
    userInput = ui.lower()

    airports = pd.read_csv("data/validAirports.csv", keep_default_na=False)
    isInDataBase = False
    
    # Checking the database to see if any keywords of the airports correlate to the user's input.
    for idAirports,airport in enumerate(airports["name"]):
        if userInput in airports["keywords"][idAirports].lower() or userInput in airport.lower():
            isInDataBase = True

    if isInDataBase:
        return userInput
    else:
        return None


def CalculateRouteTime(path, graphDict):
    """
    Function that takes as input the overall graph and a route in it and returns the time it takes for that route to happen.
    It just simply goes along the route and sums up the criterias that take time for the airplane (the actual distance, the refueling - 2, the customs).
    """
    totalTime = 0

    for index in range(len(path) - 1):
        # Initiating the 2 airports connected by an edge.
        currentAirport = path[index]
        nextAirport = path[index + 1]

        # Finding a corresponding edge.
        for edge in graphDict[currentAirport]["edges"]:
            if edge["destination"] == nextAirport:
                # Adds the time which was calculated when all of the edges were created to the total time.
                totalTime += edge["totalTime_hours"]

    # Adding the refueling at each airport - 2 (the airplane doesn't refuel at the origin and the end).
    totalTime += len(path) - 2

    return totalTime
