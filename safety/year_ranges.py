import pandas as pd
from dataclasses import make_dataclass


df_excel = pd.read_excel('דגמים_בטיחות.xlsx', sheet_name='שנים', engine='openpyxl')
df_subset1 = df_excel[['make', 'model', 'year_range', 'אבזור']]

drop_index = []
for i in range(len(df_subset1)):
	j = df_subset1['אבזור'][i]
	if df_subset1['אבזור'][i] == 'Safety Pack':
		drop_index.append(i)


df_drop = df_subset1.drop(drop_index).reset_index()
df = df_drop.astype({'year_range': 'int32', 'model': 'str'})

df = df[['make','model','year_range']]
models = df['model']
df_models = df

new_df = pd.DataFrame(columns=['make', 'model', 'year_ranges'])

years = df['year_range']

groupy = df.groupby(['make', 'model'])
group_count = groupy.count()
groupy_groups = groupy.groups

for car in groupy_groups:
	make, model = car
	car_index = groupy_groups[car].values
	year = df['year_range'].values[car_index]
	year_list = list(year)
	new_df.loc[len(new_df)] = make, model, year_list


b=5