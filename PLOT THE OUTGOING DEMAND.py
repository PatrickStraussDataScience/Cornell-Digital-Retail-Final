import pandas as pd
import matplotlib.pyplot as plt

# Load the classified_outgoing_rides.csv dataset
classified_outgoing_rides = pd.read_csv(r"C:\Users\Patrick\Downloads\outgoing_rides_with_demand.csv")
classified_incoming_rides = pd.read_csv(r"C:\Users\Patrick\Downloads\incoming_rides_with_demand.csv")

# Group the data by 5-minute intervals under 'discrete_start_time' column and count the number of rides
ride_counts1 = classified_outgoing_rides.groupby('discrete_start_time').size()
ride_counts2 = classified_incoming_rides.groupby('discrete_stop_time').size()

# Plot the count of rides against the 5-minute intervals
plt.figure(figsize=(10, 6))
ride_counts1.plot(kind='line', marker='o', color='b', linestyle='-')
ride_counts2.plot(kind='line', marker='o', color='r', linestyle='-')
plt.title('Amount of Outgoing/Incoming Rides Grouped by 5-Minute Intervals')
plt.xlabel('Time')
plt.ylabel('Count of Rides')
plt.grid(True)
plt.show()
