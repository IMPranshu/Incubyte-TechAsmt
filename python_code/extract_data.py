import pandas as pd
from connector import *

# fitting into pandas dataframe
df = pd.read_sql('SELECT * FROM patients', con=hospital_database)
# set customer id as default index
df.set_index(['cust_ID'], inplace=True)
