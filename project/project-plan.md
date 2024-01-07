# Project Plan
The main Goal of the project is to find the relation of road accident and the temparature because in recent times the road accident has incresed and the aim is to find the relation between temparature and the rate of the accident.
## Title
<!-- Give your project a short title. -->
Analyzing the changing pattern and realtionship of road accident and the average temparature of Germany.
## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. The changes of the temparature
2. How the rate of road accident increasing day by day?
3. Is there any realtion between road accident and the temparature?


## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
I will try to find the dataset and make some preprocessing such as removing null values, i have the data of average temparature daily and I have the monthly data of accident, so I have to make it average and see the changes of temparature and the changes of road accident and see the relations.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource 1:Federal Statistical Office of Germany
* Metadata URL 1: https://www.destatis.de/
* Data URL 1: https://www-genesis.destatis.de/genesis/online?language=en&sequenz=statistikTabellen&selectionname=46241#abreadcrumb
* Data Type: CSV
The road accident data in Germany. This data also shows that the accident in Indoor and outdoor as well.


### Datasource 2:climate_environment/CDC/

* Metadata URL: https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/
* Data URL: https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_01.txt
            https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_02.txt
            https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_03.txt
            https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_04.txt
            https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_05.txt
            https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_06.txt
            https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_07.txt
            https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_08.txt
            https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_09.txt
            https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_10.txt
            https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_11.txt
            https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_12.txt
* Data Type: txt
* License Type: OpenData License

This is monthly average air temparature in Germany. In this dataset it also shows that the temparature in state wise. 


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Data collection and Pre-processing [#1][i1]
2. Feature engineering [#2][i2]
3. Statistical modeling [#3][i3]
4. Interpretation and insights [#4][i4]
5. Reporting on findings [#5][i5]
