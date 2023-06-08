import re
from collections import deque


import pandas as pd

with open('ncap_urls.txt', 'r', encoding='utf-8') as reader:
	url_right = [line.strip('\n') for line in reader]


url_left = "https://www.euroncap.com"






'''def moo(url_right):
	split = url_right.split('/')
	make_and_models = split[3:-1]
	make_and_models_deque = deque(make_and_models)
	make = make_and_models_deque.popleft()
	model = make_and_models_deque.pop()
	opel = make_and_models_deque.pop() if make_and_models_deque != "vauxhall" else None
	model2 = make_and_models_deque.pop() if len(make_and_models_deque) > 0 else None
	return make, model, model2'''
'''for i in range(len(url_right)):

	a = re.search('(?<=/-)\w+', url_right[i])
	b = re.search('\w+(?=-/)', url_right[i])
	if a != None:
		b=5'''



def url_split(model_url):

	model2 = None
	car_list = deque(model_url.split('/')[3:-1])
	if "vauxhall" in car_list:
		car_list.remove("vauxhall")
	make = car_list.popleft()
	car_deque = deque(car_list)
	for i in range(len(car_deque)):
		if "'" in car_deque[i]:
			car_deque[i].remove("'")
	model = car_list.pop()
	model = re.search('(?<=-)\w+',model).group() if re.search('(?<=-)\w+',model) != None else model
	if len(car_list) == 1:
		extra_model = car_list.pop()
		model2 = re.search('\w+(?=-)',model2).group() if re.search('\w+(?=-)',model2) != None else model2
	return make, model, model2


#url = "/en/results/bmw/x3-/-x4/33285"
#url = "/en/results/mitsubishi/eclipse-cross/28678"
#make, model, model2 = url_split(url)












b=5