import json
import pandas as pd

# Example usage from_records method
records = [("Espresso", "5$"), ("Flat White", "10$")]

pd.DataFrame.from_records(records)

pd.DataFrame.from_records(records, columns=["Coffee", "Price"])

#####
KEYS_TO_USE = ['id', 'all_artists', 'title', 'medium', 'dateText', 'acquisitionYear', 'height', 'width', 'units']

def get_record_from_file(file_path, KEYS_TO_USE):
    with open(file_path) as artwork_file:
        content = json.load(artwork_file)

    record = []
    for field in KEYS_TO_USE:
        record.append(content[field])

    return tuple(record)

# Single file processing function demo
SAMPLE_JSON = os.path.join('..', 'collection-master', 'artworks', 'a', '000', 'a00001-1035.json')

sample_record = get_record_from_file(SAMPLE_JSON, KEYS_TO_USE)
