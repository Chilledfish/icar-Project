import requests
from bs4 import BeautifulSoup
import re

url = "https://www.icar.co.il/%D7%99%D7%95%D7%A0%D7%93%D7%90%D7%99/%D7%99%D7%95%D7%A0%D7%93%D7%90%D7%99_%D7%91%D7%90%D7%99%D7%95%D7%9F/%D7%99%D7%95%D7%A0%D7%93%D7%90%D7%99_%D7%91%D7%90%D7%99%D7%95%D7%9F_%D7%97%D7%93%D7%A9/version24756/"
url = "https://www.icar.co.il/%D7%90%D7%95%D7%93%D7%99/%D7%90%D7%95%D7%93%D7%99_A1/%D7%90%D7%95%D7%93%D7%99_A1_%D7%97%D7%93%D7%A9/version19678/"
website = requests.get(url)
soup = BeautifulSoup(website.content, "html.parser")
soup_find = soup.find('title')
title = soup_find.text.replace('iCar', '')
reg = re.findall(r"\b\d*[A-Za-z]+\d*[A-Za-z]*\d*\b", title)
b=5
