import pandas as pd

df = pd.read_excel('german_database.xlsx', sheet_name='cars', engine='openpyxl', index_col=None, names=None)

b = 5