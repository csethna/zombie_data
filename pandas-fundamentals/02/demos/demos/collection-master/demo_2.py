import json
import pandas as pd

# Example usage from_records method
records = [("Espresso", "5$"), ("Flat White", "10$")]

pd.DataFrame.from_records(records)

pd.DataFrame.from_records(records, columns=["Coffee", "Price"])

#####
KEYS_TO_USE = ['id', 'all_artists', 'title', 'medium', 'acquisitionYear', 'height', 'width']
