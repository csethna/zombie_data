# Import CPL wifi sessions to Pandas DataFrame
import pandas as pd
import os

CSV_PATH = os.path.join('Libraries_-_2017_Wi_Fi_Usage.csv')

df = pd.read_csv(CSV_PATH)

print(df)

df.to_pickle(os.path.join('wifi_sessions.pickle'))
