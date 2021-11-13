import pandas as pd
from load_data import *
from print_data import *

# List of Countries
data = pd.read_csv(
    "C:/Users/Specter/Desktop/Incubyte/python_code/country-codes.csv")
country_list = data['Alpha-3 code'].values


for country in country_list:
    print_data(country)
    load_data(country)
