# Import CPL wifi sessions to Pandas DataFrame
import pandas as pd
import os

# Specify the data source
CSV_PATH = os.path.join('Libraries_-_2017_Wi_Fi_Usage.csv')
# Create the DataFrame
df = pd.read_csv(CSV_PATH)
# Save DataFrame to .pickle for later
df.to_pickle(os.path.join('wifi_sessions.pickle'))

# Import CPL computer sessions by location to DataFrame
CSV_PATH = os.path.join('Libraries_-_2017_Computer_Sessions_by_Location.csv')
# Create the DataFrame with 'LOCATION' as the index column
df = pd.read_csv(CSV_PATH, index_col='LOCATION')
# Save DataFrame to .pickle for later
df.to_pickle(os.path.join('computer_sessions.pickle'))
