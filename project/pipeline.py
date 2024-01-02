import pandas as pd
from sqlalchemy import create_engine

class Pipeline:
    def __init__(self):
        self.engine = create_engine('sqlite:///FinalDB.sqlite')

    def fetch_temperature_data(self):
        # Define the list of URLs
        url_list = [
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_01.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_02.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_03.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_04.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_05.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_06.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_07.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_08.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_09.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_10.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_11.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_12.txt",  
        ]

        # Initialize an empty list to store the DataFrames
        dfs = []

        # Loop through each URL and read data into a DataFrame
        for url in url_list:
            # Use pd.read_csv to read data from the URL
            data = pd.read_csv(url, sep=';', skiprows=1, skipfooter=0)
            dfs.append(data)

        # Concatenate the list of DataFrames into a single DataFrame
        df_combined = pd.concat(dfs, ignore_index=True)

        # Filter the combined DataFrame
        df_filtered = df_combined[(df_combined['Jahr'] >= 2018) & (df_combined['Jahr'] <= 2020)]
        df_sorted = df_filtered.sort_values(by=['Jahr', 'Monat'])

        # Display the combined and filtered DataFrame
        #print(df_sorted)

        # Store the temperature data in the database
        df_sorted.to_sql('AvgTemp', self.engine, if_exists='replace', index=False)

    def fetch_additional_data(self):
        # Fetch additional data from another URL
        url2 = "https://www-genesis.destatis.de/genesisWS/rest/2020/data/tablefile?username=DE6M7SBAY6&password=Minhaz.123456&name=46241-0002&area=all&compress=false&transpose=false&startyear=2018&endyear=2020&language=en"
        data1 = pd.read_csv(url2, sep=';', skiprows=6, skipfooter=3, engine='python')
        df = data1
        df_transposed = df.T

        # Store the additional data in the same database
        df_transposed.to_sql('AccData', self.engine, if_exists='replace', index=False)
        self.engine.dispose()
        

    def run_pipeline(self):
        # Run the entire pipeline
        self.fetch_temperature_data()
        self.fetch_additional_data()

# Create an instance of the Pipeline class
pipeline_instance = Pipeline()

# Run the pipeline
pipeline_instance.run_pipeline()
