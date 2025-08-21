import math

data1 = [
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
            [0, 1, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 0]
    ],
    [
            [0, 1, 1],
            [1, 0, 1],
            [1, 0, 1],
            [0, 1, 1]
        ]
]

answers1 = [1, 0]

hidden_layer_weights = [[[1.129232765287433, 1.1866511008169895, 1.6734833183986357], [1.2567059595165044, 0.3109369854253213, 0.9330133030567026], [-0.24647429626519515, 1.1042729651030228, 1.5078592160250275], [0.5989446628978993, 1.8295527453234322, -0.3565768164743256]], [[1.0923313617122696, 0.7785330990627175, 0.47619022151831514], [0.30664218084024303, -0.3264719042953889, -0.818345752258789], [1.9226021883644921, 2.118800876099568, 1.1817072909263642], [0.4527231530938149, 0.6876554263166884, -0.17999039033146036]], [[2.1033309728361527, 1.1611365455707403, 1.287210972191818], [1.6573139778645605, 1.9103639219209714, 1.8734303897195868], [1.2147754463608356, -0.9074986960946478, 0.6133934725892878], [-0.12129473797146487, 0.09993384411593727, 0.9470805739780335]]]
thresholds = [0.6008752475060916, -0.3101519488042154, 1.0630634654387299]
thresholds1 = [7.813381869623598, 9.978335145962365, 10.37551426678112]
thresholds2 = [-11.895532541692518, -9.552026607528251, -12.252486659796375]
thresholds3 = [-7.396073875282237, 12.829215752348409]


def sum_of_product(data, weights):
    total = 0.0
    for i in range(len(data)):
        for j in range(len(data[0])):
            # print(data[i][j], "*", weights[i][j])
            total += data[i][j] * weights[i][j]
    return total

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
	
for i in range(len(data1)):
	layer1_1_sumofProduct = sum_of_product(data1[i], hidden_layer_weights[0])
	layer1_2_sumofProduct = sum_of_product(data1[i], hidden_layer_weights[1])
	layer1_3_sumofProduct = sum_of_product(data1[i], hidden_layer_weights[2])
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



	# print("-------------------------")
	誤差Q = SUMXMY2([出力z_1, 出力z_2], answers1)
	print("誤差Q:", 誤差Q)
