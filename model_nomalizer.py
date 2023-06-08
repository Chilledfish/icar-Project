import pandas as pd
import csv
from icar_convert_model import model_converter
from icar_variables import *
import numpy as np

make = 'מאזדה'
makes = ["DS", "סרס", "פיאט", "אאודי", "אופל", "אייוייז", "איווקו", "ניסאן", "איסוזו", "אלפא רומיאו", "אסטון מרטין",
         "ב.מ.וו", "ביואיק", "בנטלי", "ג'ילי", "גיפ", "יונדאי", "גרייטוול", "דאצ'יה", "דודג'", "דייהטסו", "האמר",
         "הונדה", "וולוו", "טויוטה", "טסלה", "יגואר", "יונדאי", "לינקולן", "לנדרובר", "לנצ'יה", "טויוטה", "מאזדה",
         "מאן", "מזראטי", "ב.מ.וו", "מיצובישי", "מקסוס", "מרצדס", "ניסאן", "סאאב", "סאיק-MG", "סאנגיונג", "סובארו",
         "סוזוקי", "סיאט", "סיטרואן", "סמארט", "סקודה", "סקייוול", "פולקסווגן", "פונטיאק", "פורד", "פורשה", "פיאט",
         "פיג'ו", "פרארי", "קדילאק", "סיאט", "קיה", "קרייזלר", "דודג'", "רנו", "שברולט"]

icar_make_dict = {"DS": "DS",
                  "SERES": "סרס",
                  "אבארט": "פיאט",
                  "אודי": "אאודי",
                  "אופל": "אופל",
                  "איווייז": "אייוייז",
                  "איווקו": "איווקו",
                  "אינפיניטי": "ניסאן",
                  "איסוזו": "איסוזו",
                  "אלפא רומיאו": "אלפא רומיאו",
                  "אסטון מרטין": "אסטון מרטין",
                  "ב.מ.וו": "ב.מ.וו",
                  "ביואיק": "ביואיק",
                  "בנטלי": "בנטלי",
                  "ג'ילי": "ג'ילי",
                  "גיפ": "גיפ",
                  "ג'נסיס": "יונדאי",
                  "גרייטוול": "גרייטוול",
                  "דאציה": "דאצ'יה",
                  "'דודג": "דודג",
                  "דייהטסו": "דייהטסו",
                  "האמר": "האמר",
                  "הונדה": "הונדה",
                  "וולוו": "וולוו",
                  "טויוטה": "טויוטה",
                  "טסלה": "טסלה",
                  "יגואר": "יגואר",
                  "יונדאי": "יונדאי",
                  "לינקולן": "פורד",
                  "לנדרובר": "לנדרובר",
                  "לנציה": "לנצ'יה",
                  "לקסוס": "טויוטה",
                  "מאזדה": "מאזדה",
                  "מאן": "מאן",
                  "מזראטי": "מזראטי",
                  "מיני": "ב.מ.וו",
                  "מיצובישי": "מיצובישי",
                  "מקסוס": "מקסוס",
                  "מרצדס": "מרצדס",
                  "ניסאן": "ניסאן",
                  "סאאב": "סאאב",
                  "סאיק-MG": "סאיק-MG",
                  "סאנגיונג": "סאנגיונג",
                  "סובארו": "סובארו",
                  "סוזוקי": "סוזוקי",
                  "סיאט": "סיאט",
                  "סיטרואן": "סיטרואן",
                  "סמארט": "סמארט",
                  "סקודה": "סקודה",
                  "סקייוול": "סקייוול",
                  "פולקסווגן": "פולקסווגן",
                  "פונטיאק": "פונטיאק",
                  "פורד": "פורד",
                  "פורשה": "פורשה",
                  "פיאט": "פיאט",
                  "פיג'ו": "פיג'ו",
                  "פרארי": "פרארי",
                  "קדילאק": "קדילאק",
                  "קופרה": "סיאט",
                  "קיה": "קיה",
                  "קרייזלר": "קרייזלר",
                  "ראם": "דודג'",
                  "רנו": "רנו",
                  "שברולט": "שברולט"}
datagov_make_dict = {"אאודי": "אאודי",
                     "אופל": "אופל",
                     "איווייס": "אייוייז",
                     "איווקו": "איווקו",
                     "איסוזו": "איסוזו",
                     "אלפא רומיאו": "אלפא רומיאו",
                     "אסטון מרטין": "אסטון מרטין",
                     "במוו": "ב.מ.וו",
                     "ב מ וו": "ב.מ.וו",
                     "ביואיק": "ביואיק",
                     "בנטלי": "בנטלי",
                     "ג'יפ": "ג'יפ",
                     "גופל": "גופל",
                     "גילי": "ג'ילי",
                     "גרייטוול": "גרייטוול",
                     "דאציה": "דאצ'יה",
                     "דודג'": "דודג",
                     "די.אס": "DS",
                     "דייהטסו": "דייהטסו",
                     "האמר": "האמר",
                     "הונדה": "הונדה",
                     "וולבו": "וולבו",
                     "טויוטה": "טויוטה",
                     "טסלה": "טסלה",
                     "יגואר": "יגואר",
                     "יונדאי": "יונדאי",
                     "לינקולן": "פורד",
                     "לנדרובר": "לנדרובר",
                     "לנצ'יה": "לנצ'יה",
                     "לקסוס": "טויוטה",
                     "מ א ן": "מאן",
                     "מ.ג": "סאיק-MG",
                     "מזארטי": "מזארטי",
                     "מזדה": "מאזדה",
                     "מיצובישי": "מיצובישי",
                     "מקסוס": "מקסוס",
                     "מרצדס": "מרצדס",
                     "ניסאן": "ניסאן",
                     "סאאב": "סאאב",
                     "סאנגיונג": "סאנגיונג",
                     "סובארו": "סובארו",
                     "סוזוקי": "סוזוקי",
                     "סיאט": "סיאט",
                     "סיטרואן": "סיטרואן",
                     "סמארט": "סמארט",
                     "סקודה": "סקודה",
                     "סקיוול": "סקיוול",
                     "סרס": "סרס",
                     "פולקסווגן": "פולקסווגן",
                     "פורד": "פורד",
                     "פורשה": "פורשה",
                     "פיאט": "פיאט",
                     "פיג'ו": "פיג'ו",
                     "פרארי": "פרארי",
                     "קאדילאק": "קדילאק",
                     "קיה": "קיה",
                     "קרייזלר": "קרייזלר",
                     "רובר": "לנדרובר",
                     "רנו": "רנו",
                     "שברולט": "שברולט", }
def normalize_model(in_model, model_column):
    if make not in datagov_make_dict.values() or make not in icar_make_dict.values():
        return f"{make}car_model"
    try:
        model_df = pd.read_excel("דגמים4.xlsx", engine='openpyxl', sheet_name=make, index_col=None, names=None)
    except:
        return 'Missing make'
    model = in_model.upper()
    try:
        model_df.loc[model_df.shape[0] + 1,''] = np.nan
        #model_df = model_df.concat(pd.Series(), ignore_index=True)
        #pd.concat([model_df, pd.DataFrame([[np.nan] * model_df.shape[1]], columns=model_df.columns)], ignore_index=True)
        model_df.iloc[-1] = model_df.columns
    except:
        return f"{in_model}car_model"
    model_df.index = model_df.index + 1
    model_df = model_df.sort_index()

    model_find = model_column[model_column == model].index.tolist()
    if len(model_find) == 0:

        normalized_model = model_find[0][1]
    return normalized_model


'''n_model = ''
car_translation = {"אאודי": "Audi",
                   "ביואיק": "Buick",
                   "ב.מ.וו": "BMW",
                   "אופל": "Opel",
                   "איסוזו": "Isuzu",
                   "מרצדס": "Mercedes",
                   "איווקו": "Iveco",
                   "מזדה": "Mazda",
                   "מאן": "Mann",
                   "פיאט": "Fiat",
                   "האמר": "Hummer",
                   "ניסאן": "Nissan",
                   "טויוטה": "Toyota",
                   "פולקסווגן": "VW",
                   "ג'יפ": "Jeep",
                   "מאזדה": "Mazda",
                   "סיטרואן": "Citroen",
                   "סוזוקי": "Suzuki",
                   "יונדאי": "Hyundai",
                   "הונדה": "Honda",
                   "פיג'ו": "Peugeot",
                   "דאציה": "Dacia",
                   "וולבו": "Volvo",
                   "לקסוס": "Lexus",
                   "קיה": "Kia",
                   "מ.ג": "MG",
                   "גרייט וול": "Great Wall",
                   "מיצובישי": "Mitsubishi",
                   "דייהטסו": "Daihatsu",
                   "סובארו": "Subaru",
                   "סקודה": "Skoda",
                   "סאנגיונג": "Ssangyoung",
                   "ב מ וו": "BMW",
                   "יגואר": "Jaguar",
                   "פורד": "Ford",
                   "פורשה": "Porce",
                   "פיאג'ו": "Piaggio",
                   "שברולט": "Chevrolet",
                   "רנו": "Renault",
                   "קרייזלר": "Chrysler",
                   "מ א ן": "Mann",
                   "רובר": "Land Rover",
                   "מקסוס": "Maxus",
                   "סיאט": "Seat",
                   "קאדילאק": "Cadillac",
                   "טסלה": "Tesla",
                   "די.אס": "DS",
                   "אלפא רומיאו": "Alfa Romeo",
                   "לנצ'יה": "Lancia",
                   "דודג'": "Dodge",
                   "אסטון מרטין": "Aston Martin",
                   "לינקולן": "Lincoln",
                   "סאאב": "Saab",
                   "סמארט": "Smart",
                   "פרארי": "Ferrari",
                   "מזארטי": "Masaratti",
                   "בנטלי": "Bently",
                   "לנדרובר": "Land Rover",
                   "ג'.מ": "GM",
                   "איווייס": "Aiways",
                   "גילי": "Geely"}
make_e = car_translation[make]
csvfile = f'{make}.csv'
formatted_file = f"f_{make}.csv"
tozar = make_to_tozar[make]
tozar = make
outfile = f"{make}_out.csv"
data_file = f"{make}_data.csv"
icar_file = f"{make}_icar.csv"
datagov = pd.read_csv('datagov_csv.csv', encoding='windows-1255', engine='python')
data_df = datagov[datagov['tozar'] == make]
data_df.reset_index(drop=True, inplace=True)
makefile_dict = {"אודי": "אאודי",
                  "אינפיניטי": "ניסאן",
                  "אלפא_רומיאו": "אלפא_רומיאו",
                  "אסטון_מרטין": "אסטון מרטין",
                  "ב מ וו": "ב.מ.וו",
                  "גילי": "ג'ילי",
                  "ג'נסיס": "יונדאי",
                  "גיפ": "ג'יפ",
                  "דאציה": "דאצ'יה",
                  "דודג'": "קרייזלר",
                  "דודג": "קרייזלר",
                  "וולבו": "וולוו",
                  "די אס": "DS",
                  "די.אס": "DS",
                  "יונדאי": "יונדאי",
                  "לינקולן": "פורד",
                  "לנציה": "לנצ'יה",
                  "לקסוס": "טויוטה",
                  "מזדה": "מאזדה",
                  "מ א ן": "מאן",
                  "מיני": "ב.מ.וו",
                  "מ.ג": "סאיק-MG",
                  "קופרה": "סיאט",
                  "פיגו": "פיג'ו",
                  "קאדילאק": "קדילאק",
                  "ראם": "קרייזלר",
                  }
icar_df = pd.read_csv(formatted_file, dtype=dtypes)'''


# ----------------------------------------------------------------------------

'''def normalize_icar_model(model):
    match_list = [car_model for car_model in model_keys if model.find(car_model) > -1]
    if len(match_list) > 1:
        return max(match_list)
    return match_list'''
# ----------------------------------------------------------------------------

'''def normalize_datagov_models(model):
    for i in range(len(model_dict)):
        if model in model_values[i]:
            return model_keys[i]'''
# ----------------------------------------------------------------------------

'''model_dict = model_converter(make)
model_dict_items = model_dict.items()
model_keys = [str(car_model[0]) for car_model in model_dict_items]
model_values = [str(car_model[1]) for car_model in model_dict_items]
keys = list(model_dict)
key = keys[5]
# ----------------------------------------------------------------------------

icar_models = icar_df["model"]
icar_n_models = []
# ----------------------------------------------------------------------------

data_models = data_df["kinuy_mishari"]
data_n_models = []'''
# ----------------------------------------------------------------------------



# ----------------------------------------------------------------------------


b=5