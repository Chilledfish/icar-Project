from urllib.request import urlopen
import csv
import json
import pandas as pd
from pandas.core.frame import DataFrame


url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=142afde2-6228-49f9-8a29-9b6c3a0cbe40&limit=5&q=2016&q=159'

url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=142afde2-6228-49f9-8a29-9b6c3a0cbe40&limit=5&q=2016&q=159'



fileobj = urlopen(url)

fileobj = fileobj.read().decode('utf=8')

json_data = json.loads(fileobj)
a = json_data.keys()
c = json_data['result']['records']

d = json_data['help']


df1 = pd.json_normalize(json_data)
df = pd.DataFrame.from_dict(json_data, orient='index')

a = print(df)

#icar2 = df.to_csv('icar.csv')
'''
with open('2016.csv', 'w', encoding='utf-8',newline='') as csvwriter:
    writer = csv.writer(csvwriter,delimiter=',')
    writer.writerows(fileobj)
'''

json

b=5

