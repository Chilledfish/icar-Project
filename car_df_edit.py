import pandas as pd
import numpy as np

df = pd.read_csv('merged.csv', encoding='utf-8')

columns = ["tozeret_cd", "degem_cd", "year", "gova", "ignition", "gearbox", "gear", "piston", "loops", "moment", "loopmoment", "acceleration", "speed", "urban_consumption", "intercity_consumption", "consumption", "electricity_use", "battery_capacity", "electric_range", "home_charging_time", "fast_charging_time", "brake", "cenairbag", "length", "width", "height", "wheel", "cargo", "chaircargo", "selfweight", "totalweight", "loading", "fuel"]
new_columns = ["tozeret_cd", "degem_cd", "year", "ignition", "gearbox", "gear", "piston", "loops", "moment", "loopmoment", "acceleration", "speed", "urban_consumption", "intercity_consumption", "consumption", "electricity_use", "battery_capacity", "electric_range", "home_charging_time", "fast_charging_time", "brake", "cenairbag", "length", "width", "height", "wheel", "cargo", "chaircargo", "selfweight", "totalweight", "loading", "fuel"]


new_df = df[columns]


icar_height = new_df['height']
data_height = new_df['gova']

nans = new_df['gova'].isnull().values

new_gova = []
for i in range(icar_height.shape[0]):
	nan = nans[i]
	data_gova = data_height.iloc[i]
	icar_gova = icar_height.iloc[i]
	if nan == True:
		if icar_gova == 0:
			new_gova.append(np.nan)
		else:
			new_gova.append(icar_height.iloc[i])
	else:
		if data_gova == 0:
			new_gova.append(np.nan)
		else:
			new_gova.append(data_height.iloc[i])

new_df['height'] = new_gova

new_df2 = new_df[new_columns].drop_duplicates(["tozeret_cd", "degem_cd", "year"])
new_df2.to_csv('merged_final1.csv', encoding='utf-8', index=False)
b=5


