import inspect
import json
import pickle
from collections import OrderedDict as odict
from urllib import request, response
from urllib.request import urlopen

import model_formatting as mf
import numpy as np
import pandas as pd
import requests
import safety_variables
from bs4 import BeautifulSoup

ncap_columns = ['model', 'rating', 'adult', 'passenger', 'pedestrians', 'safety equipment', 'car page',
                'crash test video']

pickle_file = open('datagov2022', 'rb')
datagov_df = pickle.load(pickle_file)

pickle_file = open('ncap_2022_models', 'rb')
ncap_df = pickle.load(pickle_file)

pickle_file = open('ncap2022', 'rb')
ncap_list = pickle.load(pickle_file)

# this adds crash test urls to ncap df
'''for i in range(len(safety_detail_list)):
    safety_detail_list[i].append(youtube_urls[i])

ncap_youtube_links_2022 = open('ncap_youtube_links_2022_2', 'ab')
pickle.dump(safety_detail_list, ncap_youtube_links_2022)
ncap_youtube_links_2022.close()'''

d_makes = ['קארמה', 'די.אס', 'סיטרואן', 'רנו', 'לינקולן', 'וואי', "ג'.מ", 'אאודי', 'סקודה', 'קרייזלר', 'אופל', 'ב מ וו',
           'טסלה', 'פורשה', 'פיאט', "פיג'ו", 'סקיוול', 'טויוטה', 'אלפא רומיאו', 'ניסאן', "דודג'", 'קאדילאק',
           'קיה', 'פולקסווגן', 'שברולט', "ג'יפ", 'מקסוס', 'סובארו', 'מ.ג', 'בי ווי די', 'אסטון מרטין', 'סרס',
           'אורה', 'אף אי דאבל יו', 'סיאט', "צ'רי", 'מיצובישי', 'לאמבורגיני', 'וולבו', 'יגואר', 'פולסטאר',
           'ליפמוטור', 'סוזוקי', 'לקסוס', 'גילי', 'אל אי וי סי', 'הונדה', 'פרארי', 'לינק אנד קו', 'רובר', 'פורד',
           'גי.אי.סי', 'מאן', 'סמארט', 'מרצדס', 'סאנגיונג', 'מזארטי', 'איסוזו', 'בנטלי', 'דאציה', 'לנדרובר', 'מזדה',
           'איווייס', 'יונדאי', 'די אס']

d_makes_translation = ['Karma', 'DS', 'Citroen', 'Renault', 'Lincoln', 'WEY', 'GM', "Audi", 'Skoda', 'Chrysler', 'Opel',
                       'BMW', 'Tesla', 'Porche', 'Fiat', 'Peugeot', 'Skywell', 'Toyota', 'Alfa_Romeo', 'Nissan',
                       'Dodge', 'Cadillac', 'Kia', 'VW', 'Chevrolet', 'Jeep', 'Maxus', 'Subaru', 'MG', 'BYD',
                       'Aston Martin', 'Seres', 'Ora', 'FEW', 'Seat', 'Cherry', 'Mitsubishi', 'Lamborghini', 'Volvo',
                       'Jaguar', 'Polestar', 'Leapmotor', 'Suzuki', 'Lexus', 'Geely', 'LEVC', 'Honda', 'Ferrari',
                       'Lynk & Co', 'Land Rover', 'Ford', 'GEC', 'MANN', 'Smart', 'Mercedes', 'SSangyong', 'Maserati',
                       'Isuzu', 'Bentley', 'Dacia', 'Land Rover', 'Mazda', 'Aiways', 'Hyundai', 'DS'
                       ]

data_makes = safety_variables.data_makes
data_makes_dict = safety_variables.ncap_data_dict
data_makes_reversed = dict([(value, key) for key, value in data_makes_dict.items()])

columns = ['tozeret_cd', 'degem_cd', 'tozar', 'kinuy_mishari', 'shnat_yitzur']

records = {
	'shnat_yitzur': 2022
}
parameters = {
	'limit': 100,
	# 'records': records
}

df = pd.DataFrame(columns=['tozeret_cd', 'degem_cd', 'tozar', 'kinuy_mishari', 'shnat_yitzur', 'degem_nm',
                           'nefah_manoa', 'delek_cd', 'delek_nm'])

url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=142afde2-6228-49f9-8a29-9b6c3a0cbe40'


# this get all cars from the datagov database into a dataframe and pickles it
'''datagov_url = f"{url}&limit=100000"
data_page = requests.get(datagov_url)
obj = data_page.json()
text = json.dumps(obj, sort_keys=True, indent=4, )
data_cars = obj['result']['records']
df = pd.DataFrame(data_cars,
                  columns=['tozeret_cd', 'degem_cd', 'tozar', 'kinuy_mishari', 'shnat_yitzur', 'degem_nm',
                           'nefah_manoa', 'delek_cd', 'delek_nm'])'''

pickle_file = open('datagov_all', 'ab')
datagov_df = pickle.dump(df, pickle_file)


def datagov_api_call(make, year=2022, limit=5000, model=''):
	make_eng = 'data_makes_reversed[make].lower()'
	make = f"&q={make}"
	year = f"&q={year}"
	if model != '':
		model = f"&q={model}"
	limit = f"&limit={limit}"
	url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=142afde2-6228-49f9-8a29-9b6c3a0cbe40'
	datagov_url = url + limit + make + model
	return requests.get(datagov_url), make_eng


make_args = []
# -----------------------------------------------------------------------------------------------
# This code extracts
'''datagov_url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=142afde2-6228-49f9-8a29-9b6c3a0cbe40&limit=50000&q=2022'
data_page = requests.get(datagov_url)
obj = data_page.json()
text = json.dumps(obj, sort_keys=True, indent=4, )
data_cars = obj['result']['records']
makes = [car_model['tozar'] for car_model in data_cars]
makes_set = set(makes)
df = pd.DataFrame(data_cars, columns=['tozeret_cd', 'degem_cd', 'tozar', 'kinuy_mishari', 'shnat_yitzur', 'degem_nm',
                                       'nefah_manoa', 'delek_cd', 'delek_nm'])'''

'''dbfile = open('pickle2', 'ab')
pickle.dump(df, dbfile)
dbfile.close()'''

#with open('pickle2', 'rb') as pickle_file:
#	df = pickle.load(pickle_file)

#df2 = pd.DataFrame(data_cars, columns=['tozeret_cd', 'degem_cd', 'tozar', 'kinuy_mishari', 'shnat_yitzur', 'degem_nm',
#                                       'nefah_manoa', 'delek_cd', 'delek_nm'])
b = 5


# -----------------------------------------------------------------------------------------------
class Cars:
	def __init__(self, make):
		self.make = make


data_makes = ['סנטרו']

for make in data_makes:
	'''df_last_row = df.tail(1)
	last_index = df_last_row.index[0]
	last = df_last_row.index
	indexes = df.index
	last_index2 = max(indexes)'''

	data_page, make_eng = datagov_api_call(make)
	obj = data_page.json()
	text = json.dumps(obj, sort_keys=True, indent=4, )
	data_cars = obj['result']['records']
	df2 = pd.DataFrame(data_cars,
	                   columns=['tozeret_cd', 'degem_cd', 'tozar', 'kinuy_mishari', 'shnat_yitzur', 'degem_nm',
	                            'nefah_manoa', 'delek_cd', 'delek_nm'])
	df = pd.concat([df, df2])

# This segment extracts the arguments for the method that is used.


# format_function = f"{make_eng}_format"


# format_function = f"{make_eng}_format"

# car = data_cars[0]
# models = [car_model['kinuy_mishari'] for car_model in data_cars]


df.reset_index(inplace=True)
df.rename(columns={'kinuy_mishari': 'model_name'}, inplace=True)
df['model_name'] = df['model_name'].apply(lambda x: x.lower())
df['corrected_model_name'] = df.apply(lambda x: standardize_model_name(args_string), axis=1)

# df = pd.DataFrame.from_records(data_car_list, columns=['tozeret_cd', 'degem_cd', 'tozar', 'kinuy_mishari', 'shnat_yitzur'])
df = df.sort_values(by='degem_nm')

try:
	standardize_model_name = getattr(mf, format_function)
except:
	print('no method available')
sig = inspect.signature(standardize_model_name)
args = list(sig.parameters.keys())
args_for_lambda = [f"car_model.{x}" for x in args]
args_string = ', '.join(args_for_lambda)

# This is a variable that imports the correct method for the manufacturer.


sig = inspect.signature(standardize_model_name)
args = list(sig.parameters.keys())
args_for_lambda = [f"car_model.{x}" for x in args]
args_string = ', '.join(args_for_lambda)

# , params=parameters


models = set(models)
data_car_list = []

data_car_list2 = []
makes = []

'''for car_model in data_cars:
    #data_car_list2.append([{'tozeret_cd': car_model['tozeret_cd']}, {'degem_cd': car_model['degem_cd']}, {'tozar': car_model['tozar']}, {'kinuy_mishari': car_model['kinuy_mishari']}, {'shnat_yitzur': car_model['shnat_yitzur']}])
    data_car_list.append([car_model['tozeret_cd'], car_model['degem_cd'], car_model['tozar'], car_model['kinuy_mishari'], car_model['shnat_yitzur']])'''

'''df_grouped = df.groupby(['degem_nm'])[['model_name', 'delek_cd']].first()

df_grouped = df.groupby(['kinuy_mishari', 'degem_nm'])
def standardize_name(group):
    return group['model_name'].str.split(' ').str[0]


moo = df_grouped.apply(standardize_name)
df['standardized_name'] = df_grouped.apply(standardize_name).transform('first')

df['delek_cd'] = df['delek_cd'].astype(np.int64)'''

data = data_cars.decode('utf-8')
data_split = data.split('id"')
b = 5

df - pd.DataFrame.from_dict()
'''# create webdriver object
driver = webdriver.Firefox()

# enter keyword to search
keyword = "geeksforgeeks"

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element_by_xpath("//form[input/@name ='search']")'''

b = 5
