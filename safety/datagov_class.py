import pandas as pd
from urllib.request import urlopen
from urllib import request, response
from bs4 import BeautifulSoup
import requests
import json


class Car:
	def __init__(self, make, model):
		self.make = make
		self.model = model

