import pandas as pd
import numpy as np
df = pd.read_csv('icar.csv', encoding='utf-8')


make = df['make']

def add_jeep(x):
	if type(x) == float:
		x = "ג'יפ"
	return x


new_make = make.apply(add_jeep)

df['make'] = new_make

df.to_csv('icar_new.csv', encoding='utf-8', index=False)
a = []
for x in range(3528,4010):
	a.append(x)
a = df.loc[4009, 'make']

b=5

