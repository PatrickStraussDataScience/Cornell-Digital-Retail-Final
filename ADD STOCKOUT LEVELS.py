import pandas as pd

# Load the dataset containing depletion status values
df = pd.read_csv(r"C:\Users\Patrick\Downloads\stockout_risk5.csv")

bikes = df['depletion_status']

# Classify stations based on depletion status
def classify_stockout_risk(bikes):
    if bikes > 9.0:
        return 'low'
    elif bikes < 1.5:
        return 'high'
    else:
        return 'Medium'

# Add the 'stockout_risk' variable to the dataset
df['stockout_risk'] = df['depletion_status'].apply(classify_stockout_risk)

# Save or display the updated dataset
df.to_csv(r"C:\Users\Patrick\Downloads\stockout_risk_classification6.csv", index=False)
print(df)
