import sqlite3
import pickle
from urllib.parse import quote
from urllib.request import urlopen
import icar_normalize
from bs4 import BeautifulSoup
import re

def audi_normalize(model):
	audi_model = model.upper()
	audi_list = ['TTS', 'TT', 'Q\d', 'A\d', 'S\d', 'R\d']
	audi_dict = {'Q4 E-TRON': 'Q4 E-TRON', 'Q8 E-TRON': 'Q8 E-TRON', 'GT': 'E-TRON GT', 'E': 'E-TRON', '^RS$': 'R8', 'RS6': 'S6'}
	sportback_list = ['SB', 'SP', 'ספורטבק']
	sportback = any(re.search(x, audi_model) for x in sportback_list)

	# Check for matches in audi_dict
	for x in audi_dict:
		if re.search(x, audi_model):
			audi_model = audi_dict[x]
			if audi_model == 'Q4 E-TRON':
				pass
			break
	# If no match was found in audi_dict, check for matches in audi_list
	else:
		for x in audi_list:
			audi_match = re.search(x, audi_model)
			if audi_match:
				audi_model = audi_match.group()
				break

	# If 'SPORTBACK' should be included, add it to the final model name
	if sportback:
		audi_model += ' SPORTBACK'

	return audi_model