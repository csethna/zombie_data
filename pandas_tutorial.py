import pandas as pd
import numpy as np

# np.array / np.ndarray - sibling datatypes Pandas uses heavily; 'nd' = 'n dimensional'
# pd.Series - represents datasets in a single column
# pd.DataFrame - multi-column data

### Code snippets:
my_numpy_array = np.random.rand(3) # 3-element ndarray (random)
my_first_series = pd.Series(np.random.rand(3)) # Series always has one column
my_first_df = pd.DataFrame(np.random.rand(3, 2)) # Two columns with random numbers

# https://app.pluralsight.com/library/courses/pandas-fundamentals/exercise-files
