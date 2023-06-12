import pandas as pd
import numpy as np

make_dict = {"DS": "DS",
                  "די אס": "DS",
                  "די.אס": "DS",
                  "SERES": "סרס",
                  "אבארט": "פיאט",
                  "אודי": "אאודי",
                  "אופל": "אופל",
                  "איווייז": "אייוייז",
                  "אייוייז": "אייוייז",
                  "איווקו": "איווקו",
                  "אינפיניטי": "ניסאן",
                  "איסוזו": "איסוזו",
                  "אלפא רומיאו": "אלפא רומיאו",
                  "אסטון מרטין": "אסטון מרטין",
                  "ב.מ.וו": "ב.מ.וו",
                  "ב מ וו": "ב.מ.וו",
                  "במוו": "ב.מ.וו",
                  "ביואיק": "ביואיק",
                  "בנטלי": "בנטלי",
                  "ג'ילי": "ג'ילי",
                  "גיפ": "ג'יפ",
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
                  "מזדה": "מאזדה",
                  "מאזדה": "מאזדה",
                  "מאן": "מאן",
                  "מ א ן": "מאן",
                  "מזראטי": "מזראטי",
                  "מיני": "ב.מ.וו",
                  "מיצובישי": "מיצובישי",
                  "מקסוס": "מקסוס",
                  "מרצדס": "מרצדס",
                  "ניסאן": "ניסאן",
                  "ניסאן2": "ניסאן",
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
                  "רובר": "לנדרובר",
                  "רנו": "רנו",
                  "שברולט": "שברולט"}


def get_model_df(make):
    if make in make_dict:
        make = make_dict.get(make)
    model_df = pd.read_excel("דגמים4.xlsx", engine='openpyxl', sheet_name=make, index_col=None, names=None)
    ''' The header, which is the common model name, isn't part of the list. I add a blank row, and populate it with the header, so it will be a part of the search '''
    model_df.loc[model_df.shape[0] + 1, ''] = np.nan
    df_column_list = model_df.columns.tolist()
    df_columns_str_list = [str(x) for x in df_column_list]
    model_df.iloc[-1] = df_columns_str_list
    model_df.index = model_df.index + 1
    model_df = model_df.sort_index()
    n_model_series = model_df.stack().astype('str')

    return n_model_series






datagov_makes = ["די.אס", "אאודי", "אופל", "איווקו", "איווייס", "אלפא רומיאו", "איסוזו", "אסטון מרטין", "ב מ וו", "גילי", "ג'יפ",
                 "גרייט וול", "דאציה", "דייהטסו", "האמר", "הונדה", "וולבו", "טויוטה", "טסלה", "יגואר", "לנדרובר", "לנצ'יה",
                 "מזדה", "מאן", "מ א ן", "מזראטי", "מיצובישי", "מקסוס", "מרצדס", "ניסאן", "סאאב", "מ.ג", "סאנגיונג", "סובארו", "סוזוקי",
                 "סיאט", "סיטרואן", "סמארט", "סקודה", "סקייוול", "פולסטאר", "פולקסווגן", "פורד", "פורשה", "פיאט", "פיג'ו", "פרארי",
                 "קאדילאק", "קיה", "קרייזלר", "רנו", "שברולט"]

icar_makes_list = ["DS", "אודי", "אופל", "איווקו", "אייוייז", "אלפא רומיאו", "איסוזו", "אסטון מרטין", "ב.מ.וו", "ג'ילי", "ג'יפ",
                   "גרייט וול", "דאצ'יה", "דייהטסו", "האמר", "הונדה", "וולוו", "טויוטה", "טסלה", "יגואר", "לנדרובר", "לנצ'יה",
                   "מאזדה", "מאן", "מ א ן", "מזראטי", "מיצובישי", "מקסוס", "מרצדס", "ניסאן", "סאאב", "סאיק-MG", "סאנגיונג", "סובארו",
                   "סוזוקי",
                   "סיאט", "סיטרואן", "סמארט", "סקודה", "סקייוול", "פולסטאר", "פולקסווגן", "פורד", "פורשה", "פיאט", "פיג'ו", "פרארי",
                   "קדילאק", "קיה", "קרייזלר", "רנו", "שברולט"]

data_icar_dict = dict(zip(datagov_makes, icar_makes_list))


df = pd.read_csv('datagov2.csv', encoding='utf-8')



tozar_series = df['tozar']

#model_find = model_column[model_column == model].index.tolist()

tozar_series = tozar_series.apply(lambda x: data_icar_dict.get(x))
df['tozar'] = tozar_series
tozars = tozar_series.unique().tolist()
n_series = pd.Series()
n_list = []
for tozar in tozars:

    tozar_df = df.loc[df['tozar'] == tozar]
    model_series = tozar_df['kinuy_mishari']
    model_series.apply(lambda x: str(x))

    n_model_df = get_model_df(tozar)
    def get_n_model(model, n_model_df=n_model_df):
        n_index = n_model_df[n_model_df == model].index.tolist()
        if len(n_index) > 0:
            try:
                n_model = str(n_index[0][1])
                return n_model
            except:
                print(f"{n_index}, problem")
                return n_index
    #n_model_series.apply(lambda car_model: str(car_model))
    new_n_model_series = model_series.apply(get_n_model)
    new_n_list = new_n_model_series.tolist()
    n_list.extend(new_n_list)

df['n_model'] = n_list

hanaa = df['hanaa_nm']

df.to_csv('datagov_for_merge.csv', encoding='utf-8', index=False)






b=5




'''df2 = pd.DataFrame(columns=df.columns)
index_names = []
for make in datagov_makes:
    index_names.extend(df[df['tozar'] == make].index.tolist())

tozar = tozar_series.unique().tolist()

for i in index_names:
    df2.loc[len(df2.index)] = df.iloc[i]
df2.to_csv('datagov2.csv', index=False, encoding='utf-8')
df.drop(index_names, inplace=True)

tozar_series = df['tozar']
tozar = tozar_series.unique().tolist()
makes = ''
for make in tozar:
    makes += f"{make}, "
df.loc[len(df.index)]'''

data_merge_values = ['tozar', 'shnat_yitzur', 'kvuzat_agra_cd', 'nefah_manua', 'koah_sus', 'hanaa_nm', 'automatic_ind', 'mispar_dlatot', 'mispar_moshavim', 'delek_cd', 'n_model']

'''def get_n_model(model):
    model_find = model_column[model_column == model].index
        return model_find[0][1]
    print(model)
    return f"{model}_missing"'''


b = 5
