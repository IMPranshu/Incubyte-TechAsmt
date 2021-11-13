from load_data import *
from clean_data import *
from connector import *

df = pd.read_sql('SELECT country FROM patients', con=hospital_database)
country_list = list(set(df.values.flatten())) # as 2D numpy array


for country in country_list:
        load_data(country)
    




