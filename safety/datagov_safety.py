import pandas as pd
from convert_model import model_converter
from ncap import data_models

makes = ["Aiways", "Alfa-Romeo", "Audi", "BMW", "Chevrolet", "Citroen", "Dacia", "DS", "Fiat",
         "Ford", "Honda", "Hyundai", "Isuzu", "Jaguar", "Jeep", "Kia", "Lancia", "Land-Rover",
         "Lexus", "Lynk & Co", "Maserati", "Mazda", "Mercedes", "MG", "Mitsubishi",
         "Nissan", "Opel", "Peugeot", "Porsche", "Renault", "Seat",
         "Skoda", "Smart", "Ssangyong", "Subaru", "Suzuki", "Tesla", "Toyota", "Volkswagen",
         "Volvo"]
data_makes = ["איוויס", "אלפא רומיאו", "אאודי", "ב מ וו", "שברולט", "סיטרואן", "דאצ'יה", "די.אס", "פיאט", "פורד",
              "הונדה", "יונדאי", "איסוזו", "יגואר", "ג'יפ", "קיה", "לנצ'יה", "לנדרובר", "לקסוס", "לינק אנד קו",
              "מזראטי", "מזדה", "מרצדס", "מ.ג", "מיצובישי", "ניסאן", "אופל", "פיג'ו", "פורשה", "רנו", "סיאט",
              "סקודה", "סמארט", "סאנגיונג", "סובראו", "סוזוקי", "טסלה", "טויוטה", "פולקסווגן", "וולוו"]

eng_heb_dict = dict(zip(makes, data_makes))
heb_eng_dict = dict(zip(data_makes, makes))


ncap_df = pd.read_csv('ncap_df.csv', encoding='utf-8', engine='python')
datagov_df = pd.read_csv('datagov_df.csv', encoding='windows-1255', engine='python')

datagov_normal_df = pd.DataFrame(columns=["dmake", "dmodel", "dyear", "tozeret_cd", "model_cd"])
small_df = datagov_normal_df
a = 1/500
b= 0/500
# datagov_df.size
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
b = [5000*i for i in a]

ranges_dict = dict(zip(a, b))

for j in range(14):
	for i in range(60000, 62711):
		data_row = datagov_df.loc[i]
		tozar = data_row["tozar"]
		make = heb_eng_dict.get(tozar)
		if make == None:
			continue
		model = data_row["kinuy_mishari"]
		model_dict = model_converter(make)
		model = data_models(model, model_dict)
		datagov_df.loc[i, "kinuy_mishari"] = model
		datagov_df.loc[i, "tozar"] = make
		outlist = [make, model, data_row["shnat_yitzur"], data_row["tozeret_cd"], data_row["degem_cd"]]
		datagov_normal_df.loc[i] = outlist
		'''if i > 10:
			if i/10 == 0:
				b=5'''

	file_name = f"datagov_normal13.csv"
	datagov_normal_df.to_csv(file_name)
	datagov_normal_df = pd.DataFrame(columns=["dmake", "dmodel", "dyear", "tozeret_cd", "model_cd"])




audi_df = datagov_df[datagov_df["kinuy_mishari"] == "A1"]

a = audi_df.size
for i in range(ncap_df.size):
	ncap_row = ncap_df.loc[i]
	car = [ncap_row[1], ncap_row[2], ncap_row[3]]
	tozar = eng_heb_dict.get(ncap_row["Make"])
	kinuy_mishari = 1
	shnat_yitzur = 2

b = 5
