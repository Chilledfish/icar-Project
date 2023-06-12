import re
import requests
import pandas as pd
from collections import deque
import unidecode
from dataframe_to_dictionary import model_converter, normalize_datagov_models
from ncap import NCAP_compiler
from urllib.parse import quote, unquote


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

with open('ncap_urls.txt', 'r', encoding='utf-8') as url_file:
	ncap_urls = [i.strip('\n') for i in url_file]


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




url_problems = []
for model_url in ncap_urls:

	simplifed_url = model_url
	URL_split = simplifed_url.split("/")[3]
	make = makes_dict.get(URL_split.lower())
	url_makes.append(make)
	if make == None:
		url_problems.append(URL_split)


url_problems = []
for i in range(len(url_makes)):
	if url_makes[i] == None:
		url_problems.append(i)

url_makes = set(url_makes)



