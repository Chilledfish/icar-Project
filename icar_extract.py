import re
import re
import sqlite3
from urllib.parse import quote
from urllib.request import urlopen
import timeit

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import pickle
import logging
from icar_format import format_icar
import os

# from model_nomalizer import normalize_icar_models
from icar_format import format_icar

# Configure logging
logging.basicConfig(level=logging.INFO)

int_fields = ['year', 'power', 'capacity', 'doors', 'automatic_ind', 'mispar_moshavim', 'delek_cd']
relevant_fields = ['year', 'doors', 'engine', 'ignition', 'sitting', 'gearbox', 'gear', 'piston', 'capacity', 'power', 'loops', 'moment', 'loopmoment', 'acceleration', 'speed', 'urban_consumption', 'intercity_consumption', 'consumption', 'electricity_use', 'battery_capacity', 'electric_range', 'home_charging_time', 'fast_charging_time', 'cenairbag', 'izofix', 'autonomous_braking', 'two_wheeler_identification', 'blind_spot', 'rear_traffic', 'rear_traffic_braking', 'alert_fatigue', 'crossing_warning_open_door', 'child_rear_seat', 'length', 'width', 'height', 'wheel', 'cargo', 'chaircargo', 'selfweight', 'totalweight', 'loading', 'towing_without_brakes', 'towing_with_brakes', 'tire', 'fuel', 'paddle_shifters', 'stop_start', 'electric_handbrake', 'ambient_light', 'hill_assist', 'suspension_dampers']
format_fields = ['sitting', 'ignition', 'gearbox', 'engine']
merge_fields = ['hanaa_nm', 'automatic_ind', 'mispar_moshavim', 'delek_cd']
hebrew_fields = ['שנת דגם',
 'מספר דלתות',
 'הנעה',
 'מקומות ישיבה',
 'תיבת הילוכים',
 "מס' הילוכים",
 'סוג מנוע',
 "מס' בוכנות",
 'נפח (סמ"ק)',
 'הספק מרבי (כ"ס)',
 'סל"ד להספק מרבי',
 'מומנט מרבי (קג"מ)',
 'סל"ד למומנט מרבי',
 'תאוצה 0-100',
 'מהירות מרבית',
 'צריכת דלק - עירונית (ק"מ/ליטר)',
 'צריכת דלק - בינעירונית (ק"מ/ליטר)',
 'צריכת דלק - ממוצעת (ק"מ/ליטר)',
 'צריכת חשמל (וואט שעה / ק"מ)',
 'קיבולת סוללה (קווט"ש)',
 'טווח נסיעה',
 'חשמלי (ק"מ)',
 'זמן טעינה ביתית',
 'זמן טעינה מהירה',
 'ביטול כרית אוויר נוסע',
 'איזופיקס',
 'בלימת חירום אוטונומית',
 'זיהוי דו גלגלי',
 'זיהוי כלי רכב ב"שטח מת"',
 'התרעת תנועה חוצה מאחור',
 'בלימה אוטונומית',
 'בנסיעה לאחור',
 'התרעת עייפות',
 'התרעת רכב חולף בפתיחת דלת',
 'התרעה על שכחת ילד במושב האחורי',
 'אורך (ס"מ)',
 'רוחב (ס"מ)',
 'גובה (ס"מ)',
 'בסיס גלגלים (ס"מ)',
 'נפח תא מטען (ליטרים)',
 'נפח תא מטען בקיפול מושבים (ליטרים)',
 'משקל עצמי (ק"ג)',
 'רכב מסחרי: משקל כולל (ק"ג)',
 'רכב מסחרי: כושר העמסה (ק"ג)',
 'כושר גרירה ללא בלמים',
 'כושר גרירה עם בלמים',
 'קיבולת מיכל דלק (ליטרים)',
 'החלפת הילוכים מגלגל ההגה',
 'מערכת "עצור וסע" לדימום מנוע בעמידה',
 'בלם יד חשמלי',
 'תאורת אווירה',
 'בקרת גלישה במדרון',
 'מתלים ובולמים',
 'רמת גימור',
 'שנת דגם',
 'מספר דלתות',
 'שנת השקת הדגם',
 'הנעה',
 'תיבת הילוכים',
 "מס' הילוכים",
 'סוג מנוע',
 "מס' בוכנות",
 'נפח (סמ"ק)',
 'הספק מרבי (כ"ס)',
 'סל"ד להספק מרבי',
 'מומנט מרבי (קג"מ)',
 'סל"ד למומנט מרבי',
 'תאוצה 0-100',
 'מהירות מרבית',
 'צריכת דלק - עירונית (ק"מ/ליטר)',
 'צריכת דלק - בינעירונית (ק"מ/ליטר)',
 'צריכת דלק - ממוצעת (ק"מ/ליטר)',
 'צריכת חשמל (וואט שעה / ק"מ)',
 'קיבולת סוללה (קווט"ש)',
 'טווח נסיעה',
 'חשמלי (ק"מ)',
 'זמן טעינה ביתית',
 'זמן טעינה מהירה',
 'ביטול כרית אוויר נוסע',
 'איזופיקס',
 'בלימת חירום אוטונומית',
 'זיהוי כלי רכב ב"שטח מת"',
 'התרעת תנועה חוצה מאחור',
 'בלימה אוטונומית',
 'בנסיעה לאחור',
 'התרעת עייפות',
 'התרעת רכב חולף בפתיחת דלת',
 'התרעה על שכחת ילד במושב האחורי',
 'אבזור בטיחותי נוסף',
 'אורך (ס"מ)',
 'רוחב (ס"מ)',
 'גובה (ס"מ)',
 'בסיס גלגלים (ס"מ)',
 'נפח תא מטען (ליטרים)',
 'נפח תא מטען בקיפול מושבים (ליטרים)',
 'משקל עצמי (ק"ג)',
 'רכב מסחרי: משקל כולל (ק"ג)',
 'רכב מסחרי: כושר העמסה (ק"ג)',
 'קיבולת מיכל דלק (ליטרים)',
 'החלפת הילוכים מגלגל ההגה',
 'מערכת "עצור וסע" לדימום מנוע בעמידה',
 'בלם יד חשמלי',
 'תאורת אווירה',
 'בקרת גלישה במדרון',
 'מתלים ובולמים',
 'רמת גימור']
field_names = ['year', 'doors', 'sitting', 'launch', 'ignition', 'gearbox', 'gear', 'engine', 'piston', 'capacity', 'power', 'loops', 'moment', 'loopmoment', 'acceleration', 'speed', 'urban_consumption', 'intercity_consumption', 'consumption', 'electricity_use', 'battery_capacity', 'home_charging_time', 'fast_charging_time', 'cenairbag', 'izofix', 'autonomous_braking', 'two_wheeler_identification', 'blind_spot', 'rear_traffic', 'alert_fatigue', 'crossing_warning_open_door', 'child_rear_seat', 'additional_safety_equipment', 'length', 'width', 'height', 'wheel', 'cargo', 'chaircargo', 'selfweight', 'totalweight', 'loading', 'towing_without_brakes', 'towing_with_brakes', 'fuel', 'trim']
columns = field_names + merge_fields
df = pd.DataFrame(columns=columns)


b = 5


'''def to_int(car_data):
	if car_data == '--':
		return car_data
	return int(car_data)'''


def str_to_int(x):
	try:
		return int(x)
	except ValueError:
		try:
			return float(x)
		except ValueError:
			return x

def connect_to_models_database(MODELS_DB_FILE):
    """Connects to the models database and returns a cursor object"""
    conn = sqlite3.connect(MODELS_DB_FILE)
    create_table_if_not_exists(conn.cursor())
    return conn.cursor()


def connect_to_cars_database(CARS_DB_FILE):
    """Connects to the cars database and returns a cursor object"""
    conn = sqlite3.connect(CARS_DB_FILE)
    return conn.cursor()


def connect_db(file_name) -> sqlite3.Cursor:
    conn = sqlite3.connect(file_name)
    create_table_if_not_exists(conn.cursor())
    return conn.cursor()

def create_table_if_not_exists(cur) -> None:

    cur.execute(('''CREATE TABLE IF NOT EXISTS cars
            (general_model TEXT,
            exact_model TEXT,
            fields BLOB)''')
        )

def get_soup(url):
	response = requests.get(url)
	# response = urlopen(url[0])
	html_content = response.content
	# Parse the HTML content of each website url and extract the small table you are interested in
	soup = BeautifulSoup(html_content, 'lxml')
	return soup


def get_fields(soup):

	title = soup.find('title')
	trim = soup.find('li', {'class': 'active'}).text
	card_soup = soup.select('div.card-body')[:-3]
	#code = '''card_soup = soup.select('div.card-body')'''
	#execution_time = timeit.timeit(title, setup=setup_code, number=1000)
	nested_card_content = [x.contents[1].contents[1::2] for x in card_soup]
	card_content = [item for sublist in nested_card_content for item in sublist]
	final_soup = [content for content in card_content if content.h3.contents[0] in hebrew_fields]
	#field_names = [content.attrs['data-field'] for content in final_soup]
	field_values = [content.contents[3].contents[0].strip() if content.contents[3].contents[0].strip() != '--' else '0' for content in final_soup]
	field_values = [str_to_int(field) for field in field_values]
	field_values.append(trim)
	results_series = pd.Series(field_values, index=field_names)
	results_dict = dict(zip(field_names, field_values))
	format_values = [results_dict.get(x) for x in format_fields]
	#format_dict = dict(zip(format_fields, format_values))
	format_series = pd.Series(format_icar(format_values), merge_fields)
	fields_series = pd.concat([results_series, format_series])
	#results_dict.update(merge_dict)
	#int_values = [int(results_dict.get(field)) for field in int_fields]
	#for field in int_fields:
	#	results_dict[field] = int(results_dict.get(field))
	#results_dict.update({'trim': trim})
	#fields_series = fields_series.reset_index(drop=True)
	fields_series.drop('sitting')

	return fields_series


def apply_func(row):
	soup = get_soup(row['model_url'])
	model_series = pd.Series([row['initial_model'], row['normalized_model']])
	a = row.iloc[0]
	a2= row.iloc[1]
	row = row.drop('model_url')
	fields_series = get_fields(soup)
	row = row.append(fields_series)
	return row

def main():
	with open('audi_urls.pkl', 'rb') as url_file:
		icar_df = pickle.load(url_file)
	columns = ['general_model', 'exact_model'] + field_names + merge_fields
	#columns = columns.remove('sitting')
	df = pd.DataFrame(columns=columns)
	columns2 = field_names + merge_fields
	rows = icar_df
	icar_rows = []
	df2 = rows.apply(apply_func, axis=1)
	with open('audi2.pkl', 'wb') as spec_file:
		pickle.dump(df2, spec_file)

	b=5




	for row in icar_rows:
		apply_func(row)


		#make = row[1]
		general_model = row[3]
		exact_model = row[2]
		version_url = row[4]
		soup = get_soup(version_url)
		#execution_time = timeit.timeit(get_fields(soup), number=1000)
		fields_dict = {'general_model': general_model,
		               'exact_model': exact_model}

		fields_series = get_fields(soup)
		model_series = pd.Series({'general_model': general_model, 'exact_model': exact_model})
		fields_series = pd.concat([fields_series, model_series])

		df.loc[len(df)] = fields_series

		#fields_dict = dict(zip(fields, fields_values))
		#fields_dict.update(merge_dict)
		#fields_blob = pickle.dump(df)



		#translation = dict(zip(fields_hebrew, fields))
		#fields_hebrew_blob = pickle.dumps(translation)


		#model_cursor.execute('''INSERT INTO cars (general_model, exact_model, fields)
	    #                                 VALUES (?, ?, ?)''', (general_model, exact_model, fields_blob))
		#execution_time = timeit.timeit(b, number=1000)
		#model_cursor.connection.commit()
	#model_cursor.connection.close()
	with open('audi.pkl', 'wb') as spec_file:
		pickle.dump(df, spec_file)

	b=5
a = main()
b=5