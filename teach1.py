import math

data1 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1]
]

answers1 = [0]

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

thresholds = [0.97, 0.92, 0.94]

def sum_of_productx(data, weights):
    total = 0.0
    for i in range(len(data)):
        for j in range(len(data[0])):
            # print(data[i][j], "*", weights[i][j])
            total += data[i][j] * weights[i][j]
    return total

layer1_sumofProduct = sum_of_product(data1, hidden_layer_weights[0])
layer2_sumofProduct = sum_of_product(data1, hidden_layer_weights[1])
layer3_sumofProduct = sum_of_product(data1, hidden_layer_weights[2])
print("Layer 1 sum of product:", layer1_sumofProduct)
print("Layer 2 sum of product:", layer2_sumofProduct)
print("Layer 3 sum of product:", layer3_sumofProduct)

exp1 = 1/(1+math.exp(-layer1_sumofProduct+thresholds[0]))
exp2 = 1/(1+math.exp(-layer2_sumofProduct+thresholds[1]))
exp3 = 1/(1+math.exp(-layer3_sumofProduct+thresholds[2]))
print("exp1:", exp1)
print("exp2:", exp2)
print("exp3:", exp3)




