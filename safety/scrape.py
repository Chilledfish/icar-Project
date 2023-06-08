from urllib.request import urlopen
from urllib import request, response
from bs4 import BeautifulSoup
import requests
from unidecode import unidecode
import pandas as pd
import webdriver_manager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
#from webdriver_manager.chrome import ChromeDriverManager
import json
import model_formatting
from unidecode import unidecode
import pickle
from urllib.parse import unquote



df = pd.DataFrame(columns=['make', 'model', 'rating', 'adult', 'passenger', 'pedestrians', 'safety equipment'])
url = "https://www.euroncap.com/en/ratings-rewards/latest-safety-ratings/"
browser = webdriver.Chrome(executable_path=r"G:\האחסון שלי\Car Project\chromedriver.exe")

#ncap_youtube_url = 'https://www.youtube.com/@EuroNCAP_forsafercars/videos'
#browser.get(ncap_youtube_url)

'''
youtube_search = browser.find_element(By.NAME, 'search_query')
path = browser.find_elements(By.ID, "video-title-url")
lines = browser.find_elements(By.ID, "content")
last = lines[-1]
#actions = ActionChains(browser)

#browser.execute_script("arguments[0].scrollIntoView();", last)
a = path[-1].get_attribute('href')
actions.move_to_element(last).perform()
youtube_search.send_keys('aygo')
youtube_search.click()'''




#browser = webdriver.Firefox()
browser.get(url)
# initiating the webdriver. Parameter includes the path of the webdriver.

# rating-table-row ng-scope
# "rating-table-row-cursor c9"
file = 'checkbox'

html = browser.page_source


# this renders the JS code and stores all of the information in static HTML code.

# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
all_divs = soup.findAll('div', {'class': 'ng-scope'})
#finder_outer = soup.findAll('div')

time.sleep(1)
#browser.find_element(By.CLASS_NAME, "checkbox").click()
soup = BeautifulSoup(html, "html.parser")


def get_safety_data():
    tables = browser.find_elements(By.ID, "rating-table1")
    current_year_table = tables[0]
    text = current_year_table.text.split('\n')
    ncap_element_list = current_year_table.find_elements(By.XPATH, './div[2]/div[@class="rating-table-row ng-scope"]')
    star_elements = ncap_element_list[0].find_element(By.XPATH, "./div[@class='rating-table-row-cursor c8']/div/span/img")
    tests = current_year_table.find_elements(By.CLASS_NAME, "rating-table-row ng-scope")
    safety_detail_list = []
    for x in ncap_element_list:
        text_split = x.text.split('\n')
        type, ratings = text_split[1], text_split[2]
        if type == 'Standard':
            link = x.find_element(By.XPATH, './div[@class="rating-table-row-cursor c9"]/a').get_attribute('href')
            link_split = link.split("/")
            make_and_model = link_split[5:-1]
            model = make_and_model.pop()
            make = " ".join(make_and_model)
            make = unquote(make).replace('+', ' ')
            model = unquote(model).replace('+', ' ')
            adult, passenger, pedestrian, equipment = ratings.split(' ')
            star_rating = x.find_element(By.XPATH, "./div[@class='rating-table-row-cursor c8']/div/span/img").accessible_name
            safety_detail_list.append([make, model, star_rating, adult, passenger, pedestrian, equipment, link])
    return safety_detail_list



def ncap_pickling():
    safety_detail_list = get_safety_data()
    new_ncap_file = open('ncap1', 'wb')
    pickle.dump(safety_detail_list, new_ncap_file)
    new_ncap_file.close()
    return safety_detail_list


safety_detail_list = get_safety_data()

pickle_file = open('ncap4', 'ab')
car_page_links = [x[-1] for x in safety_detail_list]
pickle.dump(safety_detail_list, pickle_file)
pickle_file.close()




def get_youtube_url(car_url):
    browser.get(car_url)
    try:
        youtube_element = browser.find_element(By.XPATH, '//*[@id="tab3"]/div/div[1]/div/div[1]/img')
    except:
        return 'no video'
    return youtube_element.get_attribute('data')

#youtube_urls = [get_youtube_url(car_model) for car_model in car_page_links]

pickle_file = open('ncap_youtube_links_2022', 'rb')
youtube_urls = pickle.load(pickle_file)

for i in range(len(safety_detail_list)):
    safety_detail_list[i].append(youtube_urls[i])

'''ncap_youtube_links_2022 = open('ncap_youtube_links_2022_2', 'ab')
pickle.dump(safety_detail_list, ncap_youtube_links_2022)
ncap_youtube_links_2022.close()'''


#checkbox_find2 = soup.find('div', {'id': 'filter-form'})
#boo = soup.find_all('form')
find_span = soup.find_all('div', {'class': 'rating-table-row ng-scope'})
find_car_class = soup.find_all('div', {'class': 'rating-table-row-cursor c9'})
all_cars = [x.find('a') for x in find_span]
b=5


base_xpath = "//div[@class='rating-table-row ng-scope']"





annual_tests = browser.find_elements(By.XPATH, "//div[@id='rating-2014']")
year0 = annual_tests[0].text[:4]
year1 = annual_tests[-1].text



# This locates all of the lists of cars that were tested, split by years
lists = browser.find_elements(By.XPATH, '//div[@class="rating-table-body"]')
list1 = lists[:8]
list2 = lists[8:-1]
list3 = lists[-1]

# This adds to each box that contains all the cars from each year, all of the cars within
all_cars = [x.find_elements(By.XPATH, './div[@class="rating-table-row ng-scope"]') for x in list1]


# This extracts the make, model, test results and final star rating, still split by the year that the tests were conducted - from 2016
links = []
make_and_model_list = []
stars = []
safety_equipment_list = []
i = 0
car_dict = {}
#a = all_cars[8]
#a1 = car_model.find_element(By.XPATH, './div[@class="rating-table-row-cursor c8"]/div[1]/span[@class="stars"]/img').get_attribute('alt') for car_model in year
for year in all_cars:
    star = [x.find_element(By.XPATH, './div[@class="rating-table-row-cursor c8"]/div[1]/span[@class="stars"]/img').get_attribute('alt') for x in year]
    stars.append(star)
    link = [x.find_element(By.XPATH, './div[@class="rating-table-row-cursor c9"]/a').get_attribute('href') for x in year]

    links.append(link)
    make_and_model = [x.text.split('\n') for x in year]
    make_and_model_list.append(make_and_model)
    standard = [x[1] for x in make_and_model]
    for i in range(len(standard)):
        if standard[i] == "Standard":
            car_dict["make"] = make_and_model[0]
            car_dict
    safety_equipment = [x.find_element(By.XPATH, './div[@class="rating-table-row-cursor c10"]/div/span').text for x in year]
    safety_equipment_list.append(safety_equipment)
    i += 1
    print(i)
names = []
for annual_list in make_and_model_list:
    for car in annual_list:
        car_split = car.split('\n')
        name = car_split[0]
        names.append()






b=5
videos = []

car_dict = {}


for i in range(len(links[0])):
    video = ""
    url = links[0][i]
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    find = soup.find('div', {'class': 'responsive-video video-inline youtube-player smartphone-visible'})
    safety = safety_equipment_list[0][i]
    if safety_equipment_list[0][i] != 'Standard':
        videos.append("")
        continue
    video = find.contents[1].attrs['data']

    videos.append(video)
    b=5



# pre 2009 _ This gathers the same information for cars pre 2009, where the results were structured differently

pre_2009_dict = {}

pre_2009 = browser.find_elements(By.XPATH, "//div[@id='rating-table2']/div[@class='rating-table-body']/div")
pre_2009_anchors = [x.find_element(By.XPATH, "./pre-assessment-row[1]/a") for x in pre_2009]
pre_2009_link = [x.get_attribute('href') for x in pre_2009_anchors]
pre_2009_details = [x.accessible_name for x in pre_2009_anchors]

#________________________________________________________________________________






a_elements = browser.find_elements(By.XPATH, f"{base_xpath}/div[1]/a")
model = car6.find_elements(By.XPATH, f"{base_xpath}/div[4]/span")
links = [x.get_attribute('href') for x in a_elements]
split = [x.split('/') for x in links]
make = [x[5] for x in split]
model = [x[-1] for x in split]
star_elements = browser.find_elements(By.XPATH, "//div[@class='rating-table-row-cursor c8']/div/span/img")
stars = [x.accessible_name for x in star_elements]

driver_elements = browser.find_elements(By.XPATH, f"{base_xpath}/div[4]/span")
child_elements = browser.find_elements(By.XPATH, f"{base_xpath}/div[5]/span")
pedestrian_elements = browser.find_elements(By.XPATH, f"{base_xpath}/div[6]/span")
safety_equipment_elements = browser.find_elements(By.XPATH, f"{base_xpath}/div[7]/span")

drivers = [x.text for x in driver_elements]
children = [x.text for x in child_elements]
pedestrians = [x.text for x in pedestrian_elements]
safety_equipment = [x.text for x in safety_equipment_elements]

cars = []
for i in range(len(links)):
    car = [make[i], model[i], ]

b=5
cards = browser.find_elements(By.XPATH, "//div[@class='rating-table-row-cursor c9']/a")
links = [x.get_attribute('href') for x in cards]
a = cards[0].find_elements(By.XPATH, "./a")
b = a[0].get_attribute('href')
b=5

if len(cards) > 0:
    card = cards
else:
    raise NoSuchElementException('No cards were found')

#/div[@id='rating-2014']/div[@id='rating-table1']
#/div[@class='rating-table-body']/div[@class='rating-table-row ng-scope']/div[@class='rating-table-row-cursor c9']
#"/div[1]/div[1]/div[1]"
#f = browser.find_elements(By.CLASS_NAME, "name ng-binding")
all_links = soup.findAll('a')
#finding_outing = finder_outer.find('a')
all_links = [x.attrs['href'] for x in all_cars]

#url = all_links[0].attrs
b=5

#rating_find = soup.



span_table = find_span[0]
span_find = span_table.find('a')
span_href = span_find[1]
span_href1 = span_href.attrs
span_href2 = span_href.attrs[0]
span_link = span_href.attrs
span_row = span_table.attrs
span_link = span_table.find_all('a')
#span_link_href1 = span_link.attrs
span_link_href = span_link[0].find_all()
span_link_href1 = span_link.attrs[0]
child = all_divs[4].children
child2 = [x for x in child]
children = [x for x in all_divs.children]
job_profiles = all_divs.find_all('a')

# printing top ten job profiles
count = 0
for job_profile in job_profiles:
    print(job_profile.text)
    count = count + 1
    if (count == 10):
        break
'''





ncap_page = urlopen(url)
read = ncap_page.read(200)

ncap_bs = BeautifulSoup(ncap_page, 'lxml')
b=5

headers = {'User-Agent': 'Mozilla/5.0'}
URLs = ['https://www.frayssinet-joaillier.fr/fr/p/montre-the-longines-legend-diver-l37744302-bdc2']
URLs = ['https://www.euroncap.com/en/ratings-rewards/latest-safety-ratings/#?selectedMake=0&selectedMakeName=Select%20a%20make&selectedModel=0&selectedStar=&includeFullSafetyPackage=true&includeStandardSafetyPackage=true&selectedModelName=All&selectedProtocols=45155,41776,40302,34803,30636,26061,24370,-1&selectedClasses=1202,1199,1201,1196,1205,1203,1198,1179,40250,1197,1204,1180,34736,44997&allClasses=true&allProtocols=true&allDriverAssistanceTechnologies=false&selectedDriverAssistanceTechnologies=&thirdRowFitment=false']

data = []
# , class_ = "rating-table-row ng-scope"

#name ng-binding
for url in URLs:

    results = requests.get(url)
    soup = BeautifulSoup(results.text, "lxml")
    a = soup.find('div', {'class': 'rating-table-row'})
'''
