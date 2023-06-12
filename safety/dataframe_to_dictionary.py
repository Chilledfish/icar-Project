import pandas as pd


def model_converter(make):
    best_dict = dict()

    model_xl = pd.read_excel("ncap_models.xlsx", sheet_name=make, engine='openpyxl', dtype='str')
    model_xl.fillna(0, inplace=True)
    model_dict = model_xl.to_dict(orient='list')
    for model_key in model_dict:
        data_models = model_dict.get(model_key)
        count_zeroes = data_models.count(0)
        new_len = len(data_models)-count_zeroes
        data_models = data_models[:new_len]
        model_dict[model_key] = data_models

    return model_dict



def normalize_datagov_models(model, model_dict, model_values, model_keys):
    for i in range(len(model_dict)):
        if model in model_values[i]:
            return model_keys[i]