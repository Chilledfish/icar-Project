import csv
from distutils.log import error
import pandas as pd
import numpy as np
import re
# from icar_format import format_icar
import icar_variables
from icar_variables import *

make = 'ב.מ.וו'

csvfile, formatted_file, tozar, outfile, make_e = icar_variables.file_maker(make)

icar_csv = f"{make_e}_icar_models.csv"
datagov_csv = f"{make_e}_data_models.csv"

# icar_formatted = f"f_{car_translation[make]}.csv"

datagov_df = pd.read_csv(datagov_csv, encoding='utf-8', engine='python')
#icar_df = pd.read_csv(icar_csv, encoding='utf-8', dtype=dtypes)

#icar_df['fieldsitting'] = icar_df['fieldsitting'].astype('int32')

shape = datagov_df.shape[0]


# icar_make = icar[]


data_merge_fields = ["tozar", "kinuy_mishari", "shnat_yitzur", "mispar_dlatot", "mispar_moshavim", "automatic_ind",
                     "nefah_manoa", "koah_sus",
                     "hayshaney_lahatz_avir_batzmigim_ind", "hayshaney_hagorot_ind", "galgaley_sagsoget_kala_ind"]
#icar_merge_fields = ["make", "model", "fieldyear", "fielddoors", "fieldsitting", "automatic_ind", "fieldcapacity",
#                     "fieldpower",
#                     "fieldpressure_sensor", "fieldbelt_warning", "fieldhook"]

# extra fields_dict:


outcsv = 'testout.csv'
'''
short_merege_fields_data = ["n_model", "shnat_yitzur", "nefah_manoa", "ramat_gimur", "mispar_dlatot", "koah_sus",
                            "delek_cd", "automatic_ind", "mispar_moshavim"]

short_merege_fields_icar = ["n_model", "fieldyear", "fieldcapacity", "ramat_gimur", "fielddoors", "fieldpower",
                            "delek_cd", "automatic_ind", "fieldsitting"]
'''



# , "model_nm"


data_test_fields = ["tozar", "shnat_yitzur", "mispar_dlatot", "mispar_moshavim", "automatic_ind", "nefah_manoa",
                    "kvuzat_agra_cd", "koah_sus",
                    "hayshaney_lahatz_avir_batzmigim_ind", "hayshaney_hagorot_ind", "zihuy_holchey_regel_ind",
                    "zihuy_rechev_do_galgali",
                    "bakarat_shyut_adaptivit_ind", "kosher_grira_bli_blamim", "kosher_grira_im_blamim",
                    "halon_bagg_ind",
                    "galgaley_sagsoget_kala_ind", "delek_cd"]

'''
icar_test_fields = ["make", "fieldyear", "fielddoors", "fieldsitting", "fieldgearbox", "fieldcapacity", "fieldgroupy",
                    "fieldpower",
                    "fieldpressure_sensor", "fieldbelt_warning", "fieldpedestrian_identification",
                    "fieldtwo_wheeler_identification",
                    "fieldadaptive_cruise_control", "fieldairbag", "fieldtowing_without_brakes",
                    "fieldtowing_with_brakes", "fieldsunroof", "fieldhook",
                    "fieldengine", "fieldlane_assist"]
'''
'''
shorter_merege_fields_data = ["shnat_yitzur", "nefah_manoa", "ramat_gimur", "mispar_dlatot", "koah_sus", "delek_cd",
                              "automatic_ind", "galgaley_sagsoget_kala_ind"]

shorter_merege_fields_icar = ["fieldyear", "fieldcapacity", "ramat_gimur", "fielddoors", "fieldpower", "delek_cd",
                              "automatic_ind", "fieldhook"]
'''
# new_df = datagov_suzuki.merge(icar, left_on=["shnat_yitzur", "mispar_moshavim", "mispar_dlatot"],
# right_on=["shnat_yitzur", "mispar_moshavim", "mispar_dlatot"])
# new_df.to_csv(outcsv, encoding='utf-8')

# new_df = datagov.merge(icar, left_on=data_test_fields, right_on=icar_test_fields)
# new_df.to_csv('testout2.csv', encoding='utf-8')

#testdf = datagov_df.merge(icar_df, left_on=["shnat_yitzur", "nefah_manoa"], right_on=["fieldyear", "fieldcapacity"])

new_df = datagov_df.merge(icar_df, left_on=short_merege_fields_data, right_on=short_merege_fields_icar)
new_df.to_csv('testout3.csv', encoding='utf-8')

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
