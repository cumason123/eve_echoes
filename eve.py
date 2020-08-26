import math

# Best market values found
material_best_value = {
	'tritanium': 3,
	'pyerite': 18,
	'mexallon': 33,
	'isogen': 125,
	'nocxium': 835,
	'zydrine': 550
}

# Number of materials after processing
medium_pulse_mk5 = {
	'tritanium': 3320,
	'pyerite': 804,
	'mexallon': 274,
	'isogen': 48,
	'nocxium': 13,
	'zydrine': 4,
	'cargo': 25
}

# Number of materials after processing (upgrade reprocessing for more)
small_pulse_mk5 = {
	'tritanium': 873,
	'pyerite': 211,
	'mexallon': 72,
	'isogen': 12,
	'nocxium': 3,
	'cargo': 5
}

# Where to find best prices
regions = {
	'tritanium': 'asghed',
	'pyerite': 'alikara vi',
	'nocxium': 'tash',
	'isogen': 'tash',
	'mexallon': 'tash'
}

# User's tax rate
tax = 0.151966399389
portion = lambda key, processed: material_best_value[key] * processed[key]


def calculate_net_profit(processed, name, cost):	
	gross = sum(
		[portion(key, processed) for key in material_best_value if key in processed if key != 'cargo']
		)
	income = gross - cost
	net = income * (1-tax)
	print(f"You will earn {int(net)} per {name} sold")
	return net, gross


def print_net(processed, name, cost=10000, cargo_size=3000):
	net, gross = calculate_net_profit(processed, name, cost)

	quantity_per_million_income = 1000000 / net
	num_trips = math.ceil((processed['cargo'] * quantity_per_million_income) / cargo_size)
	print(
		f"Need to sell {quantity_per_million_income} to make 1M-isk. "
		f"This will require {num_trips} trips. "
	)

	max_cargo_items = cargo_size / processed['cargo']
	print(
		f"Full cargo trip will earn {max_cargo_items * net}"
	)
	for key in processed:
		if key == 'cargo':
			continue
		material_portion = portion(key, processed)
		fraction = int((material_portion / gross) * 1000) / 10
		print(f"{key}: {fraction}%")
	print()

print_net(medium_pulse_mk5, 'medium pulse laser')
print_net(medium_pulse_mk5, 'medium pulse laser from jita', cost=34016)
print_net(small_pulse_mk5, 'small pulse laser')
