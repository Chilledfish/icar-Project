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
from collections import deque
import pickle



with open('selenium_test2', 'rb') as file:
	a = pickle.load(file)


model = a[0][0]
gimur = a[0][1]

data_lists = [x[2:] for x in a]


data = data_lists[0]

def zigzag(seq):
    return seq[::2], seq[1::2]

def get_data(data_list):
	data_list = deque(data_list)
	title = data_list.popleft()
	data_list = list(data_list)
	zig = zigzag(data_list)

	return title, zig





moo = get_data(data)
b=5

'''data = list(enumerate(data_list))
	odd = []
	even = []
	for item in data:
		if item[0] % 2 == 0:
			even.append(item[1])
		else:
			odd.append(item[1])'''


'''
even = []
odd = []
for item in a:
	moo = item[0]
	if item[0]%2 == 0:
		even.append(item[1])
	else:
		odd.append(item[1])'''






url = 'https://www.icar.co.il/%D7%90%D7%95%D7%93%D7%99/%D7%90%D7%95%D7%93%D7%99_A1/%D7%90%D7%95%D7%93%D7%99_A1_%D7%97%D7%93%D7%A9/version19678/'
browser = webdriver.Chrome(executable_path=r"G:\האחסון שלי\Car Project\chromedriver.exe")
browser.get(url)

a = browser.find_elements(By.CLASS_NAME, "card")

#a = browser.find_elements(By., "card-body")
c = a[0].text
a = [x.text for x in a]
a = a[:-2]
a = [x.split("\n") for x in a]
with open('selenium_test2', 'wb+') as file:
	pickle.dump(a, file)

c1 = c.split("\n")
c2 = deque(c1)
model = c2.popleft()
gimur = c2.popleft()
c2.popleft()
#name, value = [car_model, y for car_model, y in c2]


b=5

