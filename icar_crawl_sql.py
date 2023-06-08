import sqlite3
import pickle
from urllib.parse import quote
from urllib.request import urlopen
import icar_normalize
from bs4 import BeautifulSoup
import os
import requests
import logging

tag = 'label', {'class': 'form-check-label'}
url = 'https://www.icar.co.il/%D7%90%D7%95%D7%93%D7%99/%D7%90%D7%95%D7%93%D7%99_TT/%D7%90%D7%95%D7%93%D7%99_TT_%D7%97%D7%93%D7%A9/'
page = requests.get(url)
html = page.content
soup = BeautifulSoup(html, "html.parser")
result = soup.find_all(tag[0], tag[1])
b = 5

# function to get a BeautifulSoup object from a URL and tag
def get_soup(url, tag):
    try:
        print(len(tag))
        page = requests.get(url)
        html = page.content
        soup = BeautifulSoup(html, "html.parser")
        if len(tag) == 1:
            result = soup.find_all(tag)
            return result
        result = soup.find_all(tag[0], tag[1])
        return result
    except Exception as e:
        logging.error(f"Error in url: {url}")
        logging.error(f"Error details {e}")

# function to create a URL for a given model name
def create_url(model_name, icar_url="https://www.icar.co.il"):
    quoted_model_name = quote(model_name)
    if quoted_model_name[0] != '/':
        quoted_model_name = '/' + quoted_model_name
    page_url = icar_url + quoted_model_name
    return page_url

# function to get a dictionary of initial model names and URLs for a given make
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

def get_generations(model_url):
    tag = 'div', {'class': 'cmodel_img'}
    soup_find_generations = get_soup(model_url, tag)
    generation_partial = [quote(result.contents[1].attrs['href']) for result in soup_find_generations]
    generation_urls = [icar_url + partial for partial in generation_partial]
    return generation_urls

# function to get a list of URLs for a given generation URL
def get_versions(generation_url):
    tag = 'a'
    soup_find_versions = get_soup(generation_url, tag)
    versions = [result.attrs['href'] for result in soup_find_versions if result.text == 'למפרט']
    version_urls = [icar_url + quote(version) for version in versions]
    return version_urls

def connect_to_database():
    db_file = 'icar_db.sql'
    # Check if the database file exists
    if os.path.exists(db_file):
        # Delete the existing database file
        os.remove(db_file)
        print("Existing database file deleted.")

    # create a connection object to the database
    conn = sqlite3.connect(db_file)

    # create a cursor object
    cursor = conn.cursor()

    # create the table to store the data
    cursor.execute('''CREATE TABLE IF NOT EXISTS icar_data
                   (id INTEGER PRIMARY KEY, 
                    make TEXT,
                    general_model TEXT,
                    exact_model TEXT,
                    version_url TEXT)''')
    return cursor, conn

# get the data and store it in the database
makes = ["אודי"]
icar_url = 'https://www.icar.co.il'
cursor, conn = connect_to_database()
def main(makes):

    for make in makes:
        model_dict = get_initial_models(make)
        for model in model_dict:
            general_model = model
            exact_model = icar_normalize.audi_normalize(model)
            model_url = model_dict[model]
            for generation_url in get_generations(model_url):
                version_urls = get_versions(generation_url)
                for version_url in version_urls:
                    # insert the data into the database
                    cursor.execute('''INSERT INTO icar_data (make, general_model, exact_model, version_url)
                                   VALUES (?, ?, ?, ?)''', (make, general_model, exact_model, version_url))

    # commit the changes to the database and close the connection
    conn.commit()


    conn.close()

main(makes)
