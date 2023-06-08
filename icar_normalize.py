import re


def normalize_audi_model(model_name):
	"""
	Normalizes the name of an Audi car model.

	Parameters:
	model_name (str): The name of the Audi car model to normalize.

	Returns:
	str: The normalized name of the Audi car model.
	"""
	model_name = model_name.upper()
	model = model_name
	if model == 'Q3 SB 45E':
		b=5


	'''
	In audi_patterns:
	r'(?<=\s)[A-Z]\d' matchs a single letter followed by a single digit, as in A6.	
	r'(?<=[A-Z])[A-Z]\d' looks for a single letter and a single digit, following a letter, so RS6, will match S6.
	r'^[A-Z]\d' matches a capital letter and a digit at the start of the string
	'''
	audi_patterns = ['TTS', 'TT', r'(?<=[A-Z])[A-Z]\d', r'(?<=\s)[A-Z]\d', r'^[A-Z]\d']
	etron_patterns = ['E-TRON', 'ETRO', ' E', 'TRO', 'ETRON']
	sportback_patterns = ['SB', 'SP', 'ספורטבק']

	# Check if the input model name should include 'SPORTBACK'
	sportback = any(re.search(pattern, model_name) for pattern in sportback_patterns)

	# Check if the input model name should include 'E-TRON'
	etron = any(re.search(pattern, model_name) for pattern in etron_patterns)



	if re.search('GT', model_name):
		return 'E-TRON GT'
	if 'AUDI' in model_name:
		model_name = model_name.replace('AUDI ', '')
	for pattern in audi_patterns:
		# Compile regex patterns
		pattern = re.compile(pattern)
		match = pattern.search(model_name)
		if match:
			model_name = match.group()
			# Checking if model is one of the 2 Qs (Q4, Q8) that have an etron version
			# Check for Q4 or Q8, which have an E-TRON version
			if etron and model_name[0] == 'Q' and int(model_name[1:]) in {4, 8}:
				model_name += ' E-TRON'
				etron = False  # Reset etron flag
			break

	# If 'etron' is matched alone, set the model name to 'E-TRON'
	if etron:
		model_name = 'E-TRON'

		# If 'SPORTBACK' should be included, add it to the final model name
	if sportback:
		model_name += ' SPORTBACK'
	if model_name == '45 SPORTBACK':
		b=5

	return model_name
