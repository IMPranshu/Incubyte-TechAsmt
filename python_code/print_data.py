from extract_data import *

def print_data(country):
    data = df.loc[df['Country'] == country]
    print(data)
