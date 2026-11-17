import math

"""
This function gets as input the 2 pairs of latitude and longitude of the origin airport and the destination airport and outputs the distance between them in kilometers.
This is done using the Haversine Formula which is:

A = 0.5 - cos((Latitude of Destination-Latitude of Origin) * Half of Pi) /2 + cos(Latitude of Origin * Half of Pi)*cos(Latitude of Destination * Half of Pi) * 
    * (1-cos((Longitude of Destination - Longitude of Origin)* Half of Pi)) / 2
    
Distance between 2 Airports = 2 * Radius of Earth * asin(sqrt(A))
"""
def haversineFormula(lat_origin,long_origin,lat_dest,long_dest):
    # Initializing
    earthRadius = 6371
    halfPi = math.pi/180

    deltaLat = lat_dest-lat_origin

    deltaLong = long_dest-long_origin

    # First part of the formula
    a = 0.5 - math.cos((deltaLat)*halfPi)/2 + math.cos(lat_origin*halfPi)*math.cos(lat_dest*halfPi) * (1-math.cos((deltaLong)*halfPi)) / 2

    # Second part of the formula
    outputDistance = 2 * earthRadius * math.asin(math.sqrt(a))

    return outputDistance