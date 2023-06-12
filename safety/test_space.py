from unidecode import unidecode
from urllib.parse import unquote
import webdriver_manager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.options import BaseOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from random_user_agent.user_agent import UserAgent
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process




#software_names = [SoftwareName.CHROME.value]
#operation_systems[OperatingSystem.WINDOWS.value]


'''user_agent_rotator = UserAgent(software_names=CHROME,
                               operation_systems=WINDOWS,
                               limit=100)'''
'''user_agent = UserAgent()

chrome_options = BaseOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument()'''



lst = ['Citroën C5 X', '82%', '87%', '69%', '66%', '4', 'https://www.euroncap.com/en/results/citro%c3%abn/c5+x/46599']
url = 'https://www.iec.co.il/content/suppliers/tenders-and-decisions/tenders/active-tenders'
url = "https://www.beer-sheva.muni.il/City/FreeInfo/Rehesh/pages/bids.aspx"

table_class = "tbl"
tender_class = 'form_group-container ng-star-inserted'
#options = webdriver.ChromeOptions()
#options.add_argument("start-maximized")
#driver = uc.Chrome(options=options)
#driver.get(url)
#tenders = driver.find_elements(By.CLASS_NAME, tender_class)

driver = webdriver.Chrome(executable_path=r"G:\האחסון שלי\Car Project\chromedriver.exe")
driver.get(url)

tender_body = driver.find_elements(By.XPATH, "//table")
tenders = driver.find_elements(By.XPATH, "//table/tbody/tr/td/div")
#tenders3 = driver.find_elements(By.XPATH, "/html/body/form/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/table/tbody/tr/td/div/*")
#tenders4 = driver.find_elements(By.CLASS_NAME, "midData")

tenders_text = [x.get_attribute('innerText') for x in tenders]
tenders_text = [x for x in tenders_text if len(x) > 100]
#tenders_text3 = [car_model.get_attribute('innerText') for car_model in tenders3]
#tenders_text4 = [car_model.get_attribute('innerText') for car_model in tenders4]
#text = tenders4[0].get_attribute('innerText')
#tenders2 = [car_model for car_model in tenders if len(car_model.text) > 100]
#tenders2[0].click()
b=5





name = lst[0]
name_decode = unidecode(name)

link = lst[-1]

split_link = link.split('/')
link_name = split_link[-3]
unquote_link = unquote(split_link[-3])
unquote_link_decoded = unidecode(unquote_link)
link_name_decode = link_name
b=5
