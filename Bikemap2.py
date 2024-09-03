import folium
import geopandas as gpd
from shapely.geometry import Point
import pandas as pd

# Define CSV file path
csv_file = r"C:\Users\Patrick\Downloads\CombinedTripsData3.csv"

# Define columns to read
columns_to_read = ['start station latitude', 'start station longitude', 'start station name']

# Read the CSV file into a DataFrame
print("1. Reading the CSV file into a DataFrame...")
data = pd.read_csv(csv_file, usecols=columns_to_read)

# Drop duplicates
print("2. Selecting distinct start station names...")
stations = data.drop_duplicates()

# Create Point geometries from the coordinates
print("3. Creating Point geometries from the coordinates...")
geometry = [Point(xy) for xy in zip(stations['start station longitude'], stations['start station latitude'])]

# Create a GeoDataFrame with Point geometries
print("4. Creating a GeoDataFrame with Point geometries...")
gdf = gpd.GeoDataFrame(stations, geometry=geometry, crs="EPSG:4326")

# Create a Folium map centered at a location
m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)  # Boston coordinates

# Add roads to the map
folium.TileLayer('openstreetmap').add_to(m)

# Add bike stations to the map
for idx, row in gdf.iterrows():
    folium.Marker([row['start station latitude'], row['start station longitude']], popup=row['start station name']).add_to(m)

# Display the map
m.save("bike_stations_map.html")

print('6. Finito')
