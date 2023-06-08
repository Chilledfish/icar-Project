import re
import requests
import pandas as pd
from collections import deque
import unidecode
from dataframe_to_dictionary import model_converter, normalize_datagov_models
from ncap import NCAP_compiler
from urllib.parse import quote, unquote

start_year = 2008
final_year = 2021

NCAP_makes = ["AIWAYS", "ALFA-ROMEO", "AUDI", "BMW", "CHEVROLET", "CITROEN", "DACIA", "DS", "FIAT", "FORD", "HONDA",
              "HYUNDAI", "ISUZU", "JAGUAR", "JEEP", "KIA", "LANCIA", "LAND-ROVER", "LEXUS", "LYNK & CO", "MASERATI",
              "MAZDA", "MERCEDES", "MG", "MINI", "MITSUBISHI", "NISSAN", "OPEL", "PEUGEOT", "PORSCHE", "RENAULT",
              "SEAT", "SKODA", "SMART", "SSANGYONG", "SUBARU", "SUZUKI", "TESLA", "TOYOTA", "VOLKSWAGEN", "VOLVO"]

first_word_makes = ["Aiways", "Alfa", "Audi", "BMW", "Mini", "Chevrolet", "Citroen", "Citroën", "Dacia", "DS", "Fiat",
                    "Ford", "Honda", "Hyundai", "Genesis", "Isuzu", "Jaguar", "Jeep", "Kia", "Lancia", "Land",
                    "Lexus", "Lynk", "Maserati", "Mazda", "Mercedes", "Mercedes", "MG", "Mitsubishi",
                    "Nissan", "Infiniti", "Opel", "Opel/Vauxhall", "Peugeot", "Porsche", "Renault", "Seat", "Cupra",
                    "Skoda", "Škoda", "Smart", "Ssangyong", "Subaru", "Suzuki", "Tesla", "Toyota", "Volkswagen", "VW",
                    "Volvo"]

two_word_makes = {"Alfa": 1,
                  "Land": 20,
                  "Mercedes": 25,
                  "Lynk": 22
                  }

yazranim = ["איווייס", "אלפא רומיאו", "אאודי", "ב מ וו", "שברולט", "סיטרואן", "דאציה", "די אס", "פיאט", "פורד", "הונדה",
            "יונדאי",
            "איסוזו", "יגואר", "ג'יפ", "קיה", "לנצ'יה", "לנדרובר", "לקסוס", "לינק אנד קו", "מזארטי", "מזדה", "מרצדס",
            "מג",
            "מיצובישי", "ניסאן", "אופל", "פיג'ו", "פורשה", "רנו", "סיאט", "סקודה", "סמארט", "סאנגיונג", "סובארו",
            "סוזוקי", "טסלה", "טויוטה", "פולקסווגן", "וולוו"]

base_url = "https://www.euroncap.com/en/"

makes = ["Aiways", "Alfa-Romeo", "Audi", "BMW", "Chevrolet", "Citroen", "Dacia", "DS", "Fiat",
         "Ford", "Honda", "Hyundai", "Isuzu", "Jaguar", "Jeep", "Kia", "Lancia", "Land-Rover",
         "Lexus", "Lynk & Co", "Maserati", "Mazda", "Mercedes", "MG", "Mitsubishi",
         "Nissan", "Opel", "Peugeot", "Porsche", "Renault", "Saab", "Seat",
         "Skoda", "Smart", "Ssangyong", "Subaru", "Suzuki", "Tesla", "Toyota", "Volkswagen",
         "Volvo"]

data_makes = ["איוויס", "אלפא רומיאו", "אאודי", "ב מ וו", "שברולט", "סיטרואן", "דאצ'יה", "די.אס", "פיאט", "פורד",
              "הונדה", "יונדאי", "איסוזו", "יגואר", "ג'יפ", "קיה", "לנצ'יה", "לנדרובר", "לקסוס", "לינק אנד קו",
              "מזראטי", "מזדה", "מרצדס", "מ.ג", "מיצובישי", "ניסאן", "אופל", "פיג'ו", "פורשה", "רנו", "סיאט",
              "סקודה", "סמארט", "סאנגיונג", "סובראו", "סוזוקי", "טסלה", "טויוטה", "פולקסווגן", "וולוו"]

ncap_data_dict = dict(zip(makes, data_makes))

small_makes = [make.lower() for make in makes]

make_exceptions = {"opel/Vauxhall": "Opel",
                   "lynk-&amp;-co": "Lynk & Co",
                   "mini": "BMW",
                   "genesis": "Hyundai",
                   "cupra": "Seat",
                   "škoda": "Skoda",
                   "citroën": "Citroen",
                   "vw": "Volkswagen",
                   "mercedes-benz": "Mercedes",
                   "range-rover": "Land-Rover",
                   "infiniti": "Nissan",
                   "geely-emgrand": "Geely"
                   }

makes_dict = dict(zip(small_makes, makes))

makes_dict.update(make_exceptions)


def simplify(text):
	try:
		text = unidecode.unidecode(text, 'utf-8')
	except NameError:
		pass
	return str(text)


model_list = ["/en/results/citroën/spacetourer/22856",
              "/en/results/renault/megane/7890",
              "/en/results/bmw/x1-/-x2/30140",
              "/en/results/renault/megane/7889",
              "/en/results/peugeot/3008/5008/26581"]

ncap_df = pd.DataFrame(
	columns=['Make', 'Model', 'Year', "Rating", 'Adult_Occupant', 'Child_Occupant', 'Vulnerable_Road_Users',
	         'Safety_Assist ',
	         'Video_Url'])

small_df = pd.DataFrame(
	columns=['Make', 'Model', 'Year', "Rating", 'Adult_Occupant', 'Child_Occupant', 'Vulnerable_Road_Users',
	         'Safety_Assist ',
	         'Video_Url'])

reject_df = pd.DataFrame(
	columns=['Make', 'Model', 'Year', "Rating", 'Adult_Occupant', 'Child_Occupant', 'Vulnerable_Road_Users',
	         'Safety_Assist ',
	         'Video_Url'])

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

datagov_df = pd.read_csv('datagov_csv.csv', encoding='windows-1255', engine='python')
c = 0

with open('ncap_urls.txt', 'r', encoding='utf-8') as url_file:
	ncap_urls = [i.strip('\n') for i in url_file]

# -------------
ncap_url_list = []

make1 = makes[11]
original_make = make1
q_make = unquote(make1)
make = makes_dict.get(original_make.lower())
b = 5
# ------------
url_makes = []
current_make = [x for x in ncap_urls if make.lower() in x]



#url_makes = [makes_dict.get(car_model.lower()) for car_model in makes]


make_list = []

url_problem_index = []
for model_url in ncap_urls:
	#simplifed_url = simplify(unquote(model_url))
	simplifed_url = model_url
	URL_split = simplifed_url.split("/")[3]
	make = makes_dict.get(URL_split.lower())
	url_makes.append(make)
	if make == None:
		url_problem_index.append(URL_split)
	continue

	if not make:
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
		c += 1

url_problem_index = []
for i in range(len(url_makes)):
	if url_makes[i] == None:
		url_problem_index.append(i)

problem_urls = [ncap_urls[i] for i in url_problem_index]

url_set = set(url_makes)

b = 5
ncap_df.to_csv('ncap4.csv')
reject_df.to_csv('reject.csv')
moo = 2

'''	
if len(reassement_ind) > 0:
	df.loc[reassement_ind[0]] = ncap_model
	continue
else:
	df.loc[len(df.index)] = ncap_model
'''
# all_models = model_df.loc[0].tolist()

# df_models = list(model_df.columns.values)
# df_models = [str(i).upper() for i in models]
# model = model_split if model_split in df_models else 0
reassessment_ind = []

with open('ncap_urls.txt', 'r', encoding='utf-8') as url_file:
	ncap_urls = [i.strip('\n') for i in url_file]

reassessment_ind = ''
ncap_df.index[(ncap_df["make"] == make) & (ncap_df["model"] == model) & (ncap_df["year"] == year)].tolist()[0]

ncap_df.to_csv('ncap_dataframe.csv', encoding='utf-8', index=False)

b = 5

'''	get_title = soup.find('title').text
	title_list = get_title.split(' ')`
	year_check = re.search('20\d\d', title_list[-1])
	while re.search('20\d\d', title_list[-1]) == None:
		title_list.pop()
	year = title_list.pop()
	if title_list[-1] == '(reassessment)':
		check = title_list.pop()
	for item in title_list:
		if item in makes:
			make = item
		elif item in make_exceptions:
			make = make_exceptions.get(item)
	ind = title_list.index(make)
	title_deque = title_list[ind+1]

	make = title_deque.popleft() if title_deque[0] in makes|make_exceptions else title_deque.remove(make)
	make0 = title_deque.popleft()

	make = title_deque.popleft() if title_deque[0] in makes|make_exceptions else title_deque.popleft()
	mod = 1
	ncap_model2 = []
	url = base_url + model_url
	ncap_website = requests.get(url).text'''

'''for i in range(len(makes)):
	for j in range(len(makes[i])):
		make_dict[makes[i][j]] = yazranim[i]
		makes2.append(makes[i][j])'''

make = 'Opel'
models = ['Mokka', 'Fiat']
# makes_upper = [i.upper() for i in makes]
'''with open('ncap_urls.txt', 'r', encoding='utf-8') as url_file:
	ncap_urls = [i.strip('\n') for i in url_file]


	model_df = pd.read_excel('ncap_models.xlsx', sheet_name=make, engine='openpyxl')
	# model_df = excel_models[make].upper()

	df_models = list(model_df.columns.values)
	df_models = [str(i).upper() for i in models]
	model = model_split if model_split in df_models else 0

	soupfind = soup.findAll('img')

	for img in soupfind:
		if 'data' in img.attrs:
			crash = img.attrs['data']

	# website = ncap_website.read()
	b = 5

headers = CaseInsensitiveDict()'''

headers = {
	'POST': '/api/bespokeapi.asmx HTTP/1.1',
	'Host': 'www.regcheck.org.uk',
	'Content-Type': 'application/soap+xml; charset=utf-8',
	'Content-Length': 'length'
}

b = 5

'''make_test = title_split.popleft()
make = title_split.popleft()
if make not in makes:
	try:
		make = make_dict.get(make)
	except: b=5
	else: b = 5



if make_test in makes:
	ind = makes.index(make_test)
	make = makes[ind]
else:
	make_test = title_split.popleft()
	ind = makes.index(make_test)
	make = makes[ind]





	b=5


make = [i for i in makes if i.upper() in title.upper()]
make = make[0]
make = make_dict.get(make) if make in make_dict else make'''
