import pandas as pd


df = pd.read_excel('chasis.xlsx', sheet_name='chasis_audi', engine='openpyxl')

my_series = df['merkav'].squeeze()
#df2 = df['kinuy_mishari']


chasis_dict = dict()
merkav_list = ["סגור/משלוח"]
previous_model = '308 CDI'
j = 3
#df = df[592:].reset_index()

for i in range(df.shape[0]):

    model = df['kinuy_mishari'][i]
    merkav = df['merkav'][i]
    if model == previous_model:
        if merkav not in merkav_list:
            merkav_list.append(merkav)

    else:
        chasis_dict[previous_model] = merkav_list
        while len(merkav_list) < j:
            merkav_list.append('')

        merkav_list = []

    previous_model = model



df_out = pd.DataFrame.from_dict(chasis_dict)
df_out.to_csv('audi_chassis.csv', encoding='utf-8', index=False)
b=5

#chasis_dict[model] = df['merkav'][i]