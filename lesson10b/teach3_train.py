import math
import random

data = [
	[
		[0, 1, 1],
		[1, 0, 1],
		[1, 0, 1],
		[1, 1, 1]
	],
	[
		[0, 1, 1],
		[1, 0, 1],
		[1, 0, 1],
		[1, 1, 1]
	],
	[
		[1, 1, 0],
		[1, 0, 1],
		[1, 0, 1],
		[1, 1, 1]
	],
	[
		[1, 1, 1],
		[1, 0, 1],
		[1, 0, 1],
		[1, 1, 0]
	],
	[
		[1, 1, 1],
		[1, 0, 1],
		[1, 0, 1],
		[0, 1, 1]
	]
]

answers1 = [1, 0]

hidden_layer_weights = [
	[  # 1st hidden unit
		[0.06, 0.17, 0.12],
		[0.08, 0.33, 0.18],
		[0.15, 0.92, 0.12],
		[0.98, 0.11, 0.20]
	],
	[  # 2nd hidden unit
		[0.08, 0.91, 0.12],
		[0.29, 0.18, 0.21],
		[0.35, 0.12, 0.22],
		[0.19, 0.97, 0.03]
	],
	[  # 3rd hidden unit
		[1.00, 0.16, 0.93],
		[0.89, 0.97, 0.11],
		[0.94, 0.12, 0.09],
		[0.04, 0.06, 0.13]
	]
]
thresholds = [0.97,	0.92, 0.94]
thresholds1 = [0.18, 0.92, 0.06]
thresholds2 = [0.99, 0.10, 0.84]
thresholds3 = [1.00, 0.94]

def sum_of_product(data, weights):
	total = 0.0
	for i in range(len(data)):
		for j in range(len(data[0])):
			# print(data[i][j], "*", weights[i][j])
			total += data[i][j] * weights[i][j]
	return total
def sigmoid(x):
	# numerically stable sigmoid
	try:
		return 1.0 / (1.0 + math.exp(-x))
	except OverflowError:
		return 0.0 if x < 0 else 1.0


def SUMXMY2(array1, array2):
	if len(array1) != len(array2):
		raise ValueError("Arrays must have the same length")
	total = 0.0
	for i in range(len(array1)):
		diff = array1[i] - array2[i]
		total += diff * diff
	return total


def forward(sample, params):
	"""Compute two outputs for one sample using packed params."""
	# unpack params
	idx = 0
	hidden_layer_weights_p = []
	for h in range(3):
		unit = []
		for r in range(4):
			row = []
			for c in range(3):
				row.append(params[idx]); idx += 1
			unit.append(row)
		hidden_layer_weights_p.append(unit)

	thresholds_p = [params[idx + i] for i in range(3)]; idx += 3
	thresholds1_p = [params[idx + i] for i in range(3)]; idx += 3
	thresholds2_p = [params[idx + i] for i in range(3)]; idx += 3
	thresholds3_p = [params[idx + i] for i in range(2)]; idx += 2

	# hidden layer
	exps = []
	for h in range(3):
		s = sum_of_product(sample, hidden_layer_weights_p[h])
		exps.append(sigmoid(s - thresholds_p[h]))

	# output layer
	layer2_1_sum = exps[0] * thresholds1_p[0] + exps[1] * thresholds1_p[1] + exps[2] * thresholds1_p[2]
	z1 = sigmoid(layer2_1_sum - thresholds3_p[0])

	layer2_2_sum = exps[0] * thresholds2_p[0] + exps[1] * thresholds2_p[1] + exps[2] * thresholds2_p[2]
	z2 = sigmoid(layer2_2_sum - thresholds3_p[1])

	return [z1, z2]


def pack_initial_params():
	# pack the original variables (lines 39-62) into a flat list
	params = []
	for h in hidden_layer_weights:
		for row in h:
			for v in row:
				params.append(v)
	for v in thresholds:
		params.append(v)
	for v in thresholds1:
		params.append(v)
	for v in thresholds2:
		params.append(v)
	for v in thresholds3:
		params.append(v)
	return params


def total_error(params):
	total = 0.0
	for sample in data:
		out = forward(sample, params)
		total += SUMXMY2(out, answers1) # 誤差Q
	return total


def train(params, iterations=2000, init_step=0.05, decay=0.999):
	"""Simple stochastic hill-climbing with small random perturbations."""
	best = list(params)
	best_err = total_error(best)
	step = init_step
	for it in range(iterations):
		candidate = [best[i] + random.gauss(0, step) for i in range(len(best))]
		err = total_error(candidate)
		if err < best_err:
			best, best_err = candidate, err
		# small probability to accept worse solution (helps escape local minima)
		elif random.random() < 0.001:
			best, best_err = candidate, err
		step *= decay
		# occasional progress print
		if (it + 1) % 500 == 0:
			print(f"iter {it+1}: best_err={best_err:.6f}, step={step:.6f}")
	return best, best_err


if __name__ == '__main__':
	# Prepare initial params and train
	init_params = pack_initial_params()
	print("Initial total error:", total_error(init_params))
	tuned_params, tuned_err = train(init_params, iterations=3000, init_step=0.05, decay=0.9995)
	print("Tuned total error:", tuned_err)

	# unpack tuned params back into the named variables and print/dump them
	idx = 0
	tuned_hidden = []
	for h in range(3):
		unit = []
		for r in range(4):
			row = []
			for c in range(3):
				row.append(tuned_params[idx]); idx += 1
			unit.append(row)
		tuned_hidden.append(unit)

	tuned_thresholds = [tuned_params[idx + i] for i in range(3)]; idx += 3
	tuned_thresholds1 = [tuned_params[idx + i] for i in range(3)]; idx += 3
	tuned_thresholds2 = [tuned_params[idx + i] for i in range(3)]; idx += 3
	tuned_thresholds3 = [tuned_params[idx + i] for i in range(2)]; idx += 2

	# print results
	print('\n--- Tuned parameters ---')
	print('hidden_layer_weights =', tuned_hidden)
	print('thresholds =', tuned_thresholds)
	print('thresholds1 =', tuned_thresholds1)
	print('thresholds2 =', tuned_thresholds2)
	print('thresholds3 =', tuned_thresholds3)

	# save to json for later reuse
	try:
		import json
		out = {
			'hidden_layer_weights': tuned_hidden,
			'thresholds': tuned_thresholds,
			'thresholds1': tuned_thresholds1,
			'thresholds2': tuned_thresholds2,
			'thresholds3': tuned_thresholds3,
			'total_error': tuned_err
		}
		with open('tuned_params.json', 'w') as f:
			json.dump(out, f, indent=2)
		print('\nSaved tuned parameters to tuned_params.json')
	except Exception as e:
		print('Failed to save tuned params:', e)
