import pandas as pd

data_df = pd.read_csv('n_datagov_safety.csv', encoding='utf-8')
ncap_df = pd.read_csv('ncap_safety.csv', encoding='utf-8')

lefton = ['tozar', 'kinuy_mishari', 'shnat_yitzur']
righton = ['Make', 'Model', 'Year']

df = data_df.merge(ncap_df, left_on=lefton, right_on=righton)

df.to_csv('safety.csv', index=False, encoding='utf-8')

b=5