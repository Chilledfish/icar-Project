import pandas as pd
from icar_variables import *

#makes = ["פיג'ו", "סובארו", "מאזדה", "אאודי", "אלפא_רומיאו", "הונדה", "פיאט", "מרצדס", "לקסוס", "ניסאן", "במוו", "מיצובישי", "לנדרובר", "פולקסווגן", "סיאט", "סוזוקי", "יגואר"]
def model_converter(make):
    best_dict = {'1': '2'}
    model_xl = pd.read_excel("דגמים_upper.xlsx", sheet_name=make, engine='openpyxl', dtype='str')
    if type(model_xl) != dict:
        model_xl.fillna(0, inplace=True)
        model_dict = model_xl.to_dict(orient='list')
    else:
        model_dict = model_xl
    for model_key in model_dict:
        data_models = model_dict.get(model_key)
        count_zeroes = data_models.count(0)
        new_len = len(data_models)-count_zeroes
        data_models = data_models[:new_len]
        model_dict[model_key] = data_models

    return model_dict



#a = model_converter('אאודי')
#b=5

