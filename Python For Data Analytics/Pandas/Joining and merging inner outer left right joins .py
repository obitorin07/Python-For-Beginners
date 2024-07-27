import pandas as pd

# Load the datasets
df1 = pd.read_csv('employee_details.csv')
df2 = pd.read_csv('employee_salaries.csv')

# Set index to 'ID'
df1.set_index('ID', inplace=True)
df2.set_index('ID', inplace=True)

# Inner Join
inner_join = pd.merge(df1 , df2 , on ='ID', how ='inner')
inner_join 

# Outer Join
outer_join = pd.merge(df1 , df2 , on='ID', how = 'outer')
outer_join

# Left Join
left_join = pd.merge(df1, df2, on='ID', how = 'left')
left_join

# Right Join
right_join = pd.merge(df1, df2, on='ID', how = 'right')
right_join
