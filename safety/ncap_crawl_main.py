from urllib.request import urlopen
from urllib import request,response
from bs4 import BeautifulSoup
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
import webdriver_manager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

'''# create webdriver object
driver = webdriver.Firefox()

# enter keyword to search
keyword = "geeksforgeeks"

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element_by_xpath("//form[input/@name ='search']")'''

b=5

url = "https://www.euroncap.com/en/ratings-rewards/latest-safety-ratings/#?selectedMake=0&selectedMakeName=Select%20a%20make&selectedModel=0&selectedStar=&includeFullSafetyPackage=true&includeStandardSafetyPackage=true&selectedModelName=All&selectedProtocols=45155,41776,40302,34803,30636,26061,24370,-1&selectedClasses=1202,1199,1201,1196,1205,1203,1198,1179,40250,1197,1204,1180,34736,44997&allClasses=true&allProtocols=true&allDriverAssistanceTechnologies=false&selectedDriverAssistanceTechnologies=&thirdRowFitment=false"
url = "https://www.euroncap.com/en/ratings-rewards/latest-safety-ratings/"
url = "https://www.euroncap.com/en/ratings-rewards/latest-safety-ratings/#?selectedMake=0&selectedMakeName=Select%20a%20make&selectedModel=0&selectedStar=&includeFullSafetyPackage=true&includeStandardSafetyPackage=true&selectedModelName=All&selectedProtocols=45155,41776,40302,34803,30636,26061,24370,-1&selectedClasses=1202,1199,1201,1196,1205,1203,1198,1179,40250,1197,1204,1180,34736,44997&allClasses=true&allProtocols=true&allDriverAssistanceTechnologies=false&selectedDriverAssistanceTechnologies=&thirdRowFitment=false"
browser = webdriver.Chrome(executable_path=r"G:\האחסון שלי\Car Project\chromedriver.exe")
#browser = webdriver.Firefox
browser.get(url)
# initiating the webdriver. Parameter includes the path of the webdriver.

# rating-table-row ng-scope
# "rating-table-row-cursor c9"
file = 'checkbox'
time.sleep(7)
a = browser.find_elements(By.CLASS_NAME, "make dropdown")


#content = browser.find_elements(By.CSS_SELECTOR, "p.filter-title")
#content = browser.find_elements(By.CSS_SELECTOR, "input.checkbox")
#content = browser.find_elements(By.XPATH, "//input[@type='checkbox']")
#content = cont
html = browser.page_source


# this renders the JS code and stores all of the information in static HTML code.

# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
all_divs = soup.findAll('div', {'class': 'ng-scope'})
#finder_outer = soup.findAll('div')
'''
findddd = soup.find('div', {'id': 'filters'})
findddd2 = findddd.attrs['id']
findddd3 = soup.find('p', {'class': 'filter-title'})
filter_find = soup.find_all('label')
checkbox_find = soup.find_all('span', {'class': 'checkbox'})
span_find = soup.findAll('span')
span1 = span_find[0]
span2 = span_find[1]
spans = [y for y in checkbox_find]
span = spans[0]'''
#browser.find_element(By.CLASS_NAME, "checkbox").click()
#soup = BeautifulSoup(html, "html.parser")

#checkbox_find2 = soup.find('div', {'id': 'filter-form'})
#boo = soup.find_all('form')
find_span = soup.findAll('div', {'class': 'rating-table-row ng-scope'})
find_car_class = soup.find_all('div', {'class': 'rating-table-row-cursor c9'})
all_cars = [x.find('a') for x in find_span]
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


