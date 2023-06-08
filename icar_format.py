def str_to_int(x):
	try:
		return int(x)
	except ValueError:
		try:
			return float(x)
		except ValueError:
			return x

def find_sitting(sitting):
    if isinstance(sitting, str):
        return eval(sitting)
    return sitting

def find_engine(engine, engine_type_dict):
    engine = engine.replace("-", " ")
    engine = engine.replace("(", "").replace(")", "")
    engine_types = engine.split(" ")
    engine_numbers = [engine_type_dict.get(type) if type in engine_type_dict else 0 for type in engine_types]
    return sum(engine_numbers)


def find_ignition(ignition):
    if '4X4' in ignition:
        return '4X4'
    return '2X4'

def find_gear(gearbox):
    if 'ידני' in gearbox:
        return 0
    else:
        return 1

def format_icar(format_list):
    engine_type_dict = {'היברידי': 6, 'בנזין': 1, 'דיזל': 2, 'חשמלי': 4}
    sitting, ignition, gearbox, engine = format_list


    mispar_moshavim = find_sitting(sitting)
    # ---------------------------------------------------------------------------
    hanaa_nm = find_ignition(ignition)
    # ---------------------------------------------------------------------------
    automatic_ind = find_gear(gearbox)
    # Get engine type for each car, by matching engine names, to engine codes in datagov database
    delek_cd = find_engine(engine, engine_type_dict)
    # ---------------------------------------------------------------------------
    formatted_values = [hanaa_nm, automatic_ind, mispar_moshavim, delek_cd]

    '''merge_dict = {
        'hanaa_nm': hanaa_nm,
        'automatic_ind': int(automatic_ind),
        'mispar_moshavim': int(sitting),
        'delek_cd': int(engine_cd),
    }'''
    # ---------------------------------------------------------------------------


    return formatted_values