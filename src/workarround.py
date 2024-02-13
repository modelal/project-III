from folium.plugins import HeatMap
from pymongo import MongoClient
import requests
import json
import pandas as pd
import numpy as np
from getpass import getpass
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster

#FUNCTIONS:

#   heat_map: creates a heat map given a df with locations
#   extract_parameters: formates response data json to dictionary
#   city_places: creates a data frame for the extracted locations
#   icon_set: set icon specifications
#   city_markers: adds markers to a map given a df of locations


def heat_map(df, to_map):
    
    HeatMap(data = df[["latitude", "longitude"]]).add_to(to_map)
        
    return

def extract_parameters(i):
            
            name = i["name"]
            
            lat = i["geocodes"]["main"]["latitude"]
            lon = i["geocodes"]["main"]["longitude"]
            
            #can have more than one:
            cat_list = [x["id"] for x in i["categories"]]
            
            try:
                city = i["location"]["locality"]
            except KeyError:
                city = np.nan
            
            params = {"city":city, "name": name, "cat_code":cat_list, "lat":lat, "lon":lon}
            
            return params


def city_places(city):
    
    "Returs a dataframe with all palces inside a city from our DB"
    
    c = access_mdb_local_collection ("ironhack", "foursquare")
    
    # 1. Set the filter to the objects
    filt = {"location.locality":city}
    
    # 2. Select the filds that we want to target:
    projection = { "_id":0,"categories":1, "geocodes":1,"name":1, "location":1}
    
    # 3. Extract data
    datos = list(c.find(filt,projection))
    
    # 4. Generate an empty dictionary with the categories to save:
    register = {"city": [], "place_name":[], "categories":[],"lat":[], "lon":[]}
    
    # 5. Iterate trowh all elements found:
    for i in datos:

        info = extract_parameters(i) # info it's a dictionary 
        
        register["city"].append(info["city"])
        register["place_name"].append(info["name"])
        register["categories"].append(info["cat_code"])
        register["lat"].append(info["lat"])
        register["lon"].append(info["lon"])

    df = pd.DataFrame(register)
    
    return df


def icon_set(category_code, tags): 
    
    icon =  Icon(
            color = tags[category_code][1], #red
            icon_color = tags[category_code][2], #black
            icon = tags[category_code][3], #dog
            prefix="fa" # font-awesome website: fa
                )
            
    return icon

def city_markers(df, to_map, tags):
    
        for index, row in df.iterrows():
            
            
            # What if there is no categorie?
    
            if df.iloc[index]["categories"] != []: #--> If it's not empty - take the list 
                
                cat_list = df.iloc[index]["categories"] 
                
                 # What category select? ?
                    
                for key in tags: # --> tags = the ones we have defined
                    if key in cat_list:    
                        category_code = key  # --> we kep the category 
                    else:
                        continue # --> There is no a matching category --> skip  
            else: 
                continue # --> There is no category --> skip 

           
            
            lable =  df.iloc[index]["place_name"]
            
            """ Error that i dont understand -- Investigate """
            
            try:
                #Set the icon for that kind of place:
                icon_conf = icon_set(category_code, tags)
            except UnboundLocalError: # No idea de que es 
                continue
            
            #Extract position in witch locates:
            lat = df.iloc[index]["lat"]
            lon = df.iloc[index]["lon"]
            coordenates = [lat, lon]
            
            #Set the marker:
            marker = Marker(coordenates, tooltip=lable ,  icon=icon_conf)
            
            marker.add_to(to_map)
        
        return


