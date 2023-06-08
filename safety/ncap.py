import requests
import pandas as pd
from bs4 import BeautifulSoup
from collections import deque
from dataframe_to_dictionary import model_converter, normalize_datagov_models
import unidecode
import re

'''Function extracts all relevant data from NCAP page'''
def simplify(text):
	try:
		text = unidecode.unidecode(text, 'utf-8')
	except NameError:
		pass
	return str(text)

def parser(url_part2, url_part1="https://www.euroncap.com"):

	"""
	The car's model is extracted from the URL, and Using Beautiful Soup, the year, overall star rating, safety ratings,
	and crash video url, are located by their tags.
	"""
	soup_dict = {}
	url = url_part1 + url_part2

	split_url = url_part2.split('/')
	models = split_url[4:-1]

	# Opens the webpage for the test, and parses with 'BeautifulSoup'
	ncap_website = requests.get(url).text
	soup = BeautifulSoup(ncap_website, 'lxml')

	"""
	Locates the 'title' element which contains the make and one or two models. Then split the string into
	 a list of words, and convert the list into a double sided list, in order to retrieve items from beginning to end
	 """


	# Locates the year element and extracts the year
	soup_year = soup.find('div', {"class": 'year'})
	year = soup_year.contents[0][:4]

	""" Takes the latter half of an NCAP URL, extracts the make, models, year, safety test results and crash test
	YouTube	 Video """

	soup_stars = str(soup.find('div', {'class': 'stars'}).contents[0])

	soup_pack = soup.find('title').text



	rating = re.search('(?<=stars)\d', soup_stars)
	if rating != None:
		rating = rating.group()
	soup_safety_query = soup.findAll('div', {"class": "value"})
	safety_results = [safety.text for safety in soup_safety_query]


	soup_video = soup.findAll('img')

	crash_list = [line.attrs['data'] for line in soup_video if 'data' in line.attrs]
	if len(crash_list) < 1:
		crash_test = ''
	else:
		crash_test = crash_list[0]



	return models, year, rating, safety_results, crash_test, soup_pack




b=5


''' Function verifies the model extracted from the "title" element of the NCAP page is in a form compatible with Datagov 
'''
def ncap_models(model, model_dict):
	model_dict_items = model_dict.items()
	model_keys = [x[0] for x in model_dict_items]
	model_values = [x[1] for x in model_dict_items]
	model = model.upper().replace(' ','-')
	if model == "VAUXHALL":
		return None
	if model[0] == '-':
		model = model[1:]
	elif model[-1] == '-':
		model = model[:-1]

	for key in model_keys:
		simplified_key = simplify(str(key)).upper().replace(' ','-')
		if model == simplified_key:
			return key

	for i in range(len(model_values)):
		for value in model_values[i]:
			simplified_value = simplify(str(value)).upper().replace(' ','-')
			if model == simplified_value:
				return model_keys[i]
	return model + '?'

def data_models(model,model_dict):
	model_dict_items = model_dict.items()
	model_keys = [x[0] for x in model_dict_items]
	model_values = [x[1] for x in model_dict_items]
	model = model.upper().replace(' ', '-')
	for key in model_keys:
		simplified_key = simplify(str(key)).upper().replace(' ', '-')
		if model == simplified_key:
			return key

	for i in range(len(model_values)):
		for value in model_values[i]:
			simplified_value = simplify(str(value)).upper().replace(' ', '-')
			if model == simplified_value:
				return model_keys[i]
	return model + '?'





# Function takes all information from NCAP webpage, and compiles it to a list
def NCAP_compiler(url_part2, make):
	safety_pack = 0
	model_df = pd.read_excel('ncap_models.xlsx', sheet_name=make, dtype='str', engine='openpyxl')

	model_dict = model_converter(make)

	model_dict_items = model_dict.items()
	model_keys = [str(x[0]) for x in model_dict_items]
	model_values = [str(x[1]) for x in model_dict_items]
	keys = list(model_dict)

	url_models, year, rating, safety_results, crash_test, title = parser(url_part2)
	model2 = title.upper()
	url_part1 = "https://www.euroncap.com"

	# We take the list, and go through them to extract the make and models

	models = []
	for model in url_models:
		model = ncap_models(model, model_dict)
		if model != None:
			models.append(model)

	'''	
	Alternate method for findin car model
	model2 = re.search("full safety package", title, re.IGNORECASE)
	
	'''
	safety_pack_search = re.search("full safety package", title, re.IGNORECASE)

	if type(safety_pack_search) == re.Match:
		print("yay!")
		safety_pack = 1


	ncap_dict = {
		"make": make,
		"models": models,
		"year": year,
		"rating": rating,
		"safety_tests": safety_results,
		"crash_test": crash_test
	}

	b = 5

	#reassement_ind = df.index[(df["make"] == make) & (df["model"] == model) & (df["year"] == year).tolist()]

	return ncap_dict, safety_pack



test_urls =	["/en/results/alfa-romeo/giulietta/29288",
	"/en/results/mercedes-benz/eqb/44202",
	"/en/results/bmw/x1-/-x2/30140",
	"/en/results/mercedes-benz/citan-kombi/10838",
	"https://www.euroncap.com/en/results/bmw/2-series-gran-coup%C3%A9/41291",
	"/en/results/land-rover/defender/41395",
	"/en/results/opel/vauxhall/combo/33737",
	"/en/results/mercedes-benz/g-class/34835",
	"/en/results/land-rover/range-rover-evoque/35028"]


#a = ncap_models(test_urls[2], "BMW")
#b = 5

""" We search the 'img' element, and then the 'data' attribute, which contains the url to the YouTube car crash test
	video """



