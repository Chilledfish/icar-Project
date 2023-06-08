import sqlite3
import json
from sqlacodegen.codegen import CodeGenerator
from sqlalchemy import create_engine, MetaData
import sqlalchemy_utils
import pandas as pd
import pickle
import numpy as np
import re
import unittest


def trim_trim(trim):
	trimming = re.findall(r'\b[A-Za-z]+\b', trim)
	trimming = [x.upper() for x in trimming]
	if trimming:
		return ' '.join(trimming)
	return np.nan

class MyFunctionTestCase(unittest.TestCase):
    def test_scenario1(self):
        input = 'Sportback RFS 13 מווו'
        expected_output = ['SPORTBACK', 'RFS']  # Define the expected output
        result = trim_trim(input)
        self.assertEqual(result, expected_output)

    '''def test_scenario2(self):
        input = ...  # Define the input for this scenario
        expected_output = ...  # Define the expected output
        result = my_function(input)
        self.assertEqual(result, expected_output)'''

    # Add more test scenarios as needed


'''if __name__ == '__main__':
    unittest.main()'''



def trim_trim(trim):
	trimming = re.findall(r'\b[A-Za-z]+\b', trim)
	trimming = [x.upper() for x in trimming]
	if trimming:
		return ' '.join(trimming)
	return np.nan


with open('hebrew_fields.pkl', 'rb') as pickle_file:
	hebrew_fields = pickle.load(pickle_file)

with open('audi_datagov.pkl', 'rb') as car_file:
	df_datagov = pickle.load(car_file)

with open('hebrew_fields.pkl', 'rb') as pickle_file:
	hebrew_fields = pickle.load(pickle_file)


file_name = 'audi_datagov.db'

conn = sqlite3.connect(file_name)

c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = c.fetchall()

c.execute("SELECT * FROM data_gov")
data = c.fetchall()

data_columns = [desc[0] for desc in c.description]

df1 = pd.DataFrame(data, columns=data_columns)

file_name = 'audi_icar3.sql'




conn = sqlite3.connect(file_name)

c = conn.cursor()


c.execute("SELECT * FROM cars")
#cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
#tables = cursor.fetchall()



rows = c.fetchall()





'''a = rows[0][3]
if isinstance(a, bytes):
	a2 = 'yes'
else:
	a2 = 'no'''
icar_sql = [[pickle.loads(field) if isinstance(field, bytes) else field for field in car] for car in rows]
icar_dict = [x[2] for x in icar_sql]
icar_general_model = [x[0] for x in icar_sql]
icar_exact_model = [x[1] for x in icar_sql]

icar_names = list(icar_dict[0].keys())
icar_values = [list(car.values()) for car in icar_dict]







left_on_trim = ['shnat_yitzur', 'koah_sus', 'nefah_manoa', 'mispar_dlatot', 'hanaa_nm', 'automatic_ind', 'mispar_moshavim', 'delek_cd', 'kinuy_mishari', 'ramat_gimur']
right_on_trim = ['year', 'power', 'capacity', 'doors', 'hanaa_nm', 'automatic_ind', 'mispar_moshavim', 'delek_cd', 'general_model', 'trim']

left_on = ['shnat_yitzur', 'koah_sus', 'nefah_manoa', 'mispar_dlatot', 'hanaa_nm', 'automatic_ind', 'mispar_moshavim', 'delek_cd', 'kinuy_mishari']
right_on = ['year', 'power', 'capacity', 'doors', 'hanaa_nm', 'automatic_ind', 'mispar_moshavim', 'delek_cd', 'general_model']


#int_columns = right_on[:4] + right_on[5:]
#a = pd.to_numeric(df2['capacity'])
#a.astype(int)
#df2_types = [np.int64, np.int64, int, np.int64, np.int64, np.int64, np.int64]
#df2[int_columns] = df2[int_columns].applymap(lambda x: pd.to_numeric(x))
#df2 = df2.drop('trim', axis=1)
df2 = df2.drop('additional_safety_equipment', axis=1)
trim = df2['trim'].apply(trim_trim)
trim2 = df['trim']
trim2 = [trim_trim(trim) for trim in trim2]
df2['trim'] = trim

b = 5
#df2_type_dict = dict(zip(df2_int_columns, df2_types))
#df2.astype(df2_type_dict)
#[df2[column].astype(np.int64) for column in df2_int_columns]
# Perform initial merge of df1 and df3 based on left_on and right_on columns

#merge1 =



merged_df = pd.merge(df1, df2, left_on=left_on, right_on=right_on, how='left')


unique_df = merged_df.drop_duplicates(keep='last')

unique_df.dropna(inplace=True)
b=5
'''# Drop rows with NaN values in merge_columns from merged_df
merged_df.dropna(subset=merge_columns, inplace=True)

# Drop duplicate rows from merged_df based on left_index column, keep the first occurrence
merged_df.drop_duplicates(subset='left_index', keep='first', inplace=True)

# Reset index in merged_df
merged_df.reset_index(drop=True, inplace=True)

# Create a new column 'matching_index' in merged_df containing the index of the first matching row, if any
merged_df['matching_index'] = merged_df['left_index']

# Drop rows without a match (NaN values in right_index)
merged_df.dropna(subset=['right_index'], inplace=True)

# Reset index in merged_df
merged_df.reset_index(drop=True, inplace=True)

# Convert the 'matching_index' column to integer type
merged_df['matching_index'] = merged_df['matching_index'].astype(int)

# Concatenate the appropriate row from df2 to each remaining row in merged_df
merged_df = pd.concat([merged_df, df2.loc[merged_df['matching_index']]])

# Reset index in merged_df
merged_df.reset_index(drop=True, inplace=True)



# Perform initial merge of df1 and df3 based on left_on and right_on columns
merged_df1 = pd.merge(df1, df3, left_on=left_on, right_on=merge_columns, left_index=True, how='left')

# Drop rows with NaN values in merge_columns from merged_df1
merged_df1.dropna(subset=merge_columns, inplace=True)

# Drop duplicate rows from merged_df1 based on left_index column, keep the first occurrence
merged_df1.drop_duplicates(subset='index_col', keep='first', inplace=True)

# Reset index in merged_df1
merged_df1.reset_index(drop=True, inplace=True)

# Concatenate the appropriate row from df2 to each remaining row in merged_df1
merged_df1 = pd.concat([merged_df1, df2.loc[merged_df1['right_index']]])

# Reset index in merged_df1
merged_df1.reset_index(drop=True, inplace=True)



# Perform merge based on specified columns
merged_df = pd.merge(df1, df3, left_on=left_on, right_on=merge_columns, how='left')


# Drop duplicate rows from df2 based on specified columns, keep the first occurrence
merged_df = merged_df.drop_duplicates(subset=merge_columns, keep='first')

# Identify matching rows
matching_rows = merged_df.dropna(subset=merge_columns)

# Extract the matching indices from df2
matching_indices = matching_rows.index.tolist()

# Add a new column to df1 with matching indices from df2
df1['matching_index'] = matching_indices



merged_df3 = pd.merge(df1, df3, left_index=True, right_index=True, left_on=left_on, right_on=merge_columns, how='left')
merged_df3.set_index(merged_df3['column2'], inplace=True)

# Merge df1 with df3 to find the matching index numbers in df2
merged_df3 = pd.merge(df1, df3, left_on=left_on, right_on=merge_columns, how='left', suffixes=('', '_spec'))

# Get the matching index numbers from df3
index_numbers = merged_df3.index_spec.values

# Extract the matching rows from df2 using the index numbers
matching_df2 = df2.iloc[index_numbers]

# Concatenate the specs from matching_df2 to df1 based on their index values
merged = pd.concat([df1, matching_df2], axis=1)

# The resulting merged dataframe should now contain the specs from matching_df2
# concatenated to df1 for the cars with matching index numbers in df3.

# Save the resulting merged dataframe to a new CSV file if needed
merged.to_csv('merged_cars.csv', index=False)  # Replace with the desired filename







merged_keys = pd.merge(df1, df3, left_on=left_on, right_on=merge_columns, how='left')

index_numbers = merged_keys.index.tolist()

# Reset the index of df2
df2 = df2.reset_index(drop=True)

# Select rows from df2 using the extracted index numbers
selected_rows = df2.iloc[index_numbers]


# Concatenate df1 with selected rows from df2
merged = pd.concat([df1, selected_rows], axis=0, ignore_index=True)
merged.to_csv('merged.csv', index=False)



merged = pd.concat([df1, df2.iloc[index_numbers]], axis=0, ignore_index=True)
merged.to_csv('merged.csv', index=False)
# Drop the duplicate columns '_y' from the merge
merged = merged.filter(regex='^(?!.*_y)')

# Reset the index
merged.reset_index(drop=True, inplace=True)

merged.to_csv('merged.csv', index=False)

moo = [str(x).find('u') for x in data if str(x).find('u') > -1 and str(x).find('u') < 100]
engine = data[99]['סוג מנוע']

moo = data[1]
data_read = [json.loads(x) for x in data]
makes = rows2[0]



b=5'''