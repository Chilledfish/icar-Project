from urllib.request import urlopen
import csv
import json
import pandas as pd
from pandas.core.frame import DataFrame
from urllib.request import quote
from wltp import model
import pandas as pd
from urllib.parse import unquote
from collections import OrderedDict as odic
import re

import requests
from bs4 import BeautifulSoup
import re
import wltp
from wltp.experiment import Experiment

a = wltp._version
#b = experiment('octavia')
c = wltp.experiment

unq = unquote("https://www.mazda.co.il/%D7%93%D7%92%D7%9E%D7%99%D7%9D/21/mazda-2")
url = "https://www.mazda.co.il/%D7%93%D7%92%D7%9E%D7%99%D7%9D/21/mazda-2"

data = requests.get(unq)
html = BeautifulSoup(data.text,'lxml')
tags = {tag.name for tag in html.find_all()}
field_values_heb = html.find_all('tr',{'class': "tooltip"})
unquoted = unquote(html)
unquoted_text = unquoted.text
a = []
a2 = []
a3 = data.text
with open('mazda2.txt','w', encoding='utf-8') as file:
    file.write(a3)


#field_values = html.find_all()
field_value = html.find("span")
for field in field_values:
    text = field.text
    contents = field.table_contents
    att = field.attrs
    if len(att) > 1:
        id = att['id']
        a2.append(id)
        name = re.search('(?<=\\n).+(?=\\n)',text)
        a.append(name.group())

icar_dict = dict(zip(a2,a))


b=5