from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
import csv

#makes = ["DS", "GAC", "SERES", "אבארט", "אודי", "אופל", "איווייז", "איווקו", "אינפיניטי", "איסוזו", "אלפא_רומיאו", "אסטון מרטין", "ב.מ.וו", "ביואיק", "בנטלי", "ג'ילי", "גיפ", "ג'נסיס", "גרייט וול", "דאציה", "דודג", "דייהטסו", "האמר", "הונדה", "וולוו", "טויוטה", "טסלה", "יגואר", "יונדאי", "לינקולן", "לנדרובר", "לנציה", "לקסוס", "מאזדה", "מאן", "מזראטי", "מיני", "מיצובישי", "מקסוס", "מרצדס", "ניסאן", "סאאב", "סאיק-MG", "סאנגיונג", "סובארו", "סוזוקי", "סיאט", "סיטרואן", "סמארט", "סקודה", "סקייוול", "פולקסווגן", "פונטיאק", "פורד", "פורשה", "פיאט", "פיג'ו", "פרארי", "קדילאק", "קופרה", "קיה", "קרייזלר", "ראם", "רנו", "שברולט"]
base_url = "https://www.icar.co.il/"

make_page_url = "https://www.icar.co.il/%D7%99%D7%A6%D7%A8%D7%A0%D7%99_%D7%A8%D7%9B%D7%91/"
make_page = urlopen(make_page_url)
soup_get_urls = BeautifulSoup(make_page, 'lxml')
url_list = soup_get_urls.find_all("div", {"class": "manufacture_common"})
make_list_raw = [x.contents[1].attrs['href'] for x in url_list]
makes = [x.strip('/') for x in make_list_raw]
make_urls = [base_url + quote(x) for x in make_list_raw]
makes_dict = dict(zip(makes, make_urls))

csvfile = open('icar_models.csv', 'w', encoding='utf-8', newline='')
csvwriter = csv.writer(csvfile)

for make in makes:
	page = urlopen(makes_dict.get(make))
	soup = BeautifulSoup(page, 'lxml')
	model_find = soup.find("div", {"class": "row cars manufatures"})
	model_contents = model_find.contents
	make = make.replace('_', ' ')
	model_text = [model.text for model in model_contents if len(model) > 2]
	models_raw = [x.strip('\n') for x in model_text if x.find(make) > 0]
	models = [x[(len(make) + 1):] for x in models_raw]
	out_list = [make]
	out_list.extend(models)
	csvwriter.writerow(out_list)


b=5