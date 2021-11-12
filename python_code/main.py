from load_data import *
from print_data import *

# List of the Required Countries
country_list = ["NYC", "USA", "IND", "PHIL", "AU"]

for country in country_list:
    print_data(country)
    load_data(country)
