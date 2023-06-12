import re
import requests
import pandas as pd
from collections import deque
import unidecode
from dataframe_to_dictionary import model_converter, normalize_datagov_models
from ncap import NCAP_compiler
from urllib.parse import quote, unquote

makes = ["Aiways", "Alfa-Romeo", "Audi", "BMW", "Bentley", "Chevrolet", "Citroen", "Dacia", "DS", "DS", "Fiat",
         "Ford", "Honda", "Hyundai", "Isuzu", "Jaguar", "Jeep", "Kia", "Lancia", "Land-Rover",
         "Land-Rover", "Lexus", "Lynk & Co", "Maserati", "Mazda", "Mercedes", "MG", "Mitsubishi",
         "Nissan", "Opel", "Peugeot", "Porsche", "Renault", "Saab", "Seat",
         "Skoda", "Smart", "Ssangyong", "Subaru", "Suzuki", "Tesla", "Toyota", "Volkswagen",
         "Volvo"]

data_makes = ["איוויס", "אלפא רומיאו", "אאודי", "ב מ וו", "בנטלי", "שברולט", "סיטרואן", "דאציה", "די.אס", "די אס", "פיאט", "פורד",
              "הונדה", "יונדאי", "איסוזו", "יגואר", "ג'יפ", "קיה", "לנצ'יה", "לנדרובר", "רובר", "לקסוס", "לינק אנד קו",
              "מזראטי", "מזדה", "מרצדס", "מ.ג", "מיצובישי", "ניסאן", "אופל", "פיג'ו", "פורשה", "רנו", "סאאב", "סיאט",
              "סקודה", "סמארט", "סאנגיונג", "סובארו", "סוזוקי", "טסלה", "טויוטה", "פולקסווגן", "וולבו"]

data_makes_dict = dict(zip(data_makes, makes))

ncap_df = pd.read_csv('ncap_df.csv', encoding='utf-8')

data_df = pd.read_csv('datagov_df.csv', encoding='windows-1255')


data_makes = data_df['tozar']
ncap_makes = ncap_df['Make']

data_models = data_df['kinuy_mishari']
ncap_models = ncap_df['Model']


# remove dashes and question marks from models
new_ncap_models = ncap_models.apply(lambda x: x.replace('-', ' ').replace('?', ''))
ncap_df['Model'] = new_ncap_models
ncap_df = ncap_df.drop(columns='Unnamed: 0')
new_data_models = data_models.apply(lambda x: x.replace('-', ' ').replace('?', ''))
data_df['kinuy_mishari'] = new_data_models

# Translate makes to Hebrew
'''new_data_makes = data_makes.apply(lambda car_model: data_makes_dict.get(car_model))
data_makes_list = new_data_makes.to_list()
data_makes_set = set(data_makes_list)
data_df['tozar'] = new_data_makes
df = data_df.loc[data_df['tozar'] == 'None']
data_df = data_df.drop(columns='Unnamed: 0')'''



b=5
test_urls = [
	"/en/results/toyota/urban-cruiser/11068",
	"/en/results/land-rover/range-rover-evoque/35028",
	"/en/results/peugeot/3008/5008/26581",
	"/en/results/bmw/x1-/-x2/30140",
	"/en/results/bmw/2-series-gran-coup%C3%A9/41291",
	"/en/results/alfa-romeo/giulietta/29288",
	"/en/results/mercedes-benz/eqb/44202",
	"/en/results/bmw/x1-/-x2/30140",
	"/en/results/mercedes-benz/citan-kombi/10838",
	"/en/results/bmw/2-series-gran-coup%C3%A9/41291",
	"/en/results/land-rover/defender/41395",
	"/en/results/opel/vauxhall/combo/33737",
	"/en/results/bmw/2-series-gran-coup%C3%A9/41291",
	"/en/results/mercedes-benz/g-class/34835",
	"/en/results/land-rover/range-rover-evoque/35028"]

#data_df.to_csv('datagov_safety.csv', encoding='utf-8', index=False)
ncap_df.to_csv('ncap_safety.csv')
datagov_df = pd.read_csv('datagov_csv.csv', encoding='windows-1255', engine='python')
c = 0

with open('ncap_urls.txt', 'r', encoding='utf-8') as url_file:
	ncap_urls = [i.strip('\n') for i in url_file]


# -------------
ncap_url_list = []

make1 = makes[11]
original_make = make1
q_make = unquote(make1)
#make = makes_dict.get(original_make.lower())
b = 5
# ------------
url_makes = []
#current_make = [car_model for car_model in ncap_urls if make.lower() in car_model]



#url_makes = [makes_dict.get(car_model.lower()) for car_model in makes]




url_problems = []
for model_url in ncap_urls[31:]:
	#simplifed_url = simplify(unquote(model_url))
	simplifed_url = model_url
	URL_split = simplifed_url.split("/")[3]
	#make = makes_dict.get(URL_split.lower())
	#url_makes.append(make)
	#if make == None:
	#	url_problems.append(URL_split)


'''	if not make:
		continue
	model_dict, safety_pack = NCAP_compiler(simplifed_url, make)
	models = model_dict.get('models')
	year = int(model_dict.get('year'))

	rating = int(model_dict.get('rating'))
	safety = model_dict.get('safety_tests')
	crash = model_dict.get('crash_test').strip('\t')

	for i in range(len(models)):
		model = models[i]
		out_list = [make, models[i], year, rating, safety[0], safety[1], safety[2], safety[3], crash]

		try:
			reassessment_ind = ncap_df.index[
				(ncap_df["Make"] == make) & (ncap_df["Model"] == model) & (ncap_df["Year"] == year).tolist()]

			r = reassessment_ind[0]
		except:
			reassessment_ind = pd.Series(dtype=object)
			reject_df.loc[len(reject_df.index)] = out_list

		if reassessment_ind.dtype == 'int64' and reassessment_ind.size > 0:
			a = ncap_df.loc[r, "Video_Url"]
			if len(ncap_df.loc[r, "Video_Url"]) == 0:
				ncap_df.loc[r, "Video_Url"] = crash
			elif ncap_df.loc[r, 'Adult_Occupant'] < safety[0]:
				ncap_df.loc[r] = out_list
			else:
				reject_df.loc[len(reject_df.index)] = out_list

		else:
			ncap_df.loc[len(ncap_df.index)] = out_list
		f = 2
		cursor += 1'''
'''
url_problems = []
for i in range(len(url_makes)):
	if url_makes[i] == None:
		url_problems.append(i)

url_makes = set(url_makes)

b = 5
ncap_df.to_csv('ncap4.csv')
reject_df.to_csv('reject.csv')
moo = 2

'''
'''if len(reassement_ind) > 0:
	df.loc[reassement_ind[0]] = ncap_model
	continue
else:
	df.loc[len(df.index)] = ncap_model'''
'''
# all_models = model_df.loc[0].tolist()

# df_models = list(model_df.columns.values)
# df_models = [str(i).upper() for i in models]
# model = model_split if model_split in df_models else 0
reassessment_ind = []

with open('ncap_urls.txt', 'r', encoding='utf-8') as url_file:
	ncap_urls = [i.strip('\n') for i in url_file]

reassessment_ind = \
ncap_df.index[(ncap_df["make"] == make) & (ncap_df["model"] == model) & (ncap_df["year"] == year)].tolist()[0]

ncap_df.to_csv('ncap_dataframe.csv', encoding='utf-8', index=False)



reject_df = pd.DataFrame(
	columns=['Make', 'Model', 'Year', "Rating", 'Adult_Occupant', 'Child_Occupant', 'Vulnerable_Road_Users',
	         'Safety_Assist ',
	         'Video_Url'])'''