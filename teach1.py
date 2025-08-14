import math

# data1 = [
#     [1, 1, 1],
#     [1, 0, 1],
#     [1, 0, 1],
#     [1, 1, 1]
# ]
data1 = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1]
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


layer1_1_sumofProduct = sum_of_product(data1, hidden_layer_weights[0])
layer1_2_sumofProduct = sum_of_product(data1, hidden_layer_weights[1])
layer1_3_sumofProduct = sum_of_product(data1, hidden_layer_weights[2])
print("Layer 1 sum of product:", layer1_1_sumofProduct)
print("Layer 2 sum of product:", layer1_2_sumofProduct)
print("Layer 3 sum of product:", layer1_3_sumofProduct)


exp1 = 1/(1+math.exp(-layer1_1_sumofProduct+thresholds[0]))
exp2 = 1/(1+math.exp(-layer1_2_sumofProduct+thresholds[1]))
exp3 = 1/(1+math.exp(-layer1_3_sumofProduct+thresholds[2]))
print("exp1:", exp1)
print("exp2:", exp2)
print("exp3:", exp3)

print("-------------------------")
layer2_1_sumofProduct = exp1 * \
    thresholds1[0] + exp2 * thresholds1[1] + exp3 * thresholds1[2]
出力z_1 = 1/(1+math.exp(-layer2_1_sumofProduct+thresholds3[0]))

layer2_2_sumofProduct = exp1 * \
    thresholds2[0] + exp2 * thresholds2[1] + exp3 * thresholds2[2]
出力z_2 = 1/(1+math.exp(-layer2_2_sumofProduct+thresholds3[1]))
print("出力z_1:", 出力z_1)
print("出力z_2:", 出力z_2)

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


print("-------------------------")
誤差Q = SUMXMY2([出力z_1, 出力z_2], answers1)
print("誤差Q:", 誤差Q)
