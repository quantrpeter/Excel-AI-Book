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

hidden_layer_weights = [[[0.5113495872036149, 1.9730905890793906, -1.0193506512464998], [1.3138814740379918, -0.5422814009682525, -0.6541064142160854], [2.0941041362232045, 0.8820002157006396, 1.3487930544121218], [1.8679367065190657, 0.8195051260676144, 0.7412682984532902]], [[1.1980200094246682, 0.33081822992209575, 0.685167057300194], [1.4095103175848012, -0.7102044101299303, 0.8191488141115975], [0.7396281918945664, -0.24978605931574022, 0.05712784132686405], [1.8623110689881086, 0.31162017872442177, 2.155865168842974]], [[0.8320477790622764, -0.5887831053082823, 1.6077780213737292], [1.4562877845792674, 0.07435430639888133, -0.2859710306650384], [2.3036668151236026, 1.9272853370165253, 3.0885133619399396], [0.14664150127756265, 0.09144593941062651, -0.2421630055029666]]]
thresholds = [2.0023024112803482, 1.7491764360146949, 0.0682512510560818]
thresholds1 = [8.797650827959663, 10.282872320778907, 9.065586991033085]
thresholds2 = [-10.405211450375178, -9.873479166230588, -11.621294374816904]
thresholds3 = [-7.957494877968446, 10.46222659884424]

def sum_of_product(data, weights):
	total = 0.0
	for i in range(len(data)):
		for j in range(len(data[0])):
			# print(data[i][j], "*", weights[i][j])
			total += data[i][j] * weights[i][j]
	return total

for i in range(len(data)):
	layer1_1_sumofProduct = sum_of_product(data[i], hidden_layer_weights[0])
	layer1_2_sumofProduct = sum_of_product(data[i], hidden_layer_weights[1])
	layer1_3_sumofProduct = sum_of_product(data[i], hidden_layer_weights[2])
	# print("Layer 1 sum of product:", layer1_1_sumofProduct)
	# print("Layer 2 sum of product:", layer1_2_sumofProduct)
	# print("Layer 3 sum of product:", layer1_3_sumofProduct)

	exp1 = 1/(1+math.exp(-layer1_1_sumofProduct+thresholds[0]))
	exp2 = 1/(1+math.exp(-layer1_2_sumofProduct+thresholds[1]))
	exp3 = 1/(1+math.exp(-layer1_3_sumofProduct+thresholds[2]))
	# print("exp1:", exp1)
	# print("exp2:", exp2)
	# print("exp3:", exp3)

	# print("-------------------------")
	layer2_1_sumofProduct = exp1 * \
		thresholds1[0] + exp2 * thresholds1[1] + exp3 * thresholds1[2]
	出力z_1 = 1/(1+math.exp(-layer2_1_sumofProduct+thresholds3[0]))

	layer2_2_sumofProduct = exp1 * \
		thresholds2[0] + exp2 * thresholds2[1] + exp3 * thresholds2[2]
	出力z_2 = 1/(1+math.exp(-layer2_2_sumofProduct+thresholds3[1]))
	# print("出力z_1:", 出力z_1)
	# print("出力z_2:", 出力z_2)

	# Example usage:
	# =SUMXMY2(J7:K7,J17:K17)
	# SUMXMY2([出力z_1, 出力z_2], [target1, target2])

	def SUMXMY2(array1, array2):
		"""
		Excel SUMXMY2 function: Returns the sum of squares of differences of corresponding values
		Formula: sum((x - y)^2) for each pair of values
		"""
		if len(array1) != len(array2):
			raise ValueError("Arrays must have the same length")

		total = 0
		for i in range(len(array1)):
			diff = array1[i] - array2[i]
			total += diff * diff

		return total

	# print("-------------------------")
	誤差Q = SUMXMY2([出力z_1, 出力z_2], answers1)
	print("誤差Q:", 誤差Q)
