import pickle
import re
from unidecode import unidecode

def pickle_dump(file_name, var):
	with open(file_name, 'wb+') as file:
		pickle.dump(var, file)

def pickle_load(file_name):

	with open(file_name, 'rb') as file:
		var = pickle.load(file)
	return var

'''	pickle_file = open('ncap4', 'rb')
	ncap_list = pickle.load(pickle_file)
	pickle_file.close()'''


'''pickle_file = open('ncap4', 'rb')
ncap_list = pickle.load(pickle_file)
pickle_file.close()'''

with open('ncap4', 'rb') as pickle_file:
	ncap_list = pickle.load(pickle_file)

with open('eng_makes', 'rb') as pickle_file:
	eng_makes = pickle.load(pickle_file)

with open('heb_makes', 'rb') as pickle_file:
	heb_makes = pickle.load(pickle_file)

with open('makes_dict', 'rb') as pickle_file:
	makes_dict = pickle.load(pickle_file)

#makes_dict['פולקסווגן'] = 'Volkswagen'

make_changes = {
				'cupra': 'Seat',
                'vw': 'Volkswagen',
                'mercedes-benz': 'Mercedes',
				'opel/vauxhall ': 'Opel',
				'genesis': 'Hyundai',
				'mercedes-eq': 'Mercedes'
}



pickle_dump('eng_makes', eng_makes)

makes_lower = [x.lower() for x in eng_makes]

moo = pickle_load('ncap4')

cars = [unidecode(x[0]) for x in ncap_list]
cars_lower = [x.lower() for x in cars]

#cars_2022 = [car_model.split(' ') for car_model in cars]

#makes_2022 = [car_model.find() for car_model in cars if car_model in cars]
new_list = []



missing_makes = []

def car_check(car):
	make = None
	model = None
	car_lower = car.lower()

	make_changes_keys = list(make_changes.keys())
	dict_check = [index for (index, item) in enumerate(make_changes_keys) if car_lower.startswith(item)]
	make_check = [index for (index, item) in enumerate(makes_lower) if car_lower.startswith(item)]
	if dict_check:
		make_ind = dict_check[0]
		make = make_changes[make_changes_keys[make_ind]]
	elif make_check:
		make_ind = make_check[0]
		make = eng_makes[make_ind]
	model = car[len(car_lower) + 1:]
	return make, model

for car in cars:
	a2_4 = []
	car = car.lower()
	eng_makes = [x.lower() for x in eng_makes]
	a = car.split(' ')[0]
	a2 = [x.find(a) for x in eng_makes]
	a2_2 = [eng_makes[x] for x in range(len(eng_makes)) if a2[x] > -1]


for car in cars[30:]:
	new_list.append(car_check(car))



for car in cars:
	if car in make_changes:
		car = make_changes[car]
	counter = 0
	new = 0
	match = car
	for i in range(len(makes_lower)):
		lower_make = makes_lower[i]
		make = eng_makes[i]
		match = re.match(f"{makes_lower[i]} ", car)
		if match:
			new = 1
			counter += 1
			if lower_make in make_changes:
				make = make_changes[lower_make]
			continue
		elif re.match(f"{make_changes[car]} ", car):
			make = make_changes[lower_make]
			new_list.append(make)
		new_list.append(make)
	if new == 0:
		make = None
		missing_makes.append(car)
		pass
	new_list.append(make)


'''for car in cars:
	new = 0
	match = car
	for make in makes_lower:
		if car.find(make) > -1:
			match = make
			new = 1
	if new == 0:
		new_list.append(f"new make: {match}")
	else:
		new_list.append(match)'''


new_list = [[x for x in cars] for x in cars]





pickle_file = open('ncap2022', 'rb')
current_ncap_df2 = pickle.load(pickle_file)
pickle_file.close()

'''pickle_file = open('datagov2022', 'rb')
datagov_df = pickle.load(pickle_file)
pickle_file.close()'''

pickle_file = open('datagov_all', 'rb')
datagov_df = pickle.load(pickle_file)
pickle_file.close()

tozar = datagov_df['tozar'].tolist()
tozar_set = set(tozar)



b=5
b=5