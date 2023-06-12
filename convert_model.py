import pandas as pd
from icar_variables import *

#makes = ["פיג'ו", "סובארו", "מאזדה", "אאודי", "אלפא_רומיאו", "הונדה", "פיאט", "מרצדס", "לקסוס", "ניסאן", "במוו", "מיצובישי", "לנדרובר", "פולקסווגן", "סיאט", "סוזוקי", "יגואר"]
def model_converter(df, model):
    best_dict = {'1': '2'}
    df.iloc[-1] = df.columns
    model_series = df.stack()
    if type(df) != dict:
        df.fillna(0, inplace=True)
        model_dict = df.to_dict(orient='list')
        model_find = model_series[model_series == model].index.tolist()
        if len(model_find) == 0:
            normalized_model = model_find[0][1]
        return normalized_model



    else:
        model_dict = df
    for model_key in model_dict:
        data_models = model_dict.get(model_key)
        count_zeroes = data_models.count(0)
        new_len = len(data_models)-count_zeroes
        data_models = data_models[:new_len]
        model_dict[model_key] = data_models

    return model_dict



a = model_converter('אאודי')
b=5

