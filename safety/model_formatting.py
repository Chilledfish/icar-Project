


def audi_format(model_name, delek_cd):
	if 'gt' in model_name:
		return 'e-tron gt'
	model_name_split = model_name.split(' ')
	delek_cd = int(delek_cd)
	if delek_cd > 3:
		if model_name_split[0] == 'e-tron':
			return model_name
		elif model_name_split[0][0] == 'e':
			return 'e-tron'
		return f"{model_name_split[0]} e-tron"
	return model_name_split[0]

def mazda_format(model_name):
	if 'mazda' in model_name:
		return model_name.replace('mazda', '')
	return model_name

