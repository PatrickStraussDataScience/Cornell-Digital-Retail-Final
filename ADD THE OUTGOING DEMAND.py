import pandas as pd

# Load the outgoing_rides.csv dataset
outgoing_rides = pd.read_csv(r"C:\Users\Patrick\Downloads\outgoing_rides.csv")

# Calculate the count of end station IDs
end_station_counts = outgoing_rides.groupby('start station id').size().reset_index(name='end_station_count')

# Calculate the percentiles of end station counts
low_threshold = end_station_counts['end_station_count'].quantile(0.33)
high_threshold = end_station_counts['end_station_count'].quantile(0.66)

# Classify stations based on end station counts
end_station_counts['outgoing_demand_level'] = pd.cut(
    end_station_counts['end_station_count'],
    bins=[float('-inf'), low_threshold, high_threshold, float('inf')],
    labels=['Low', 'Medium', 'High']
)

# Merge the classification back to the original dataset
outgoing_rides = outgoing_rides.merge(end_station_counts, how='left', on='start station id')

# Save the updated dataset to a new CSV file
outgoing_rides.to_csv(r"C:\Users\Patrick\Downloads\outgoing_rides_with_demand.csv", index=False)
