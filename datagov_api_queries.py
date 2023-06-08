import pickle
import pandas as pd
import requests
import re
import icar_normalize
import os
import sqlite3

with open('datagov2022', 'rb') as pickle_file:
    datagov_df = pickle.load(pickle_file)


b = 5

# this adds crash test urls to ncap df
'''for i in range(len(safety_detail_list)):
    safety_detail_list[i].append(youtube_urls[i])

ncap_youtube_links_2022 = open('ncap_youtube_links_2022_2', 'ab')
pickle.dump(safety_detail_list, ncap_youtube_links_2022)
ncap_youtube_links_2022.close()'''

'''data_makes = ['קארמה', 'די.אס', 'סיטרואן', 'רנו', 'לינקולן', 'וואי', "ג'.מ", 'אאודי', 'סקודה', 'קרייזלר', 'אופל',
              'ב מ וו',
              'טסלה', 'פורשה', 'פיאט', "פיג'ו", 'סקיוול', 'טויוטה', 'אלפא רומיאו', 'ניסאן', "דודג'", 'קאדילאק',
              'קיה', 'פולקסווגן', 'שברולט', "ג'יפ", 'מקסוס', 'סובארו', 'מ.ג', 'בי ווי די', 'אסטון מרטין', 'סרס',
              'אורה', 'אף אי דאבל יו', 'סיאט', "צ'רי", 'מיצובישי', 'לאמבורגיני', 'וולבו', 'יגואר', 'פולסטאר',
              'ליפמוטור', 'סוזוקי', 'לקסוס', 'גילי', 'אל אי וי סי', 'הונדה', 'פרארי', 'לינק אנד קו', 'רובר', 'פורד',
              'גי.אי.סי', 'מאן', 'סמארט', 'מרצדס', 'סאנגיונג', 'מזארטי', 'איסוזו', 'בנטלי', 'דאציה', 'לנדרובר', 'מזדה',
              'איווייס', 'יונדאי', 'די אס']'''




def create_make_df(columns, make, years=range(2009,2023), limit=25000):

    query_url = create_api_url(make, years, limit)

    data_page = requests.get(query_url)
    obj = data_page.json()
    data_cars_all_columns = obj['result']['records']
    #df = pd.DataFrame(data_cars_all_columns)
    a1 = [x['kinuy_mishari'] for x in data_cars_all_columns]
    a2 = list(set(a1))
    a = pd.Series(a2)

    data_cars_str = [[x[y] for y in columns] for x in data_cars_all_columns]
    data_cars = []
    x = 'Q4 SBACK50 ETRO'
    #m = icar_normalize.audi_normalize(x)
    for x in data_cars_str:
        x[3] = icar_normalize.normalize_audi_model(x[3])
        x = ['0' if y == '' else y for y in x]
        data_cars.append([str(x[0]), str(x[1]), x[2], x[3], int(x[4]), x[5], int(x[6]), int(x[7]), int(x[8]), x[9], int(x[10]), int(x[11]), int(x[12])])
    data_car_dict = {}

    for car in data_cars:
        temp_dict = dict(zip(columns, car))
    df = pd.DataFrame(data_cars, columns=columns)
    #df2 = pd.DataFrame(data_cars_str, columns=columns




    #    pickle.dump(tozarim, pickle_file)
    #a = list(set(df['kinuy_mishari'].to_list()))

    return df

def create_api_url(make, years, limit=10000):
    print(years)
    api_base_url = "https://data.gov.il/api/3/action/datastore_search?resource_id=142afde2-6228-49f9-8a29-9b6c3a0cbe40"
    kwargs = dict()
    result = []

    kwargs['tozar'] = "\"" + make + "\""
    year_string = "[" + ", ".join(['"' + str(item) + '"' for item in years]) + "]"
    kwargs['shnat_yitzur'] = year_string

    for key in kwargs:
        result.append(f'"{key}": {kwargs[key]}')

    filter = '{' + ', '.join(result) + '}'
    query_url = f"{api_base_url}&limit={limit}&filters={filter}"
    return query_url


a = __name__
b =5

def main():
    columns = ['tozeret_cd', 'degem_cd', 'tozar', 'kinuy_mishari', 'shnat_yitzur', 'ramat_gimur', 'delek_cd',
               'mispar_dlatot', 'automatic_ind', 'hanaa_nm', 'nefah_manoa', 'koah_sus', 'mispar_moshavim']

    df = create_make_df(columns, "אאודי")
    with open('audi_datagov.pkl', 'wb') as pickle_file:
        pickle.dump(df, pickle_file)

    with open('datagov2022', 'rb') as pickle_file:
        datagov_df = pickle.load(pickle_file)

    with open('datagov_makes', 'rb') as pickle_file:
        tozarim = pickle.load(pickle_file)

    with open('אאודי', 'rb') as pickle_file:
        audi = pickle.load(pickle_file)

    filter = {'shnat_yitzur': [2009,2023]}

    #a = create_query(filter)



    with open('אאודי', 'rb') as pickle_file:
        nissan = pickle.load(pickle_file)




    file_name = 'audi_data.sql'

    if os.path.exists(file_name):
        os.remove(file_name)


    conn = sqlite3.connect(file_name)

    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS cars
                   (make TEXT,
                    model TEXT,
                    heb_fields BLOB,
                    eng_fields BLOB,
                    merge_fields BLOB)''')








    #datagov_df = df


    makes = list(set(datagov_df['tozar'].to_list()))
    values = sorted(makes)
    value1 = values[0]
    a = re.match('אאא', values[0])

    current_year = datagov_df["shnat_yitzur"].to_list()
    current_year = list(set(current_year))

    current_year = current_year.sort()



    ncap_columns = ['model', 'rating', 'adult', 'passenger', 'pedestrians', 'safety equipment', 'car page',
                    'crash test video']



    b=5
    d_makes_translation = ['Karma', 'DS', 'Citroen', 'Renault', 'Lincoln', 'WEY', 'GM', "Audi", 'Skoda', 'Chrysler', 'Opel',
                           'BMW', 'Tesla', 'Porche', 'Fiat', 'Peugeot', 'Skywell', 'Toyota', 'Alfa_Romeo', 'Nissan',
                           'Dodge', 'Cadillac', 'Kia', 'VW', 'Chevrolet', 'Jeep', 'Maxus', 'Subaru', 'MG', 'BYD',
                           'Aston Martin', 'Seres', 'Ora', 'FEW', 'Seat', 'Cherry', 'Mitsubishi', 'Lamborghini', 'Volvo',
                           'Jaguar', 'Polestar', 'Leapmotor', 'Suzuki', 'Lexus', 'Geely', 'LEVC', 'Honda', 'Ferrari',
                           'Lynk & Co', 'Land Rover', 'Ford', 'GEC', 'MANN', 'Smart', 'Mercedes', 'SSangyong', 'Maserati',
                           'Isuzu', 'Bentley', 'Dacia', 'Land Rover', 'Mazda', 'Aiways', 'Hyundai', 'DS'
                           ]
    # data_makes = d_makes.data_makes
    # data_makes_dict = d_makes.ncap_data_dict
    # data_makes_reversed = dict([(value, key) for key, value in data_makes_dict.items()])

    b=5

    parameters = {
        'limit': 100,
        # 'records': records
    }
    with open('makes', 'rb') as pickle_file:
        makes = pickle.load(pickle_file)
    b=5

    ['tozeret_cd', 'degem_cd', 'tozar', 'kinuy_mishari', 'shnat_yitzur', 'ramat_gimur', 'delek_cd',
               'mispar_dlatot', 'automatic_ind', 'hanaa_nm', 'nefah_manoa', 'koah_sus', 'mispar_moshavim', 'kvuzat_agra_cd']
    b=5







    file_name = 'mazda_datagov.db'



    if os.path.exists(file_name):
        os.remove(file_name)

    conn = sqlite3.connect(file_name)




    sqlll = df.to_sql('data_gov', conn, if_exists='replace')
    c = conn.cursor()
    c.execute("SELECT degem_cd FROM data_gov")

    rows = c.fetchall()

    b=5
b=5
main()
if __name__ == '__main__':
    main()


#cursor = conn.cursor()









b=5








'''dgamim_all = df['kinuy_mishari'].to_list()
    #dgamim = [car_model[5:] if re.match("AUDI", car_model)  else car_model for car_model in dgamim_all]
    #dgamim = [car_model[:car_model.find('SBACK')] + 'SPORTBACK' if car_model.find('SBACK') > -1 else car_model for car_model in dgamim]
    #dgamim = [car_model[:car_model.find('SB')] + 'SPORTBACK' if car_model.find('SB') > -1 else car_model for car_model in dgamim]
    #dgamim = [car_model[:car_model.find('SPORTBACK') + 9] if car_model.find('SPORTBACK') > -1 else car_model for car_model in dgamim]
    dgamin_series = df['kinuy_mishari']
    #dgamin_series.apply()


    #engine_all = d

    items = []
    i = 5
    item = dgamim_all[i]
    for i in range(len(dgamim_all)):
        space_ind = None
        item = dgamim_all[i]
        if item.find("AUDI") > -1:
            item = item[5:]
        if item.isspace():
            space_ind = item.index(" ")
        car_model = item.find("SB") + item.find("SP")
        if car_model > -1:
            item = item[:2] + " " + "SPORTBACK"

        items.append(item)
    dgamim_all[i] = item

    items2 = list(set(items))
    items = list(set(dgamim_all))
    dgamim = []
    for car_model in dgamim_all:
        if re.match("AUDI", car_model):
           car_model = car_model[5:]


    df['kinuy_mishari'] = dgamim
    df2 = df.groupby('kinuy_mishari', as_index=False).agg({'kinuy_mishari': 'first', 'degem_cd': ', '.join})

    dgamim_all = df2['kinuy_mishari'].to_list()
    dgamim = list(set(dgamim_all))
    print(dgamim)
    with open(make, 'wb') as pickle_file:
        pickle.dump(dgamim, pickle_file)
#api_base_url = "https://data.gov.il/api/3/action/datastore_search?resource_id=142afde2-6228-49f9-8a29-9b6c3a0cbe40"
#query_url = f"{api_base_url}&limit=70000&filters=" + '{"shnat_yitzur": ["2010", "2015", "2019", "2023"]}'



while True:
    save = input("save? (y,n)")
    if save == "y":
        with open(make, 'ab') as pickle_file:
            pickle.dump(dgamim, pickle_file)
        break
    elif save == "n":
        break

b=5'''




'''data_cars = obj['result']['records']
dgamim_all = [car_model['tozar'] for car_model in data_cars]
dgamim += dgamim_all
dgamim_sofi = list(set(tozarim))
with open('datagov_makes', 'ab') as pickle_file:
    pickle.dump(tozarim, pickle_file)
b = 5'''

# this get all cars from the datagov database into a dataframe and pickles it
'''datagov_url = f"{url}&limit=100000"
data_page = requests.get(datagov_url)
obj = data_page.json()
text = json.dumps(obj, sort_keys=True, indent=4, )
data_cars = obj['result']['records']
df = pd.DataFrame(data_cars,
                  columns=['tozeret_cd', 'degem_cd', 'tozar', 'kinuy_mishari', 'shnat_yitzur', 'degem_nm',
                           'nefah_manoa', 'delek_cd', 'delek_nm'])'''

'''pickle_file = open('datagov_all', 'ab')
datagov_df = pickle.dump(df, pickle_file)'''


'''def datagov_api_call(make, year=2022, limit=5000, model=''):
    make_eng = 'data_makes_reversed[make].lower()'
    make = f"&q={make}"
    year = f"&q={year}"
    if model != '':
        model = f"&q={model}"
    limit = f"&limit={limit}"
    url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=142afde2-6228-49f9-8a29-9b6c3a0cbe40'
    datagov_url = url + limit + make + model
    return requests.get(datagov_url), make_eng'''


make_args = []
# -----------------------------------------------------------------------------------------------
# This code extracts

# with open('pickle2', 'rb') as pickle_file:
#	df = pickle.load(pickle_file)

# df2 = pd.DataFrame(data_cars, columns=['tozeret_cd', 'degem_cd', 'tozar', 'kinuy_mishari', 'shnat_yitzur', 'degem_nm',
#                                       'nefah_manoa', 'delek_cd', 'delek_nm'])
b = 5


# -----------------------------------------------------------------------------------------------
class Cars:
    def __init__(self, make):
        self.make = make


data_makes = ['סנטרו']

'''for make in data_makes:
    df_last_row = df.tail(1)
    last_index = df_last_row.index[0]
    last = df_last_row.index
    indexes = df.index
    last_index2 = max(indexes)

    data_page, make_eng = datagov_api_call(make)
    obj = data_page.json()
    text = json.dumps(obj, sort_keys=True, indent=4, )
    data_cars = obj['result']['records']
    df2 = pd.DataFrame(data_cars,
                       columns=['tozeret_cd', 'degem_cd', 'tozar', 'kinuy_mishari', 'shnat_yitzur', 'degem_nm',
                                'nefah_manoa', 'delek_cd', 'delek_nm'])
    df = pd.concat([df, df2])'''

# This segment extracts the arguments for the method that is used.


# format_function = f"{make_eng}_format"


# format_function = f"{make_eng}_format"

# car = data_cars[0]
# models = [car_model['kinuy_mishari'] for car_model in data_cars]

'''
df.reset_index(inplace=True)
df.rename(columns={'kinuy_mishari': 'model_name'}, inplace=True)
df['model_name'] = df['model_name'].apply(lambda car_model: car_model.lower())
df['corrected_model_name'] = df.apply(lambda car_model: standardize_model_name(args_string), axis=1)'''

# df = pd.DataFrame.from_records(data_car_list, columns=['tozeret_cd', 'degem_cd', 'tozar', 'kinuy_mishari', 'shnat_yitzur'])
#df = df.sort_values(by='degem_nm')

'''try:
    standardize_model_name = getattr(mf, format_function)
except:
    print('no method available')
sig = inspect.signature(standardize_model_name)
args = list(sig.parameters.keys())
args_for_lambda = [f"car_model.{car_model}" for car_model in args]
args_string = ', '.join(args_for_lambda)'''

# This is a variable that imports the correct method for the manufacturer.


'''sig = inspect.signature(standardize_model_name)
args = list(sig.parameters.keys())
args_for_lambda = [f"car_model.{car_model}" for car_model in args]
args_string = ', '.join(args_for_lambda)
'''
# , params=parameters


'''models = set(models)
data_car_list = []

data_car_list2 = []
makes = []'''

'''for car_model in data_cars:
    #data_car_list2.append([{'tozeret_cd': car_model['tozeret_cd']}, {'degem_cd': car_model['degem_cd']}, {'tozar': car_model['tozar']}, {'kinuy_mishari': car_model['kinuy_mishari']}, {'shnat_yitzur': car_model['shnat_yitzur']}])
    data_car_list.append([car_model['tozeret_cd'], car_model['degem_cd'], car_model['tozar'], car_model['kinuy_mishari'], car_model['shnat_yitzur']])'''

'''df_grouped = df.groupby(['degem_nm'])[['model_name', 'delek_cd']].first()

df_grouped = df.groupby(['kinuy_mishari', 'degem_nm'])
def standardize_name(group):
    return group['model_name'].str.split(' ').str[0]


moo = df_grouped.apply(standardize_name)
df['standardized_name'] = df_grouped.apply(standardize_name).transform('first')

df['delek_cd'] = df['delek_cd'].astype(np.int64)'''


'''# create webdriver object
driver = webdriver.Firefox()

# enter keyword to search
keyword = "geeksforgeeks"

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element_by_xpath("//form[input/@name ='search']")'''

b = 5
