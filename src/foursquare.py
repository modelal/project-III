
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


def insert_unique_parents(response, mdb_collection):
    
    """
    Inserts the results of a reques that ARE NOT in the 
    given collection AND ARE NOT related to other object(childrens)

    response: --- : what to insert
    collection: ----: where to insert it
    """
    
    # 1. set conter for inserted objects
    inserted = 0
    
    # 3. Get the list of all elements alrready registered in the collection
    registered = [i['fsq_id'] for i in collection.find({}, {"_id":0,"fsq_id":1})]
    
    # 4. Iterate trough all elements of the response 
    for i in response["results"]:
        
        #Need to meet 2 conditions to be inserted:
        # It is not alrready registered:
        cond1 = i['fsq_id'] not in registered
        
        ## It's not a children of a parent:
        cond2 = "parent" not in list(i["related_places"].keys())
        
        # Check if the conditions are meet:
        if cond1 and cond2 == True:
            collection.insert_one(i)
            inserted += 1
            
    print(f'{inserted} items inserted into the collection')
               
    return