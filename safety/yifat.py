import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from urllib.request import urlopen
from urllib import request,response
from bs4 import BeautifulSoup
import pandas as pd
import requests
#from webdriver_manager.chrome import ChromeDriverManager
import webdriver_manager
import requests
import json
from datetime import date



# משרד הביטחון

'''url = 'https://www.online.mod.gov.il/Online2016/pages/general/Balam/BalamList.aspx'

driver = webdriver.Chrome(executable_path=r"G:\האחסון שלי\Car Project\chromedriver.exe")
driver.get(url)
driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$ucBalamSearch$btnSearch").click()'''
b=5

today = date.today().strftime("%d/%m/%Y")

url = 'https://www.tenders.co.il/main'

driver = webdriver.Chrome(executable_path=r"G:\האחסון שלי\Car Project\chromedriver.exe")
driver.get(url)
html = driver.page_source
driver.find_element(By.CLASS_NAME, "src-app-components-___Topbar__login-link___GheLj").click()
driver.find_element(By.NAME, "userName").send_keys("410901")
driver.find_element(By.NAME, "password").send_keys("410901")
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[3]/div/div[2]/button").click()
driver.find_element(By.XPATH, '//div[@class="src-common-components-SearchInput-___SearchInput__clear_s___xCNID"]/a').click()
time.sleep(3)
results = driver.find_elements(By.CLASS_NAME, "src-common-components-ResultsItem-___ResultsItem__new_tab___hIzNx")
#results2 = driver.find_elements(By.XPATH, '//*[@id="root"]/section/div[2]/div[1]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/a')
moo = []
for x in results:
	moo.append(x.get_attribute('href'))
driver.get(url)
#driver.find_element(By.XPATH, '//div[class="react-datepicker__input-container"]')
#.send_keys(today)



b=5














url = 'https://www.tenders.co.il/main'

web_page = requests.get(url)