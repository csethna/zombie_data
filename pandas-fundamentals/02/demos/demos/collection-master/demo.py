import pandas as pd
import os

# Load data for first time
df = pd.read_pickle(os.path.join('..', 'data_frame.pickle'))

# Demo 1
df.artist
artists = df['artist']
pd.unique(artists)
len(pd.unique(artists))

# Demo 2
s = df['artist'] == 'Bacon, Francis'
s.value_counts()

# Other way
artist_counts = df['artist'].value_counts()
artist_counts['Bacon, Francis']
