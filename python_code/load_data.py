from extract_data import *

def load_data(country):
    data = df.loc[df['Country'] == country]
    file_name = str(country)
    data.to_csv('C:/Users/Specter/Desktop/Incubyte/data/' +
                file_name + '.csv')  # savepath
    print("Data loading done.")
