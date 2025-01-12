import pandas as pd
from sqlalchemy import create_engine, String , TEXT, INTEGER, Float, DECIMAL, BIGINT

#reading the data from the link
url='https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv'
df = pd.read_csv(url,sep=";", on_bad_lines='skip')

#df.head(3)

columnTypes = {'column_1': INTEGER, 
               'column_2': String, 
               'column_3': String, 
               'column_4': String, 
               'column_5': String,
               'column_6': String, 
               'column_7': Float,
               'column_8': Float, 
               'column_9': INTEGER, 
               'column_10': Float,
               'column_11': TEXT,
               'column_12': String, 
               'geo_punkt': DECIMAL}

# saving the table in sqlite database
df.to_sql('airports','sqlite:///airports.sqlite', if_exists='replace', index=False)


