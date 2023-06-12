import pandas as pd
import collections
import ast
import numpy as np

ncap_years_df = pd.read_csv('ncap_years.csv', index_col=0)
datagov_df = pd.read_csv('n_datagov_safety.csv')

#ncap_df = ncap_df.astype({"years": "Series"})

ncap_df = pd.read_csv('ncap_safety.csv', index_col=0)

ncap_columns = "columns=['make', 'model', 'years', 'Rating', 'Adult_Occupant', 'Child_Occupant', 'Vulnerable_Road_Users', 'Safety_Assist', 'Video_Url']"

safety_df = pd.DataFrame(columns= ["tozeret_cd", "model_cd", "year", "test_year", "Rating", "Adult_Occupant", "Child_Occupant", "Vulnerable_Road_Users", "Safety_Assist", "Video_Url"])

makes = ["Aiways", "Alfa-Romeo", "Audi", "Bentley", "BMW", "Chevrolet", "Citroen", "Dacia", "DS", "Fiat",
         "Ford", "Honda", "Hyundai", "Isuzu", "Jaguar", "Jeep", "Kia", "Lancia", "Land-Rover",
         "Lexus", "Lynk & Co", "Maserati", "Mazda", "Mercedes", "MG", "Mitsubishi",
         "Nissan", "Opel", "Peugeot", "Porsche", "Renault","Saab", "Seat",
         "Skoda", "Smart", "Ssangyong", "Subaru", "Suzuki", "Tesla", "Toyota", "Volkswagen",
         "Volvo"]



def combiner(test_data, datagov_year):

	years = list(ast.literal_eval(test_data[2]))
	#datagov_df_2nd_subset = datagov_df_subset[datagov_df_subset["dmodel"] == model]
	for i in range(len(years)):
		ncap_year = years.pop()
		if ncap_year <= datagov_year:
			return ncap_year
	return None


test_list = []

for make in makes:
	ncap_df_subset = ncap_years_df[ncap_years_df["make"] == make]
	datagov_df_subset = datagov_df[datagov_df["tozar"] == make].reset_index(drop=True)

	if datagov_df_subset.size > 0:
		len_ncap_df = ncap_df_subset.shape[0]
		model_set = set(ncap_df_subset.model)
		#len_data_df = datagov_df_subset.shape[0]
		for i in range(len_ncap_df):
			test_data = ncap_df_subset.iloc[i]
			ncap_model = test_data.iloc[1]
			datagov_df_model_subset = datagov_df_subset[datagov_df_subset["kinuy_mishari"] == ncap_model]
			year = test_data.iloc[2]
			year = ast.literal_eval(year)
			test = tuple(test_data[2])
			len_datagov_model = datagov_df_model_subset.shape[0]

			for j in range(len_datagov_model):
				datagov_row = datagov_df_model_subset.iloc[j]
				integrity_check =  np.isnan(datagov_row['shnat_yitzur'])
				if (integrity_check) is False:
					continue
				try: datagov_year = int(datagov_row['shnat_yitzur'])
				except: continue
				model = datagov_row['kinuy_mishari']
				datagov_data = datagov_df_model_subset.iloc[j].tolist()
				test_year = combiner(test_data, datagov_year)
				if test_year != None:
					datagov_data.append(test_year)
					try:
						ncap_ind = ncap_df.index[
						(ncap_df["Make"] == make) & (ncap_df["Model"] == model) & (ncap_df["Year"] == test_year).tolist()].values[0]
					except:
						continue
					ncap_test = list(ncap_df.iloc[ncap_ind])
					test_percentages = ncap_test[4:-1]
					test_nums = [int(x[:-1]) for x in test_percentages]
					ncap_data = ncap_test[3:]
					test_list_1 = [datagov_data[3], datagov_data[4], datagov_data[2], datagov_data[5], ncap_test[3], test_nums[0], test_nums[1], test_nums[2], test_nums[3], ncap_test[-1]]
					test_list.append(test_list_1)
					try:
						datagov_data[4] = int(datagov_data[4])
					except:
						continue
					datagov_data.extend(ncap_data)
					safety_df.loc[len(safety_df.index)] = test_list_1
				b = 5

safety_df.to_csv('ncap_dataframe2.csv', encoding='utf-8', index=False)





