# from icar_format import format_icar
import numpy as np
import pandas as pd

import icar_variables
from icar_variables import *

makes = ["אודי", "אופל", "איווקו", "אינפיניטי", "איסוזו", "אלפא_רומיאו", "אסטון_מרטין", "ב.מ.וו",
         "ביואיק",
         "בנטלי",
         "ג'ילי", "ג'נסיס", "גיפ", "גרייט וול", "דאציה", "דודג", "דייהטסו", "הונדה", "וולוו",
         "טויוטה",
         "טסלה", "יגואר",
         "DS", "יונדאי", "לינקולן", "לנדרובר", "לנציה", "לקסוס", "מרצדס", "מאזדה", "מאן", "מזראטי",
         "מיני",
         "מיצובישי",
         "מקסוס", "מרצדס", "ניסאן", "סאאב", "סאיק-MG", "סאנגיונג", "סובארו", "סוזוקי", "סיאט",
         "סיטרואן",
         "סמארט", "סקודה",
         "סקייוול", "פולקסווגן", "פורד", "פורשה", "פיאט", "פיגו", "פרארי", "קדילאק", "קופרה", "קיה",
         "קרייזלר", "ראם",
         "רנו", "שברולט"]


def merger(make, left, right):
	pass


csvfile, formatted_file, tozar, outfile, make_e = icar_variables.file_maker(make)

# icar_df = pd.read_csv('icar_new.csv', encoding='utf-8')
datagov_df = pd.read_csv("datagov_for_merge.csv", encoding='utf-8')
# datagov_df.loc[datagov_df["nefah_manoa"] == 0] = np.NaN

datagov_df["nefah_manoa"].mask(datagov_df["nefah_manoa"] == 0, np.NaN, inplace=True)

# icar_formatted = f"f_{car_translation[make]}.csv"

# tesla = icar_df.loc[icar_df['make'] == "טסלה"]

# icar_df['fieldsitting'] = icar_df['fieldsitting'].astype('int32')

shape = datagov_df.shape[0]

# icar_make = icar[]


data_merge_fields = ["tozar", "shnat_yitzur", "mispar_dlatot", "mispar_moshavim", "automatic_ind", "nefah_manoa",
                     "koah_sus", "n_model", "delek_cd", "hanaa_nm"]
icar_merge_fields = ["make", "year", "doors", "sitting", "automatic_ind", "capacity", "power", "n_model", "engine_cd",
                     "hanaa_nm"]

headers = ['tozeret_cd', 'tozar', 'kinuy_mishari', 'ramat_gimur_x', 'shnat_yitzur', 'degem_cd', 'kvuzat_agra_cd',
           'nefah_manoa', 'mishkal_kolel', 'gova', 'hanaa_cd', 'hanaa_nm', 'automatic_ind', 'mispar_halonot_hashmal',
           'merkav', 'delek_cd', 'delek_nm', 'mispar_dlatot', 'koah_sus', 'mispar_moshavim', 'technologiat_hanaa_cd',
           'technologiat_hanaa_nm', 'n_model', 'Unnamed: 0', 'make', 'model', 'ramat_gimur_y', 'year', 'doors',
           'sitting', 'ignition', 'gearbox', 'gear', 'engine', 'piston', 'capacity', 'power', 'loops', 'moment',
           'loopmoment', 'acceleration', 'speed', 'urban_consumption', 'intercity_consumption', 'consumption',
           'electricity_use', 'battery_capacity', 'electric_range', 'home_charging_time', 'fast_charging_time', 'brake',
           'airbag', 'stability', 'cenairbag', 'length', 'width', 'height', 'wheel', 'cargo', 'chaircargo',
           'selfweight', 'totalweight', 'loading', 'towing_without_brakes', 'towing_with_brakes', 'tire', 'fuel',
           'sitting.1', 'engine_cd']
output_df = pd.DataFrame(columns=headers)

#headers = list(merged_df.columns)
#output_df = pd.DataFrame(columns=headers)

for make in makes:
	icar_df = pd.read_csv(f"{make}.csv", encoding='utf-8')
	icar_df["sitting"].mask(icar_df["sitting"] == ('2+2' or '4'), '5', inplace=True)
	# icar_df["sitting"].mask(icar_df["sitting"] == '4', '5', inplace=True)
	icar_df['sitting'] = icar_df['sitting'].apply(lambda x: int(x))
	# icar_df["sitting"].mask(icar_df["sitting"] == '5', 5, inplace=True)
	# icar_moo = icar_df.loc[icar_df["sitting"] == 4]
	icar_df.astype({'sitting': 'int64'})
	merged_df = pd.merge(datagov_df, icar_df, left_on=data_merge_fields, right_on=icar_merge_fields, how='inner')

headers = list(merged_df.columns)

output_df.loc[len(output_df.index)] = merged_df
# extra fields_dict:

outcsv = 'testout.csv'

icar_with_trim = ["make", "n_model", "year", "capacity", "ramat_gimur", "doors", "power",
                  "delek_cd", "automatic_ind", "sitting"]
datagov_with_trim = ["make", "n_model", "shnat_yitzur", "nefah_manoa", "ramat_gimur", "mispar_dlatot", "koah_sus",
                     "delek_cd", "automatic_ind", "mispar_moshavim"]

icar_without_trim = ["make", "n_model", "fieldyear", "fieldcapacity", "fielddoors", "fieldpower", "delek_cd",
                     "automatic_ind", "fieldsitting", "fieldpressure_sensor"]

datagov_without_trim = ["make", "n_model", "shnat_yitzur", "nefah_manoa", "mispar_dlatot", "koah_sus", "delek_cd",
                        "automatic_ind", "mispar_moshavim", "hayshaney_lahatz_avir_batzmigim_ind"]

new_df = pd.DataFrame(columns=headers)
merged_df.to_csv('merged_tesla.csv', index='false')

# , "model_nm"
# merged_df2 = merged_df.loc[2:]

data_test_fields = ["tozar", "shnat_yitzur", "mispar_dlatot", "mispar_moshavim", "automatic_ind", "nefah_manoa",
                    "kvuzat_agra_cd", "koah_sus",
                    "hayshaney_lahatz_avir_batzmigim_ind", "hayshaney_hagorot_ind", "zihuy_holchey_regel_ind",
                    "zihuy_rechev_do_galgali",
                    "bakarat_shyut_adaptivit_ind", "kosher_grira_bli_blamim", "kosher_grira_im_blamim",
                    "halon_bagg_ind",
                    "galgaley_sagsoget_kala_ind", "delek_cd"]
icar_test_fields = ["make", "fieldyear", "fielddoors", "fieldsitting", "fieldgearbox", "fieldcapacity", "fieldgroupy",
                    "fieldpower",
                    "fieldpressure_sensor", "fieldbelt_warning", "fieldpedestrian_identification",
                    "fieldtwo_wheeler_identification",
                    "fieldadaptive_cruise_control", "fieldairbag", "fieldtowing_without_brakes",
                    "fieldtowing_with_brakes", "fieldsunroof", "fieldhook",
                    "fieldengine", "fieldlane_assist"]

shorter_merege_fields_data = ["tozar", "n_model", "shnat_yitzur", "nefah_manoa", "mispar_dlatot", "koah_sus",
                              "automatic_ind", "engine_cd"]
shorter_merege_fields_icar = ["make", "n_model", "year", "capacity", "doors", "power", "automatic_ind", "engine_cd"]

# new_df = datagov_suzuki.merge(icar, left_on=["shnat_yitzur", "mispar_moshavim", "mispar_dlatot"],
# right_on=["shnat_yitzur", "mispar_moshavim", "mispar_dlatot"])
# new_df.to_csv(outcsv, encoding='utf-8')

# new_df = datagov.merge(icar, left_on=data_test_fields, right_on=icar_test_fields)
# new_df.to_csv('testout2.csv', encoding='utf-8')

# testdf = datagov_df.merge(icar_df, left_on=["shnat_yitzur", "nefah_manoa"], right_on=["fieldyear", "fieldcapacity"])

new_df = datagov_df.merge(icar_df, left_on=shorter_merege_fields_data, right_on=shorter_merege_fields_icar)
new_df.to_csv('testout5.csv', encoding='utf-8')

new_copied_df = new_df.copy()

merged_fields = ["tozeret_cd", "degem_cd", "shnat_yitzur", "tozar", "kinuy_mishari", "ramat_gimur", "make", "model",
                 "fieldchassis", "fieldignition", "fieldgearbox", "fieldgear", "fieldengine", "fieldpiston",
                 "fieldloops",
                 "fieldmoment",
                 "fieldloopmoment", "fieldacceleration", "fieldspeed", "fieldurban_consumption",
                 "fieldintercity_consumption",
                 "fieldconsumption",
                 "fieldelectricity_use", "fieldbattery_capacity", "fieldelectric_range", "fieldhome_charging_time",
                 "fieldfast_charging_time", "fieldairbag",
                 "fieldstability", "fieldcenairbag", "fieldizofix", "fieldpressure_sensor", "fieldbelt_warning",
                 "fieldautonomous_braking",
                 "fieldpedestrian_identification", "fieldtwo_wheeler_identification", "fieldadaptive_cruise_control",
                 "fieldlane_assist",
                 "fieldblind_spot",
                 "fieldrear_traffic", "fieldrear_traffic_braking", "fieldalert_fatigue", "fieldhigh_beam_assist",
                 "fieldtraffic_sign_recognition",
                 "fieldcrossing_warning_open_door", "fieldchild_rear_seat", "fieldadditional_safety_equipment",
                 "fieldlength", "fieldwidth",
                 "fieldheight",
                 "fieldwheel", "fieldcargo", "fieldchaircargo", "fieldselfweight", "fieldtire", "fieldfuel",
                 "fieldaudio", "fieldbluetooth",
                 "fielddisc_changer", "fieldtouch_screen", "fieldscreen_size", "fieldgps", "fieldaudio_connections",
                 "fieldconnectivity",
                 "fieldwireless_charging", "fieldseat_screens", "fieldwindows", "fieldairconditioning", "fieldsunroof",
                 "fieldhook",
                 "fieldrowing",
                 "fieldupholstery", "fieldautochair", "fieldhotchair", "fieldmassage_seats", "fieldlight", "fieldfog",
                 "fieldrain",
                 "fielddark",
                 "fieldparking_sensors", "fieldparking_camers", "fieldautomatic_parking", "fieldcomputer",
                 "fielddigital_cluster",
                 "fieldhead_up_display",
                 "fieldwithout_key", "fieldfolding_mirrors", "fieldinside_mirror", "fieldleather",
                 "fieldheated_steering_wheel",
                 "fieldpaddle_shifters",
                 "fielddriving_mode", "fieldstop_start", "fieldelectric_handbrake", "fieldambient_light",
                 "fieldhill_assist",
                 "fieldsuspension_dampers",
                 "fieldelectric_tailgate", "fieldmore_equ"]
new_filtered_df = new_copied_df.filter(merged_fields)
new_filtered_df.to_csv(outfile, encoding='utf-8')

b = 5

b = 5
