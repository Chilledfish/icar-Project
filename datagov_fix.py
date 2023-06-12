import pandas as pd


df = pd.read_csv('datagov_for_merge.csv', encoding='utf-8')

hanaa = df['hanaa_nm']
hanaa = hanaa.apply(lambda x: '2X4' if x == '4X2' else x)


df['hanaa_nm'] = hanaa

df.to_csv('datagov_for_merge.csv', encoding='utf-8', index=False)

b=5