import pandas as pd 
from dotenv import dotenv_values 
env = dotenv_values('Data Analytics Practice/Refreshing/credentials.env')

file_path = env.get('file')
# print(file_path)

df = pd.read_csv(file_path)

print(df.head())
print(df.info())

df['Order Date'] = pd.to_datetime(df['Order Date'])
print(df.info())
print(df.head())