import pandas as pd
import os

# Where our data lives
CSV_PATH = os.path.join('..', 'collection-master', 'artwork_data.csv')

# Read just 5 rows to see what's there
df = pd.read_csv(CSV_PATH, nrows=5)

# Specify an Index
df = pd.read_csv(CSV_PATH, nrows=5, index_col='id')

print(df)
