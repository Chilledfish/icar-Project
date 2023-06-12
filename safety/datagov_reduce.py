import pandas as pd
import numpy as np


normalized_datagov_df = pd.read_csv('datagov_normalized.csv', engine='python')

new_df = pd.DataFrame(columns={'dmake', 'dmodel', 'dyear', 'tozeret_cd', 'model_cd'})
n = 0
#normalized_datagov_df = normalized_datagov_df.astype({'dyear': 'int32'}, errors='ignore')
a = normalized_datagov_df.index.size
for i in range(normalized_datagov_df.index.size):
	none = normalized_datagov_df.loc[i,'none']
	if type(none) == float:
		new_df.loc[len(new_df.index)] = normalized_datagov_df.loc[i]

new_df.to_csv("datagov_final.csv")


b=5