import pandas as pd
from SQLAlchemy import String, TEXT, INTEGER, Float, DECIMAL
url = 'https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv'
df = pd.read_csv(url)
df.head(3)