import pandas as pd

# Load your spreadsheet data into a DataFrame
df = pd.read_csv(r"C:\Users\Patrick\Downloads\BIKEDATASET3.csv")

# Filter the data to only include rows where the start station name is "MIT at Mass Ave / Amherst St"
mit_data = df[df['start station name'] == "MIT at Mass Ave / Amherst St"]

# Convert 'starttime' and 'stoptime' columns to datetime objects
mit_data['starttime'] = pd.to_datetime(mit_data['starttime'])
mit_data['stoptime'] = pd.to_datetime(mit_data['stoptime'])

# Group the data by day and calculate inflow, outflow, and net demand for each day
mit_data['date'] = mit_data['starttime'].dt.date
daily_data = mit_data.groupby('date').agg({
    'starttime': 'count',  # Count of trips as inflow
    'stoptime': lambda x: len(x.unique()),  # Count of unique bikes as outflow
}).rename(columns={'starttime': 'inflow', 'stoptime': 'outflow'})
daily_data['net_demand'] = daily_data['inflow'] - daily_data['outflow']

# Calculate mean and standard deviation of inflow, outflow, and net demand per day
mean_inflow = daily_data['inflow'].mean()
std_inflow = daily_data['inflow'].std()
mean_outflow = daily_data['outflow'].mean()
std_outflow = daily_data['outflow'].std()
mean_net_demand = daily_data['net_demand'].mean()
std_net_demand = daily_data['net_demand'].std()

# Determine the number of time periods per day
num_time_periods_per_day = mit_data['starttime'].dt.hour.nunique()  # Number of unique hours

print("Mean Inflow per day:", mean_inflow)
print("Standard Deviation of Inflow per day:", std_inflow)
print("Mean Outflow per day:", mean_outflow)
print("Standard Deviation of Outflow per day:", std_outflow)
print("Mean Net Demand per day:", mean_net_demand)
print("Standard Deviation of Net Demand per day:", std_net_demand)
print("Number of Time Periods per day:", num_time_periods_per_day)
