import numpy as np
"""
Distance between two points on Earth, calculated with the Haversine formula.
"""
def haversineFormula(lat_origin,long_origin,lat_dest,long_dest):
    """
    This function gets as input the 2 pairs of latitude and longitude of the origin airport and the destination airport and returns the distance between them in kilometers.
    This is done using the Haversine Formula which is:

    A = 0.5 - cos((Latitude of Destination-Latitude of Origin) * Half of Pi) /2 + cos(Latitude of Origin * Half of Pi)*cos(Latitude of Destination * Half of Pi) * 
        * (1-cos((Longitude of Destination - Longitude of Origin)* Half of Pi)) / 2
    Distance between 2 Airports = 2 * Radius of Earth * asin(sqrt(A))
    """
    # Initializing the variables needed for the formula
    earthRadius = 6371
    halfPi = np.pi / 180

    deltaLat, deltaLong = lat_dest-lat_origin, long_dest-long_origin

    # First part of the formula
    a = 0.5 - np.cos((deltaLat)*halfPi)/2 + np.cos(lat_origin*halfPi)*np.cos(lat_dest*halfPi) * (1-np.cos((deltaLong)*halfPi)) / 2

    # Second part of the formula
    outputDistance = 2 * earthRadius * np.asin(np.sqrt(a))

    return outputDistance