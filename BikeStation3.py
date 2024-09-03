import folium
import geopandas as gpd
from shapely.geometry import Point
import pandas as pd

# Define CSV file path
csv_file = r"C:\Users\Patrick\Downloads\CombinedTripsDataCLEANED.csv"

# Define columns to read
columns_to_read = ['start station latitude', 'start station longitude', 'start station name']

# Read the CSV file into a DataFrame
print("1. Reading the CSV file into a DataFrame...")
data = pd.read_csv(csv_file, usecols=columns_to_read)

# Calculate the count of each station
station_counts = data['start station name'].value_counts()

# Drop duplicates to get unique station coordinates
print("2. Selecting distinct start station names...")
stations = data.drop_duplicates(subset=['start station latitude', 'start station longitude']).copy()

# Add a new column for marker size based on station counts
stations['marker_size'] = stations['start station name'].map(station_counts)

# Normalize marker sizes
max_size = stations['marker_size'].max()
stations['marker_size'] = stations['marker_size'] / max_size * 20  # Adjust the multiplier for appropriate scaling

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

# Add bike stations to the map with marker size based on count
for idx, row in gdf.iterrows():
    folium.CircleMarker(location=[row['start station latitude'], row['start station longitude']],
                        radius=row['marker_size'],
                        popup=row['start station name'],
                        fill=True,
                        color='blue').add_to(m)

# Display the map
m.save(r"C:\Users\Patrick\Downloads\bike_stations_map5.html")

print('6. Finito')
