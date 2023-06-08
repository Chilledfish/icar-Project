from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup as bs



icar_url = "https://www.icar.co.il/"
decoded_text = quote("יצרני_רכב/")
makes_page_url = f"{icar_url}{decoded_text}"
makes_page = urlopen(makes_page_url)
soup = bs(makes_page, 'lxml')
h2 = soup.find_all('h2')
makes = [x.contents[0].get_text() for x in h2][:-2]
quoted_makes = [quote(make) for make in makes]
make_urls = [(icar_url + make) for make in quoted_makes]
quotemakes_dict = dict(zip(makes, make_urls))
get_urls_url = "https://www.icar.co.il/%D7%99%D7%A6%D7%A8%D7%A0%D7%99_%D7%A8%D7%9B%D7%91/"
get_urls_page = urlopen(get_urls_url)
soup_get_urls = bs(get_urls_page, 'lxml')
urls_list = soup_get_urls.find_all("div", {"class": "manufacture_common"})
make_list_raw = [x.contents[1].attrs['href'] for x in urls_list]
make_urls = [icar_url + quote(x) for x in make_list_raw]
makes_dict = dict(zip(makes, make_urls))
makes_dict = {"DS": "DS",
                  "די אס": "DS",
                  "די.אס": "DS",
                  "SERES": "סרס",
                  "אבארט": "פיאט",
                  "אודי": "אאודי",
                  "אופל": "אופל",
                  "איווייז": "אייוייז",
                  "איווקו": "איווקו",
                  "אינפיניטי": "ניסאן",
                  "איסוזו": "איסוזו",
                  "אלפא רומיאו": "אלפא רומיאו",
                  "אסטון מרטין": "אסטון מרטין",
                  "ב.מ.וו": "ב.מ.וו",
                  "ב מ וו": "ב.מ.וו",
                  "במוו": "ב.מ.וו",
                  "ביואיק": "ביואיק",
                  "בנטלי": "בנטלי",
                  "ג'ילי": "ג'ילי",
                  "גיפ": "ג'יפ",
                  "ג'נסיס": "יונדאי",
                  "גרייטוול": "גרייטוול",
                  "דאציה": "דאצ'יה",
                  "'דודג": "דודג",
                  "דייהטסו": "דייהטסו",
                  "האמר": "האמר",
                  "הונדה": "הונדה",
                  "וולוו": "וולוו",
                  "טויוטה": "טויוטה",
                  "טסלה": "טסלה",
                  "יגואר": "יגואר",
                  "יונדאי": "יונדאי",
                  "לינקולן": "פורד",
                  "לנדרובר": "לנדרובר",
                  "לנציה": "לנצ'יה",
                  "לקסוס": "טויוטה",
                  "מזדה": "מאזדה",
                  "מאזדה": "מאזדה",
                  "מאן": "מאן",
                  "מ א ן": "מאן",
                  "מזראטי": "מזראטי",
                  "מיני": "ב.מ.וו",
                  "מיצובישי": "מיצובישי",
                  "מקסוס": "מקסוס",
                  "מרצדס": "מרצדס",
                  "ניסאן": "ניסאן",
                  "ניסאן2": "ניסאן",
                  "סאאב": "סאאב",
                  "סאיק-MG": "סאיק-MG",
                  "סאנגיונג": "סאנגיונג",
                  "סובארו": "סובארו",
                  "סוזוקי": "סוזוקי",
                  "סיאט": "סיאט",
                  "סיטרואן": "סיטרואן",
                  "סמארט": "סמארט",
                  "סקודה": "סקודה",
                  "סקייוול": "סקייוול",
                  "פולקסווגן": "פולקסווגן",
                  "פונטיאק": "פונטיאק",
                  "פורד": "פורד",
                  "פורשה": "פורשה",
                  "פיאט": "פיאט",
                  "פיג'ו": "פיג'ו",
                  "פרארי": "פרארי",
                  "קדילאק": "קדילאק",
                  "קופרה": "סיאט",
                  "קיה": "קיה",
                  "קרייזלר": "קרייזלר",
                  "ראם": "דודג'",
                  "רובר": "לנדרובר",
                  "רנו": "רנו",
                  "שברולט": "שברולט"}

b=5

def get_models(make):
	make_url = quotemakes_dict.get(make)
	#make_url = 'https://www.icar.co.il/%D7%91.%D7%9E.%D7%95%D7%95/'
	make_page = urlopen(make_url)
	make_soup = bs(make_page, 'lxml')
	model_list_raw = make_soup.find('div', {'class': "row cars manufatures"})
	model_list_text = model_list_raw.text
	model_split = model_list_text.split('\n')
	models = [x for x in model_split if len(x) > 1]
	model_names = [x.replace("אודי ", "") for x in models]
	model_partial_urls = [x.contents[1].attrs['href'] for x in model_list_raw if len(x) > 2 if 'href' in x.contents[1].attrs]
	model_urls = [icar_url + quote(x) for x in model_partial_urls]
	return model_urls

def get_sub_models(model_url):
	model_page = urlopen(model_url)
	model_soup = bs(model_page, "lxml")
	submodel_find = model_soup.find("div", {"class": "carmodel_wrap"}).contents
	submodel_list_raw = [x.contents[3].table_contents[0] for x in submodel_find if len(x) > 2][:-1]
	submodel_list = [x.attrs['href'] for x in submodel_list_raw]
	submodel_urls = [icar_url + quote(x) for x in submodel_list]
	return submodel_urls


def get_version_urls(submodel_url):
	version_page = urlopen(submodel_url)
	version_soup = bs(version_page, "lxml")
	version_find = version_soup.find_all("label", {"class": "form-check-label"})
	version_list = [x.contents[5].attrs["href"] for x in version_find]
	version_urls = [icar_url[:-1] + quote(x) for x in version_list]
	return version_urls



#makes = ['פורד','DS']
makes = ['בנטלי', 'ב.מ.וו']
for make in makes:
	make = makes_dict.get(make)
	models = get_models(make)
	model_dict = dict()
	model_dict.update({make: models})
	sub_models = []
	versions = []
	for model in models:
		sub_models.extend(get_sub_models(model))
	for sub_model in sub_models:
		versions.extend(get_version_urls(sub_model))
	#versions = versions[:-2]
	with open(f"{make}.txt", 'w') as writer:
		for line in versions:
			writer.write("%s\n" % line)

b=5
