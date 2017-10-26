import numpy as np
import pandas as pd
import datetime
import urllib

from bokeh.plotting import *
from bokeh.models import HoverTool
from collections import OrderedDict

# Read in our data. We've aggregated it by date already, so we don't need to worry about paging
query = ("https://data.lacity.org/resource/mgue-vbsx.json?"
    "$group=date"
    "&call_type_code=507P"
    "&$select=date_trunc_ymd(dispatch_date)%20AS%20date%2C%20count(*)"
    "&$order=date")
raw_data = pd.read_json(query)

# Augment the data frame with the day of the week and the start of the week that it's in.
# This will make more sense soon...
raw_data['day_of_week'] = [date.dayofweek for date in raw_data["date"]]
raw_data['week'] = [(date - datetime.timedelta(days=date.dayofweek)).strftime("%Y-%m-%d") for date in raw_data["date"]]

# Pivot our data to get the matrix we need
data = raw_data.pivot(index='week', columns='day_of_week', values='count')
data = data.fillna(value=0)

# Get our "weeks" and "days"
weeks = list(data.index)
days = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
