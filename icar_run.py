from os.path import exists

import pandas as pd
import numpy as np
from icar_extract import icar_version_extract
from icar_format import format_icar

a = []
fields = ["make",
          "model",
          "ramat_gimur",
          "year",
          "doors",
          "sitting",
          "ignition",
          "gearbox",
          "gear",
          "engine",
          "piston",
          "capacity",
          "power",
          "loops",
          "moment",
          "loopmoment",
          "acceleration",
          "speed",
          "urban_consumption",
          "intercity_consumption",
          "consumption",
          "electricity_use",
          "battery_capacity",
          "electric_range",
          "home_charging_time",
          "fast_charging_time",
          "brake",
          "airbag",
          "stability",
          "cenairbag",
          "length",
          "width",
          "height",
          "wheel",
          "cargo",
          "chaircargo",
          "selfweight",
          "totalweight",
          "loading",
          "towing_without_brakes",
          "towing_with_brakes",
          "tire",
          "fuel", ]

icar_names = ['make', 'model', 'trim', 'year', 'doors', 'sitting', 'ignition', 'gearbox', 'gear', 'engine', 'piston',
              'capacity', 'power', 'loops', 'moment', 'loopmoment', 'acceleration', 'speed', 'urban_consumption',
              'intercity_consumption', 'consumption', 'electricity_use', 'battery_capacity', 'electric_range',
              'home_charging_time', 'fast_charging_time', 'brake', 'airbag', 'stability', 'cenairbag', 'length',
              'width', 'height', 'wheel', 'cargo', 'chaircargo', 'selfweight', 'totalweight', 'loading',
              'towing_without_brakes', 'towing_with_brakes', 'tire', 'fuel', 'hanaa_nm', 'automatic_ind', 'sitting', 'engine_cd']
icar_df = pd.DataFrame(columns=icar_names)

def isnum(num):
	if num.isnumeric():
		return int(num)
	try:
		num = float(num)
	except ValueError:
		if num == '--':
			num = np.nan
	return num


make = 'אודי'
heb_make = "טסלה"
file_name = f"{make}.csv"
text_file = f"{make}.txt"
# check if file exists to avoid overwrite
if exists(file_name):
	print(f"{file_name} exists")
	file_name = f"{make}2.csv"
	if exists(file_name):
		file_name = f"{make}3.csv"
		if exists(file_name):
			exit()

data_test_fields = ["tozar", "kinuy_mishari", "ramat_gimur", "shnat_yitzur", "mispar_dlatot", "mispar_moshavim",
                    "hanaa_cd",
                    "automatic_ind", "nefah_manoa", "kvuzat_agra_cd", "merkav", "delek_cd", "koah_sus",
                    "mispar_kariot_avir",
                    "hayshaney_lahatz_avir_batzmigim_ind", "hayshaney_hagorot_ind", "zihuy_holchey_regel_ind",
                    "zihuy_rechev_do_galgali",
                    "bakarat_shyut_adaptivit_ind", "bakarat_stiya_activ_s", "kosher_grira_bli_blamim",
                    "kosher_grira_im_blamim",
                    "halon_bagg_ind", "galgaley_sagsoget_kala_ind"]
icar_test_fields = ["make", "model", "ramat_gimur", "fieldyear", "fielddoors", "fieldsitting", "fieldignition",
                    "fieldgearbox",
                    "fieldcapacity", "fieldgroupy", "fieldchassis", "fieldengine", "fieldpower", "fieldairbag",
                    "fieldpressure_sensor",
                    "fieldbelt_warning", "fieldpedestrian_identification", "fieldtwo_wheeler_identification",
                    "fieldadaptive_cruise_control", "fieldlane_assist", "fieldtowing_without_brakes",
                    "fieldtowing_with_brakes",
                    "fieldsunroof", "fieldhook"]
test_fields = dict(zip(icar_test_fields, data_test_fields))

field_name_list = ["make", "model", "ramat_gimur", "fieldyear", "fielddoors", "fieldsitting", "fieldprice",
                   "fieldgroupy",
                   "fieldcontinous_value", "fieldguarantee", "fieldchassis", "fieldlaunch", "fieldignition",
                   "fieldgearbox", "fieldgear", "fieldengine",
                   "fieldpiston", "fieldcapacity", "fieldpower", "fieldloops", "fieldmoment", "fieldloopmoment",
                   "fieldacceleration",
                   "fieldspeed", "fieldurban_consumption", "fieldintercity_consumption", "fieldconsumption",
                   "fieldelectricity_use",
                   "fieldbattery_capacity", "fieldelectric_range", "fieldhome_charging_time", "fieldfast_charging_time",
                   "fieldpollution",
                   "fieldbreaking", "fieldbrake", "fieldairbag", "fieldstability", "fieldcenairbag", "fieldizofix",
                   "fieldpressure_sensor",
                   "fieldbelt_warning", "fieldautonomous_braking", "fieldpedestrian_identification",
                   "fieldtwo_wheeler_identification",
                   "fieldadaptive_cruise_control", "fieldlane_assist", "fieldblind_spot", "fieldrear_traffic",
                   "fieldrear_traffic_braking",
                   "fieldalert_fatigue", "fieldhigh_beam_assist", "fieldtraffic_sign_recognition",
                   "fieldcrossing_warning_open_door",
                   "fieldchild_rear_seat", "fieldadditional_safety_equipment", "fieldlength", "fieldwidth",
                   "fieldheight", "fieldwheel",
                   "fieldcargo", "fieldchaircargo", "fieldselfweight", "fieldtowing_without_brakes",
                   "fieldtowing_with_brakes", "fieldtire",
                   "fieldfuel", "fieldaudio", "fieldbluetooth", "fielddisc_changer", "fieldtouch_screen",
                   "fieldscreen_size", "fieldgps",
                   "fieldaudio_connections", "fieldconnectivity", "fieldwireless_charging", "fieldseat_screens",
                   "fieldwindows",
                   "fieldairconditioning", "fieldsunroof", "fieldhook", "fieldrowing", "fieldupholstery",
                   "fieldautochair", "fieldhotchair",
                   "fieldmassage_seats", "fieldlight", "fieldfog", "fieldrain", "fielddark", "fieldparking_sensors",
                   "fieldparking_camers",
                   "fieldautomatic_parking", "fieldcomputer", "fielddigital_cluster", "fieldhead_up_display",
                   "fieldwithout_key",
                   "fieldfolding_mirrors", "fieldinside_mirror", "fieldleather", "fieldheated_steering_wheel",
                   "fieldpaddle_shifters",
                   "fielddriving_mode", "fieldstop_start", "fieldelectric_handbrake", "fieldambient_light",
                   "fieldhill_assist",
                   "fieldsuspension_dampers", "fieldelectric_tailgate", "fieldmore_equ", "fieldprice_equ"]
icar_to_df = []

# open text file with urls and extract data from each
with open(text_file, 'r', encoding='utf-8') as icar_file:
	urls_raw = icar_file.readlines()
urls = [x.strip('\n') for x in urls_raw]
for i in range(len(urls)):
    str_values = icar_version_extract(urls[i])
    values = [isnum(x) for x in str_values]
    icar_df.loc[len(icar_df.index)] = values
icar_df.to_csv(f"make".csv)
field_value_list = []
#car = raw_car.strip('\n')

#icar_values = icar_version_extract(car)


	# add extracted fields_dict to a list and make it into a row in the DataFrame

# write DataFrame to csv
