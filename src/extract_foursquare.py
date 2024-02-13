
# Libraries:

import requests
from pymongo import MongoClient
import json 

# Function:
def extract_foursquare(location, radius, query="" ,category = ""):
    
    """
    Search for places by distance on a circular boundary in ForeSquare API and returns a .json()
    Optional filter, venue and/or category can be added
    Response limited to 50 (maximum)

    :location: str : "latidude,longitude" around which to retrieve place information  eg. "43.37012643,-8,39114853"
    :radius: int : radius in meters.define the area to bias search results.  eg. 10000
    :query: str : OPTIONAL:  a string to be matched against all content for this place
    :category: int: OPTIONAL : returns FSQ Places matching the specified id categories
       see category taxonomy -->  https://location.foursquare.com/places/docs/categories

    """


    url = "https://api.foursquare.com/v3/places/search"

    params = {
        "query": query,
        "ll": location,
        "radius":radius,
        "categories":category,
        "limit":50,
        "sort":"DISTANCE"  #Por defecto relevancia. 
    }

    headers = {
        "Accept": "application/json",
        "Authorization": token
    }

    return requests.get(url, params=params, headers=headers).json()
