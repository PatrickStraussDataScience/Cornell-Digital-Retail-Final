import pandas as pd

# Load the incoming_rides.csv dataset
incoming_rides = pd.read_csv(r"C:\Users\Patrick\Downloads\incoming_rides.csv")

# Calculate the count of start station IDs
start_station_counts = incoming_rides.groupby('end station id').size().reset_index(name='start_station_count')

# Calculate the percentiles of start station counts
low_threshold = start_station_counts['start_station_count'].quantile(0.33)
high_threshold = start_station_counts['start_station_count'].quantile(0.66)

# Classify stations based on start station counts
start_station_counts['incoming_demand_level'] = pd.cut(
    start_station_counts['start_station_count'],
    bins=[float('-inf'), low_threshold, high_threshold, float('inf')],
    labels=['Low', 'Medium', 'High']
)

# Merge the classification back to the original dataset
incoming_rides = incoming_rides.merge(start_station_counts, how='left', on='end station id')

# Save the updated dataset to a new CSV file
incoming_rides.to_csv(r"C:\Users\Patrick\Downloads\incoming_rides_with_demand.csv", index=False)
