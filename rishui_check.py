import pandas as pd


merge_columns = ['tozeret_cd', 'degem_cd']
rishui_columns = ['tozeret_cd', 'degem_cd', 'size']
file_name = 'rishui_out'

df = pd.read_csv('rishui_out_all.csv', encoding='utf-8')
df2 = df.groupby(df.columns.tolist(), as_index=False).sum()
b = 5



'''c_df = pd.DataFrame(columns=rishui_columns)
for i in range(21):
	i = i+1
	df = pd.read_csv(f"{file_name}{i}.csv", encoding='utf-8')
	df2 = df.groupby(df.columns.tolist(), as_index=False).size()
	c_df = pd.concat([c_df, df2])
	b = 5

#c_df.to_csv('rishui_out_all.csv', encoding='utf-8', index=False)
d_df = c_df.groupby(c_df.columns.tolist(), as_index=False).sum()'''

b = 5
'''merge_df = pd.read_csv('merged_final1.csv', encoding='utf-8', usecols=merge_columns)

rishui_df = pd.read_csv('all_cars.csv', encoding='utf-8')

df_name = 'rishui_df'


df_list = [rishui_df.iloc[(i)*100000:(i+1)*100000] for i in range(15)]




#rishui_df = rishui_df.rename(columns={'size': 'amount'})

#rishui_df2 = rishui_df.groupby(risui_columns, as_index=False).size()
hit_df = pd.merge(merge_df, rishui_df, left_on=merge_columns, right_on=merge_columns, how='outer', indicator=True).query('_merge' != "both")
hit_df2 = hit_df.groupby(merge_columns, as_index=False).size()
b=5'''
