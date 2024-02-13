from pymongo import MongoClient
import requests
import json
import pandas as pd
from getpass import getpass
import os

import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster


import src.acces_mdb_local_collection as access 
import src.extract_foursquare as extract
import src.heat_map as heat
import src.insert_unique_parents as insert

"""ESTO FUNCIONA TE SACA EL MAPA DE EUROPA """

from dotenv import load_dotenv
load_dotenv()

token = os.getenv("token_monica")

# 1. MONGO - COMPANIES:

# Acces Mongo DB coll
#ection : companies
c = access.access_mdb_local_collection("ironhack", "companies")

# Locate videogames companies
null = {"$type":10}
cond1 = {"offices.latitude": {"$exists": True, "$ne": null}}
cond2 = {"offices.longitude": {"$exists": True, "$ne": null}}
cond3 = {"category_code" :"games_video"}
filter_ = {"$and":[cond1, cond2, cond3]}
projection = {
        "_id":0, 
        "name":1, 
        "category_code":1,
        "offices.latitude":1,
        "offices.longitude":1
}

datos = c.find(filter_ ,projection)

# Create a DF:
df = pd.DataFrame(list(datos))

#Tranform the DF
df["latitude"] = df["offices"].apply(lambda x : x[0]["latitude"])
df["longitude"] = df["offices"].apply(lambda x : x[0]["longitude"])
df.dropna(subset=['latitude'], inplace=True)
df.dropna(subset=['offices'], inplace=True)

# Generate and save the heat map:
eu = [50.3785,14.9706]
eu_map = Map(eu, zoom_start=4, tiles='CartoDB positron')
heat.heat_map(df, eu_map)
path = "output/europe_heatmap.html"
eu_map.save(path)
os.system(f"open {path}")

#Never finish this, sotty not sorry - you can look the code process in notebooks

# 2. Spain-Univesities
# 3. Citys-Sport_dogs_vegan
# 4. Madrid-Spot
