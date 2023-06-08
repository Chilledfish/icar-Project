icar_compare_list = ["אודי", "אופל", "איווקו", "אינפיניטי", "איסוזו", "אלפא_רומיאו", "אסטון_מרטין", "ב.מ.וו", "ביואיק",
                     "בנטלי",
                     "ג'ילי", "ג'נסיס", "גיפ", "גרייט וול", "דאציה", "דודג", "דייהטסו", "הונדה", "וולוו", "טויוטה",
                     "טסלה", "יגואר",
                     "DS", "יונדאי", "לינקולן", "לנדרובר", "לנציה", "לקסוס", "מרצדס", "מאזדה", "מאן", "מזראטי", "מיני",
                     "מיצובישי",
                     "מקסוס", "מרצדס", "ניסאן", "סאאב", "סאיק-MG", "סאנגיונג", "סובארו", "סוזוקי", "סיאט", "סיטרואן",
                     "סמארט", "סקודה",
                     "סקייוול", "פולקסווגן", "פורד", "פורשה", "פיאט", "פיגו", "פרארי", "קדילאק", "קופרה", "קיה",
                     "קרייזלר", "ראם",
                     "רנו", "שברולט"]
datagov_compare_list = ["אאודי", "אופל", "איווקו", "ניסאן", "איסוזו", "אלפא רומיאו", "אסטון מרטין", "ב מ וו", "ביואיק",
                        "בנטלי", "גילי",
                        "יונדאי", "ג'יפ", "גרייט וול", "דאציה", "דודג'", "דייהטסו", "הונדה", "וולוו", "טויוטה", "טסלה",
                        "יגואר",
                        "די.אס", "יונדאי", "לינקולן", "לנדרובר", "לנצ'יה", "לקסוס", "מרצדס", "מזדה", "מאן", "מזארטי",
                        "ב מ וו",
                        "מיצובישי", "מקסוס", "מרצדס", "ניסאן", "סאאב", "מ.ג", "סאנגיונג", "סובארו", "סוזוקי", "סיאט",
                        "סיטרואן", "סמארט",
                        "סקודה", "סקיוול", "פולקסווגן", "פורד", "פורשה", "פיאט", "פיג'ו", "פרארי", "קאדילאק", "סיאט",
                        "קיה", "קרייזלר",
                        "דודג'", "רנו", "שברולט"]

make = "ב.מ.וו"

# lists
# -------------------------------------------
makes = ["פיג'ו", "סובארו", "מאזדה", "אאודי", "אלפא_רומיאו", "הונדה", "פיאט", "מרצדס", "לקסוס", "ניסאן", "במוו",
         "מיצובישי", "לנדרובר", "פולקסווגן", "סיאט", "סוזוקי", "יגואר"]
fields = ["make", "model", "ramat_gimur", "fieldyear", "fielddoors", "fieldsitting", "fieldgroupy", "fieldignition",
          "fieldgearbox",
          "fieldgear", "fieldengine", "fieldpiston", "fieldcapacity", "fieldpower", "fieldloops", "fieldloopmoment",
          "fieldacceleration",
          "fieldspeed", "fieldurban_consumption", "fieldintercity_consumption", "fieldconsumption",
          "fieldelecicity_use",
          "fieldbattery_capacity", "fieldelecic_range", "fieldhome_charging_time", "fieldfast_charging_time",
          "fieldpollution",
          "fieldbreaking", "fieldbrake", "fieldairbag", "fieldstability", "fieldcenairbag", "fieldizofix",
          "fieldpressure_sensor",
          "fieldbelt_warning", "fieldautonomous_braking", "fieldpedesian_identification",
          "fieldtwo_wheeler_identification",
          "fieldadaptive_cruise_conol", "fieldlane_assist", "fieldblind_spot", "fieldrear_affic",
          "fieldrear_affic_braking",
          "fieldalert_fatigue", "fieldhigh_beam_assist", "fieldaffic_sign_recognition",
          "fieldcrossing_warning_open_door",
          "fieldchild_rear_seat", "fieldadditional_safety_equipment", "fieldlength", "fieldwidth", "fieldheight",
          "fieldwheel",
          "fieldcargo", "fieldchaircargo", "fieldselfweight", "fieldtowing_without_brakes", "fieldtowing_with_brakes",
          "fieldtire",
          "fieldfuel", "fieldaudio", "fieldbluetooth", "fielddisc_changer", "fieldtouch_screen", "fieldscreen_size",
          "fieldgps",
          "fieldaudio_connections", "fieldconnectivity", "fieldwireless_charging", "fieldseat_screens", "fieldwindows",
          "fieldairconditioning", "fieldsunroof", "fieldhook", "fieldrowing", "fieldupholstery", "fieldautochair",
          "fieldhotchair",
          "fieldmassage_seats", "fieldlight", "fieldfog", "fieldrain", "fielddark", "fieldparking_sensors",
          "fieldparking_camers",
          "fieldautomatic_parking", "fieldcomputer", "fielddigital_cluster", "fieldhead_up_display", "fieldwithout_key",
          "fieldfolding_mirrors", "fieldinside_mirror", "fieldleather", "fieldheated_steering_wheel",
          "fieldpaddle_shifters",
          "fielddriving_mode", "fieldstop_start", "fieldelecic_handbrake", "fieldambient_light", "fieldhill_assist",
          "fieldsuspension_dampers", "fieldelecic_tailgate", "fieldmore_equ", "fieldprice_equ"]
data_test_fields = ["shnat_yitzur", "mispar_dlatot", "mispar_moshavim", "nefah_manoa", "kvuzat_agra_cd", "koah_sus",
                    "hayshaney_lahatz_avir_batzmigim_ind", "hayshaney_hagorot_ind", "zihuy_holchey_regel_ind",
                    "zihuy_rechev_do_galgali",
                    "bakarat_shyut_adaptivit_ind", "kosher_grira_bli_blamim", "kosher_grira_im_blamim",
                    "delek_cd", "automatic_ind"]
icar_test_fields = ["fieldyear", "fielddoors", "fieldsitting", "fieldcapacity", "fieldgroupy", "fieldpower",
                    "fieldpressure_sensor", "fieldbelt_warning", "fieldpedestrian_identification",
                    "fieldtwo_wheeler_identification",
                    "fieldadaptive_cruise_control", "fieldtowing_without_brakes", "fieldtowing_with_brakes", "delek_cd",
                    "automatic_ind"]
final_fields = ["fielddoors",
                "fieldsitting",
                "fieldchassis",
                "fieldlaunch",
                "fieldignition",
                "fieldgearbox",
                "fieldgear",
                "fieldengine",
                "fieldpiston",
                "fieldloops",
                "fieldmoment",
                "fieldloopmoment",
                "fieldacceleration",
                "fieldspeed",
                "fieldurban_consumption",
                "fieldintercity_consumption",
                "fieldconsumption",
                "fieldelectricity_use",
                "fieldbattery_capacity",
                "fieldelectric_range",
                "fieldhome_charging_time",
                "fieldfast_charging_time",
                "fieldbrake",
                "fieldcenairbag",
                "fieldizofix",
                "fieldautonomous_braking",
                "fieldrear_traffic",
                "fieldrear_traffic_braking",
                "fieldalert_fatigue",
                "fieldcrossing_warning_open_door",
                "fieldchild_rear_seat",
                "fieldadditional_safety_equipment",
                "fieldlength",
                "fieldwidth",
                "fieldheight",
                "fieldwheel",
                "fieldcargo",
                "fieldchaircargo",
                "fieldselfweight",
                "fieldfuel",
                "fieldaudio",
                "fieldbluetooth",
                "fielddisc_changer",
                "fieldtouch_screen",
                "fieldscreen_size",
                "fieldgps",
                "fieldaudio_connections",
                "fieldconnectivity",
                "fieldwireless_charging",
                "fieldseat_screens",
                "fieldwindows",
                "fieldairconditioning",
                "fieldsunroof",
                "fieldrowing",
                "fieldupholstery",
                "fieldautochair",
                "fieldhotchair",
                "fieldmassage_seats",
                "fieldlight",
                "fieldfog",
                "fieldrain",
                "fielddark",
                "fieldparking_sensors",
                "fieldparking_camers",
                "fieldautomatic_parking",
                "fieldcomputer",
                "fielddigital_cluster",
                "fieldhead_up_display",
                "fieldwithout_key",
                "fieldfolding_mirrors",
                "fieldinside_mirror",
                "fieldleather",
                "fieldheated_steering_wheel",
                "fieldpaddle_shifters",
                "fielddriving_mode",
                "fieldstop_start",
                "fieldelectric_handbrake",
                "fieldambient_light",
                "fieldhill_assist",
                "fieldsuspension_dampers",
                "fieldelectric_tailgate",
                "fieldmore_equ",
                "fieldprice_equ"]
pratim = ['tozar', 'kinuy_mishari', 'shnat_yitzur', 'ramat_gimur', 'tozeret_cd', 'degem_cd', 'nefah_manoa', 'automatic_ind',
          'mispar_dlatot', 'koah_sus', 'delek_nm', 'kvuzat_agra_cd', 'bakarat_shyut_adaptivit_ind', 'zihuy_holchey_regel_ind']

# dictionaries
# -------------------------------------------
make_to_tozar = {"אאודי": "אאודי",
                 "אופל": "אופל",
                 "איווקו": "איווקו",
                 "אינפיניטי": "ניסאן",
                 "איסוזו": "איסוזו",
                 "אלפא רומיאו": "אלפא רומיאו",
                 "אסטון מרטין": "אסטון מרטין",
                 "ב.מ.וו": "ב מ וו",
                 "ביואיק": "ביואיק",
                 "בנטלי": "בנטלי",
                 "ג'ילי": "גילי",
                 "ג'נסיס": "יונדאי",
                 "גיפ": "ג'יפ",
                 "גרייט וול": "גרייט וול",
                 "דאציה": "דאציה",
                 "דודג": "דודג'",
                 "דייהטסו": "דייהטסו",
                 "הונדה": "הונדה",
                 "וולוו": "וולבו",
                 "טויוטה": "טויוטה",
                 "טסלה": "טסלה",
                 "יגואר": "יגואר",
                 "DS": "די אס",
                 "DS": "די.אס",
                 "יונדאי": "יונדאי",
                 "לינקולן": "לינקולן",
                 "לנדרובר": "דייהטסו",
                 "לנציה": "לנצ'יה",
                 "לקסוס": "לקסוס",
                 "מזדה": "מאזדה",
                 "מאן": "מאן",
                 "מזראטי": "מזארטי",
                 "מיני": "ב מ וו",
                 "מיצובישי": "מיצובישי",
                 "מקסוס": "מקסוס",
                 "מרצדס": "מרצדס",
                 "ניסאן": "ניסאן",
                 "סאאב": "סאאב",
                 "סאיק-MG": "מ.ג",
                 "סאנגיונג": "לקסוס",
                 "סובארו": "מ א ן",
                 "סוזוקי": "מ.ג",
                 "סיאט": "סיאט",
                 "סיטרואן": "סיטרואן",
                 "סמארט": "סמארט",
                 "סקודה": "סקודה",
                 "סקייוול": "סקיוול",
                 "פולקסווגן": "פולקסווגן",
                 "פורד": "פורד",
                 "פורשה": "פורשה",
                 "פיאט": "פיאט",
                 "פיגו": "פיג'ו",
                 "פרארי": "פרארי",
                 "קדילאק": "קאדילאק",
                 "קופרה": "סיאט",
                 "קיה": "קיה",
                 "קרייזלר": "קרייזלר",
                 "ראם": "דודג'",
                 "רנו": "רנו",
                 "שברולט": "שברולט"}
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
tozar_to_make = {"אודי": "אאודי",
                 "אופל": "אופל",
                 "איווקו": "איווקו",
                 "ניסאן": "אינפיניטי",
                 "איסוזו": "איסוזו",
                 "אלפא רומיאו": "אלפא רומיאו",
                 "אסטון מרטין": "אסטון מרטין",
                 "ב מ וו": "ב.מ.וו",
                 "ביואיק": "ביואיק",
                 "בנטלי": "בנטלי",
                 "גילי": "ג'ילי",
                 "יונדאי": "ג'נסיס",
                 "ג'יפ": "גיפ",
                 "גרייט וול": "גרייט וול",
                 "דאציה": "דאציה",
                 "דודג'": "דודג",
                 "דייהטסו": "דייהטסו",
                 "הונדה": "הונדה",
                 "וולבו": "וולוו",
                 "טויוטה": "טויוטה",
                 "טסלה": "טסלה",
                 "יגואר": "יגואר",
                 "די אס": "DS",
                 "די.אס": "DS",
                 "יונדאי": "יונדאי",
                 "לינקולן": "לינקולן",
                 "דייהטסו": "לנדרובר",
                 "לנצ'יה": "לנציה",
                 "לקסוס": "לקסוס",
                 "מזדה": "מאזדה",
                 "מאן": "מאן",
                 "מזארטי": "מזראטי",
                 "ב מ וו": "מיני",
                 "מיצובישי": "מיצובישי",
                 "מקסוס": "מקסוס",
                 "מרצדס": "מרצדס",
                 "ניסאן": "ניסאן",
                 "סאאב": "סאאב",
                 "מ.ג": "סאיק-MG",
                 "לקסוס": "סאנגיונג",
                 "מ א ן": "סובארו",
                 "מ.ג": "סוזוקי",
                 "סיאט": "סיאט",
                 "סיטרואן": "סיטרואן",
                 "סמארט": "סמארט",
                 "סקודה": "סקודה",
                 "סקיוול": "סקייוול",
                 "פולקסווגן": "פולקסווגן",
                 "פורד": "פורד",
                 "פורשה": "פורשה",
                 "פיאט": "פיאט",
                 "פיג'ו": "פיגו",
                 "פרארי": "פרארי",
                 "קאדילאק": "קדילאק",
                 "סיאט": "קופרה",
                 "קיה": "קיה",
                 "קרייזלר": "קרייזלר",
                 "דודג'": "ראם",
                 "רנו": "רנו",
                 "שברולט": "שברולט"}
dtypes = {"make": str,
          "model": str,
          "ramat_gimur": str,
          "fieldyear": 'int32',
          "fielddoors": 'int32',
          "fieldsitting": 'int32',
          "fieldgearbox": str,
          "fieldcapacity": 'int32',
          "fieldgroupy": 'int32',
          "fieldgroupy": 'int32',
          "fieldchassis": str,
          "fieldpower": 'int32',
          "fieldpressure_sensor": 'int32',
          "fieldbelt_warning": 'int32',
          "fieldpedestrian_identification": 'int32',
          "fieldtwo_wheeler_identification": 'int32',
          "fieldtowing_without_brakes": 'int32',
          "fieldtowing_with_brakes": 'int32',
          "delek_cd": 'int32',
          "automatic_ind": 'int32',
          "hanaa_nm": str,
          "model_nm": str}

# file maker
# -------------------------------------------

def file_maker(make_nm=make):
    make_e = car_translation[make_nm]
    csvfile = f'{make_e}.csv'
    formatted_file = f"f_{make_e}.csv"
    tozar = make_to_tozar[make_nm]
    outfile = f"{make_e}_out.csv"

    return csvfile, formatted_file, tozar, outfile, make_e
# -------------------------------------------



