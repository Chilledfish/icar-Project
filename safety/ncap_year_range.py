import pandas as pd
import collections


makes = ["Aiways", "Alfa-Romeo", "Audi", "BMW", "Chevrolet", "Citroen", "Dacia", "DS", "Fiat",
         "Ford", "Honda", "Hyundai", "Isuzu", "Jaguar", "Jeep", "Kia", "Lancia", "Land-Rover",
         "Lexus", "Lynk & Co", "Maserati", "Mazda", "Mercedes", "MG", "Mitsubishi",
         "Nissan", "Opel", "Peugeot", "Porsche", "Renault", "Seat",
         "Skoda", "Smart", "Ssangyong", "Subaru", "Suzuki", "Tesla", "Toyota", "Volkswagen",
         "Volvo"]

ncap_df = pd.read_csv('ncap_df.csv', index_col=0)
new_df = pd.DataFrame(columns=['make', 'model', 'years'])

final_df = pd.read_csv('ncap_final.csv', index_col=0)
datagov_df = pd.read_csv('datagov_final.csv', index_col=0)


ncap_df_subset = ncap_df[ncap_df["Make"] == 'Audi']
finder_outer = ncap_df_subset[ncap_df_subset['Model'] == 'A1']
years = []
for make in makes:
	ncap_df_subset = ncap_df[ncap_df["Make"] == make]
	model_list = list(ncap_df_subset.Model)
	model_set = set(model_list)
	counter = dict(collections.Counter(model_list))
	for model in model_set:
		model_ind = ncap_df.index[(ncap_df["Make"] == make) & (ncap_df["Model"] == model)].tolist()
		for ind in model_ind:
			data_list = ncap_df_subset.loc[ind].tolist()
			years.append(data_list[2])
			out_list = data_list[:3]

		years = tuple(years)
		out_list[2] = years
		years = []
		new_df.loc[len(new_df.index)] = out_list

new_df.to_csv('ncap_final.csv')




