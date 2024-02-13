from folium.plugins import HeatMap
    
def heat_map(df, to_map):
    
    HeatMap(data = df[["latitude", "longitude"]]).add_to(to_map)
        
    return