import pandas as pd




file_name = 'rishui'
file_name2 = 'rishui2.csv'
out_file = 'rishui_out'
#def df_creator(chunk):


columns = ['tozeret_cd', 'degem_cd']
count_columns = ['tozeret_cd', 'degem_cd', 'size']
chunks = []
chunk = 10 ** 5
'''with pd.read_csv(file_name, chunksize=chunksize) as reader:
	for i in reader:
		pass'''
# chunksize=chunksize

final_car_df = pd.DataFrame(columns=columns)
p = 0
for i in range(1, 3):
	reader = pd.read_csv(f"{file_name}{i}.csv", iterator=True, error_bad_lines=False, chunksize=1000, encoding='windows-1255', delimiter='|', usecols=columns)

	df_list = []
	#i = 0
	car_count_list = []

	a = ''

	car_df = pd.DataFrame(columns=columns)
	car_df2 = pd.DataFrame(columns=columns)
	car_count = pd.DataFrame(columns=count_columns)
	car_list = []
	for j in range(10):
		try:
			for item in reader:
				new_df = item
				car_df = pd.concat([car_df, new_df])
				if car_df.shape[0] > 299999:
					p += 1
					car_df.to_csv(f"{out_file}{p}.csv", encoding='utf-8', index=False)
					car_df = pd.DataFrame(columns=columns)


		except:
			print(i+p)
			pass
		car_list.append(car_df)
		car_df.to_csv(f"{out_file}{p}.csv", encoding='utf-8', index=False)
		car_df = pd.DataFrame(columns=columns)

		b = 5

car_counter = [x.groupby(x.columns.tolist(), as_index=False).size() for x in car_list]


				#	 = car_df.groupby(car_df.columns.tolist(), as_index=False).sum()
				#car_df2 = new_df.groupby(new_df.columns.tolist(), as_index=False).size()
				#car_df2 = car_df.groupby(ca)

				#car_df2 = car_count[columns]
				# car_df = car_count[columns]






	#final_car_df = pd.concat([final_car_df, car_df])
	#car_count2 = final_car_df.groupby(final_car_df.columns.tolist(), as_index=False).sum()



car_count = final_car_df.groupby(car_df.columns.tolist(), as_index=False).sum()

car_df.to_csv('all_cars.csv', encoding='utf-8', index=False)

car_count = car_df.groupby(car_df.columns.tolist(), as_index=False).size()
car_count_df = car_count[car_count['size'] > 7]
car_count_df.to_csv('car_count_noyear.csv', encoding='utf-8', index=False)
car_df.to_csv('all_cars.csv', encoding='utf-8', index=False)
