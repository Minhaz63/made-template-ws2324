# Analyzing the changing pattern and relationship between road accidents and the average temperature of Germany.

The main Goal of the project is to find the relation between road accidents and temperature because in recent times road accidents have increased and the aim is to find the relation between temperature and the rate of accidents.

## Project Work
Datasource 1:Federal Statistical Office of Germany
Metadata URL 1: https://www.destatis.de/
Data URL 1: https://www-genesis.destatis.de/genesis/online?language=en&sequenz=statistikTabellen&selectionname=46241#abreadcrumb
Data Type: CSV The road accident data in Germany. This data also shows the accidents in Indoor and outdoor as well.
Datasource 2:climate_environment/CDC/
Metadata URL: https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/
Data URL: https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_01.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_02.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_03.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_04.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_05.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_06.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_07.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_08.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_09.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_10.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_11.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_12.txt

Data Type: txt

License Type: OpenData License

This is monthly average air temparature in Germany. In this dataset it also shows that the temparature in state wise.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to html: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`

# Final Report: 
Link: "https://github.com/Minhaz63/made-template-ws2324/blob/main/project/report.ipynb"

## Exercises
During the semester you will need to complete exercises, sometimes using [Python](https://www.python.org/), sometimes using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.<jv or py>`.

In regular intervalls, exercises will be given as homework to complete during the semester. We will divide you into two groups, one completing an exercise in Jayvee, the other in Python, switching each exercise. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. Exercise 1: https://github.com/Minhaz63/made-template-ws2324/blob/main/exercises/exercise1.py
2. Exercise 2: https://github.com/Minhaz63/made-template-ws2324/blob/main/exercises/exercise1.jv
3. Exercise 3: https://github.com/Minhaz63/made-template-ws2324/blob/main/exercises/exercise1.py
4. Exercise 4: https://github.com/Minhaz63/made-template-ws2324/blob/main/exercises/exercise1.jv
5. Exercise 5: https://github.com/Minhaz63/made-template-ws2324/blob/main/exercises/exercise1.py

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
