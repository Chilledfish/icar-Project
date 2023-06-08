from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
from requests.structures import CaseInsensitiveDict
import json
import requests
from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()

headers = {
'POST':'/api/bespokeapi.asmx HTTP/1.1',
'Host':'www.regcheck.org.uk',
'Content-Type': 'application/soap+xml; charset=utf-8',
'Content-Length': 'length'
}


data = """ <?xml version=\"1.0\" encoding=\"utf-8\"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <CheckEuroNCap xmlns="http://Regcheck.org.uk/">
      <Make>Audi</Make>
      <Model>A3</Model>
      <username>Chilledfish</username>
    </CheckEuroNCap>
  </soap12:Body>
</soap12:Envelope> """



url = "https://www.regcheck.org.uk/api/bespokeapi.asmx?op=CheckEuroNCap"


resp = requests.post(url, headers=headers, data=data)
response = requests.request("POST", url, headers=headers,data=data)


ncap_url = 'https://www.euroncap.com/en/ratings-rewards/latest-safety-ratings/'
ncap_html = urlopen(ncap_url).read().decode('utf-8')

ncap_models = ncap_html.find(" this.models = function () { return JSON.parse('[")
#jason = json.loads(ncap_url)


ncap_models = []
ncap_makes = []
ncap_demakes = []
ncap_urls = []
with open('ncap_models.txt', 'r', encoding='utf-8') as file:
    ncap_models_header = file.readline().strip('\n')
    for line in file:
        line = line.strip('\n')
        split = line.split(',')
        ncap_models.append(split)

        


make_id = []
with open('ncap_makes.txt', 'r', encoding='utf-8') as file:
    ncap_makes_header = file.readline().strip('\n')
    for line in file:
        line = line.strip('\n')
        split = line.split(',')
        ncap_makes.append(split)


with open('ncap_demakes.txt', 'r', encoding='utf-8') as file:
    ncap_demakes_header = file.readline().strip('\n')
    for line in file:
        line = line.strip('\n')
        split = line.split(',')
        ncap_demakes.append(split)


with open('ncap_urls.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip('\n')
        ncap_urls.append(line)



ncap_makes_n_models = []
ncap_makes_n_models_header = ['make','model','id']

a = ncap_models[0][0]

#ncap_models_dict = dict()
#for i in ncap_models[0]:
#    ncap_models_dict.append(i[0]:i[1])





ncap_url = 'https://www.euroncap.com'
urls = []
for model in ncap_models:
    for make in ncap_makes:
        if make[0] == model[2]:
            ncap = [make[1],model[1],model[0]]
            #urls.append(url + make[1] + '/' + model[1] + '/' + model[0])
            ncap_makes_n_models.append(ncap)
            continue

for line in ncap_urls:
    url = ncap_url + line
    urls.append(url)




'''
ncap_get = requests.get(ncap_url)

soup = BeautifulSoup(ncap_html)
soup_get = BeautifulSoup(ncap_get.text, 'lxml')
pretty = soup.prettify()
pretty2 = soup_get.prettify()
title = soup_get.title
a = soup_get.find_all('a')
'''



b=5