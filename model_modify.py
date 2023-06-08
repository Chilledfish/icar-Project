import re

import pandas as pd
import pickle
from fuzzywuzzy import fuzz
from datagov_api_queries import create_make_df
import difflib


with open ('makes.pkl', 'rb') as pickle_file:
	makes = pickle.load(pickle_file)

makes = sorted(makes)

makes_dict = ["Audi", "Opel", "ORA", "Aiways"
]


es = list()

def assign_engine(x):
	if x < 4:
		return 'petrol'
	if x == 4:
		return 'electric'
	return 'hybrid'

def modify_audi2(car_model, car_engine):
	item = car_model
	engine = car_engine
	if engine < 4:
		match_audi = re.match("AUDI", item)
		if match_audi:
			item = item[5:]

		if re.search("(^RS5)|(^RS6)", item):
			return item[:3]
		match_sb = re.search("SB|SP", item)
		if match_sb:
			match_ind = re.search(" ", item).start() + 1
			item = item[:match_ind] + "SPORTBACK"

		if re.search("(^RSQ)", item):
			item = item[2:]
		if re.search("(^RS(?!\s))|(^SQ)", item):
			item = item[1:]
			b=5
		match_chasis = re.search("(SEDAN|CABRIOLET|COUPE|CABRIO)", item)
		if match_chasis:
			sedan_ind = match_chasis.start()
			item = item[:sedan_ind-1]
		match_num = re.search("\d\d", item)
		if match_num:
			item = item.replace(match_num.group(), "")
		if re.search("TT", item):
			item = "TT"
		match_L = re.search("L$", item)
		if match_L:
			item = item[:-1]
		eng = re.search('\s[A-Z]', item)
		if eng:
			item = item[:eng.start()]

		if "E" in item:
			es.append(item)
		if re.search("\s$", item):
			item = item[:-1]
		return item
		if item == "RS":
			return "Q7"
		if item[0] == "R":
			b=5
	else:
		if "GT" in item:
			return "E-TRON GT"



		sback = re.search("SBACK", item)

		if sback:
			sback_ind = (sback.start(), sback.end())
			item = item.replace(item[sback_ind[0]:sback_ind[1]], "SPORTBACK")
			b=5
		digits = re.search("\d\d", item)
		if digits:
			item = item.replace(digits.group(), "")
		if re.search("Q4", item):
			if re.search("SPORTBACK", item):
				return "Q4 E-TRON SPORTBACK"
			return "Q4 E-TRON"
		e = item.find("E")
		if e == 0:
			if re.search("SPORTBACK", item):
				return "E-TRON SPORTBACK"
			return "E-TRON"

		letter_search = re.search("\s[A-Z]", item)
		if letter_search:
			item = item[:letter_search.start()]
		if item.count(" ") > 1:
			return item[item.rfind(" "):]
		es.append(item)
		if re.search("\s$", item):
			item = item[:-1]
		return item


'''def audi_match(item, list):
	for x in list:
		model_match = re.search(x, item)
		if model_match:
			if re.search("SB|SP", item):
				return f"{model_match.group()} SPORTBACK"
			return model_match.group()'''


def modify_audi(car_model, car_engine):

	audi_list = ['TTS', 'TT', 'Q\d', 'A\d', 'S\d', 'R\d']
	audi_dict = {'GT': 'E-TRON GT', 'E': 'E-TRON', '^RS$': 'R8', 'RS6': 'S6'}
	item = car_model
	item = re.sub("AUDI ", "", item)
	if item == "e-tron ספורטבק":
		return "E-TRON SPORTBACK"
	for x in audi_dict:
		if re.search(x, item):
			audi_model = audi_dict[x]
			break
	for x in audi_list:
		audi_match = re.search(x, item)
		if audi_match:
			audi_model = audi_match.group()
			break
	if re.search("SB|SP", car_model):
		# Next line for adding word SPORTBACK where appropriate
		#return audi_model + " SPORTBACK"
		b=5
	return audi_model



with open('audi_models.pkl', 'rb') as pickle_file:
    audi_models = pickle.load(pickle_file)

audi_models = [x.replace("ספורטבק", "SPORTBACK") if re.search("ספורטבק", x) else x for x in audi_models]

def modify_mazda(car_model, car_engine):
	mazda = re.search("MAZDA", car_model)
	if mazda:
		return re.search("\d", car_model).group()
	if re.search("(CX)", car_model):
		num = re.search("\d+", car_model).group()
		return f"CX{num}"
	if re.search("(MX)", car_model):
		num = re.search("\d+", car_model).group()
		return f"MX{num}"
	if re.search("BT", car_model):
		return "BT50"
	return car_model

def modify_opel(car_model):
	if re.search("\sST", car_model):
		return car_model.replace(" ST"," סטיישן")
	if re.search("MOKKA", car_model):
		return "MOKKA"
	if re.search("BERLINA", car_model):
		return "ASTRA BERLINA"
	if re.search("ASTRA", car_model):
		if re.search("GTC", car_model):
			return car_model
		return "ASTRA"
	if re.search("CORSA", car_model):
		return "CORSA"
	if car_model.find("ZAFIRA") > -1:
		return "ZAFIRA"
	return car_model

make = "אאודי"

'''with open(make, 'rb') as pickle_file:
    df = pickle.load(pickle_file)'''

ef = es
ef = set(ef)

audi_models = pd.Series(audi_models)

df = create_make_df(make)
#df['delek_cd']= df['delek_cd'].astype(str)

#b = 5

#kinuy = df2['kinuy_mishari']

#kinuy1 = kinuy.apply(lambda x: difflib.get_close_matches(x, audi_models))

#kinuy = list(set(df['kinuy_mishari'].to_list()))

# create two example series to match
s1 = pd.Series(['apple', 'banana', 'pear', 'orange'])
s2 = pd.Series(['apples', 'bananas', 'peaches', 'grapes'])
#kinuy = s1
#audi_models = s2
# create an empty dataframe to store the results
results = pd.DataFrame(columns=['string_1', 'string_2', 'fuzz_ratio'])

# loop through each combination of strings in the two series
'''for i in kinuy.index:
    for j in audi_models.index:
        # calculate the fuzzy ratio between the two strings
        if kinuy[i][:1] == audi_models[j][:1]:
	        if kinuy[i][:2] == audi_models[j][:2]:
	            ratio = fuzz.ratio(kinuy[i], audi_models[j])
	            # add the results to the dataframe
	            results = results.append({'string_1': kinuy[i], 'string_2': audi_models[j], 'fuzz_ratio': ratio}, ignore_index=True)'''


# display the results

b=5


#df2 = df['kinuy_mishari'].apply(modify_opel)
#b = 5
'''df_gas = df.loc[df['delek_cd'] < 4]
df_gas_models = df_gas['kinuy_mishari'].apply(modify_audi)
gas_models = list(set(df_gas_models.to_list()))


df2 = df[['kinuy_mishari', 'delek_cd', 'degem_cd']]

moo = df.loc[df['delek_cd'] < 4]['kinuy_mishari']
model = df['kinuy_mishari']'''
models1 = df['kinuy_mishari'].to_list()
models = sorted(list(set(models1)))
df['delek_cd'] = df['delek_cd'].apply(lambda x: assign_engine(x))

df['kinuy_mishari'] = df.apply(lambda row: modify_audi(row['kinuy_mishari'], row['delek_cd']), axis=1)
df2 = df.groupby('kinuy_mishari').agg({'kinuy_mishari': 'first', 'degem_cd': ', '.join})
models1 = df['kinuy_mishari'].to_list()
models = sorted(list(set(models1)))
moo = df.loc[df['degem_cd'] == "0212"]['kinuy_mishari']
eng4 = df['kinuy_mishari'].loc[df['delek_cd'] > 3].to_list()
eng4_1 = list(set(eng4))
models1 = df['kinuy_mishari'].to_list()
models = list(set(models1))
with open('audi_models.pkl', 'wb') as pickle_file:
    pickle.dump(models, pickle_file)

#df2['delek_cd']= df2['delek_cd'].apply(lambda x: str(x))
#model2 = df2.groupby('kinuy_mishari').agg({'kinuy_mishari': 'first', 'delek_cd': ', '.join})

match1 = df['kinuy_mishari'].apply(modify_audi)
models = list(set(match1.to_list()))
match = df.loc[df['delek_cd'] < 4]
matches = match.apply(lambda x: fuzz.token_set_ratio(x, 'ETRON'))
b=5

