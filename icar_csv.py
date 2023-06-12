import numpy as np
import pandas as pd

makes_list = ["DS", "אודי", "אופל", "איווקו", "אייוייז", "אלפא רומיאו", "איסוזו", "אסטון מרטין", "ב.מ.וו", "ג'ילי", "ג'יפ", "גרייט וול",
              "דאצ'יה", "דודג", "דייהטסו", "האמר", "הונדה", "וולוו", "טויוטה", "טסלה", "יגואר", "לנדרובר", "לנצ'יה", "מאזדה", "מאן",
              "מזראטי", "מיצובישי", "מקסוס", "מרצדס", "ניסאן", "סאאב", "סאיק-MG", "סאנגיונג", "סובארו", "סוזוקי", "סיאט", "סיטרואן",
              "סמארט", "סקודה", "סקייוול", "פולסטאר", "פולקסווגן", "פורד", "פורשה", "פיאט", "פיג'ו", "פרארי",
              "קדילאק", "קיה", "קרייזלר", "רנו", "שברולט"]

df_columns = ["make", "model", "ramat_gimur", "year", "doors", "sitting", "ignition", "gearbox", "gear", "engine", "piston", "capacity", "power", "loops", "moment", "loopmoment", "acceleration", "speed", "urban_consumption", "intercity_consumption", "consumption", "electricity_use", "battery_capacity", "electric_range", "home_charging_time", "fast_charging_time", "brake", "airbag", "stability", "cenairbag", "length", "width", "height", "wheel", "cargo", "chaircargo", "selfweight", "totalweight", "loading", "towing_without_brakes", "towing_with_brakes", "tire", "fuel", "hanaa_nm", "automatic_ind", "sitting_num", "engine_cd", "n_model"]

df = pd.DataFrame(columns=df_columns)
b = ''
for make in makes_list:
    print(make)
    new_df = pd.read_csv(f"{make}.csv")
    new_df.rename(columns= {'sitting.1': 'sitting_num'}, inplace=True)
    n_models = new_df['n_model']
    new_df.pop('Unnamed: 0')

    df = pd.concat([df, new_df], axis=0)
    #df.loc[:,len(df.index)] = new_df

n_models = df['n_model']



def func(x):
    x = str(x)
    if x.find('missing') > -1:
        return False
    return True

mask = n_models.apply(func)
df2 = df[mask == True]

