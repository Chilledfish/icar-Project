import sqlite3
import pickle
from urllib.parse import quote
from urllib.request import urlopen

import pandas as pd

import icar_normalize
from bs4 import BeautifulSoup
import requests
import os



def get_makes():
    make_page_name = "/יצרני_רכב/"
    quoted_make_page = quote(make_page_name)
    icar_url = "https://www.icar.co.il"
    makes_url = icar_url + quoted_make_page
    make_tag = 'div', {"class": "manufacture_common"}
    soup_makes = get_soup(makes_url, make_tag)
    makes = [x.text.strip('\n') for x in soup_makes]
    make_quotes = [quote(x) for x in makes]
    make_urls = [icar_url + '/' + x for x in make_quotes]
    return makes, make_urls


def create_url(model_name, icar_url="https://www.icar.co.il"):
    quoted_model_name = quote(model_name)
    if quoted_model_name[0] != '/':
        quoted_model_name = '/' + quoted_model_name
    page_url = icar_url + quoted_model_name
    return page_url


def get_soup(url, tag):
    request = requests.get(url)
    html = request.content
    soup = BeautifulSoup(html, "html.parser")
    result = soup.find_all(tag[0], tag[1])
    return result


def get_initial_models(make):
    make_len = len(make) + 1
    make_url = create_url(make)
    tag = 'div', {'class': 'row cars manufatures'}
    soup_model_find = get_soup(make_url, tag)
    models_from_soup = [y.text.strip('\n').replace(' ', '_') for x in soup_model_find for y in x if
                        len(y.text.strip('\n')) > 0]
    icar_models = list(set(models_from_soup))
    initial_models = [x.replace('_', ' ')[make_len:] for x in icar_models]
    model_urls = [f"{make_url}/{quote(x)}" for x in icar_models]
    model_dict = dict(zip(initial_models, model_urls))
    return model_dict


def get_urls(model_url):
    version_urls = []
    generation_urls = []
    base_url = 'https://www.icar.co.il'
    tag = 'div', {'class': 'cmodel_common'}
    soup_gen_find = get_soup(model_url, tag)
    generations_children = [x.findChildren() for x in soup_gen_find]
    '''for item in generations_children:
        generation = item[1].attrs['href']
        for generation in item[1].attrs['href']:
            generation_urls.append(generation)'''
    generation_names = [x[1].attrs['href'] for x in generations_children]
    gen_urls = [base_url + quote(x) for x in generation_names]
    for url in gen_urls:
        version_urls += get_versions(url)
    return version_urls


def get_versions(gen_url):
    icar_url = 'https://www.icar.co.il'
    tag = 'div', {'class': 'form-check'}
    soup_find_models = get_soup(gen_url, tag)
    children = [x.findChildren() for x in soup_find_models]
    version_names = [x[3].attrs['href'] for x in children]
    version_urls = [icar_url + quote(x) for x in version_names]
    return version_urls


makes = ["אודי"]
icar_url = 'https://www.icar.co.il'

# Connect to database
conn = sqlite3.connect('icar_data2.sql')
c = conn.cursor()
'''rows = cursor.fetchall()
# Check if the table is empty
cursor.execute("SELECT COUNT(*) FROM models")
count = cursor.fetchone()[0]
rows = cursor.fetchall()

if count > 0:
    # The table is not empty, so delete its contents
    cursor.execute("DELETE FROM models")'''


# Create tables


c.execute('''CREATE TABLE IF NOT EXISTS models
             (id INTEGER PRIMARY KEY,
              make TEXT,
              initial_model TEXT,
              normalized_model TEXT,
              url TEXT)''')


# Insert data into makes table


def get_data(model, model_dict):
    initial_model = model
    normalized_model = icar_normalize.audi_normalize(model)
    version_urls = get_urls(model_dict[model])
    car_data = [[initial_model, normalized_model, version_url] for version_url in version_urls]
    return car_data




def main(make):
    columns = ['initial_model', 'normalized_model', 'model_url']
    df = pd.DataFrame(columns=columns)
    model_dict = get_initial_models(make)
    for model in model_dict:
        initial_model = model
        normalized_model = icar_normalize.audi_normalize(model)
        version_urls = get_urls(model_dict[model])
        car_data = [[initial_model, normalized_model, version_url] for version_url in version_urls]
        df = df.append(pd.DataFrame(car_data, columns=columns), ignore_index=True)
        #df.loc[len(df)] = car_data
        #print(car_data)
    with open('audi_urls.pkl', 'wb') as spec_file:
        pickle.dump(df, spec_file)

    '''df_sorted = df.sort_values('normalized_model')
    df_sorted.reset_index(inplace=True)
    with open('audi_urls.pkl', 'wb') as spec_file:
        pickle.dump(df_sorted, spec_file)'''

main('אודי')