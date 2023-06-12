import pandas as pd

df = pd.read_csv('datagov_n.csv', encoding='utf-8')
df2 = df.loc[df['n_model'] == 'Q7']



mask = ~df['n_model'].str.contains('missing')


df_mask = df[mask]
df_mask.to_csv("datagov_masked.csv")
b=5

