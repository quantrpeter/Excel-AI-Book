import math
import numpy as np
from scipy.optimize import minimize

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

data1 = [
	[1, 1, 1],
	[1, 0, 1],
	[1, 0, 1],
	[1, 1, 1]
]

answers1 = [1, 0]

# --- Training with optimization ---
def loss(params):
	# Unpack params
	# 3 hidden units, each 4x3 weights = 36, plus 3 thresholds for layer1, 3+3 for layer2 (two sets)
	w = params[:36].reshape((3,4,3))
	t1 = params[36:39]  # thresholds for layer1
	t2_1 = params[39:42]  # thresholds for layer2_1
	t2_2 = params[42:45]  # thresholds for layer2_2

	# Layer 1
	l1 = [sum_of_product(data1, w[i]) for i in range(3)]
	exp = [1/(1+math.exp(-l1[i]+t1[i])) for i in range(3)]

	# Layer 2
	l2_1 = exp[0]*t2_1[0] + exp[1]*t2_1[1] + exp[2]*t2_1[2]
	l2_2 = exp[0]*t2_2[0] + exp[1]*t2_2[1] + exp[2]*t2_2[2]
	out1 = 1/(1+math.exp(-l2_1+1.00))
	out2 = 1/(1+math.exp(-l2_2+0.94))
	return SUMXMY2([out1, out2], answers1)

# Initial guess: flatten original weights and thresholds
init_weights = np.array([
	# 1st hidden unit
	[0.5, 0.5, 0.5],
	[0.5, 0.33, 0.18],
	[0.15, 0.92, 0.12],
	[0.98, 0.11, 0.20],
	# 2nd hidden unit
	[0.5, 0.91, 0.12],
	[0.29, 0.18, 0.21],
	[0.35, 0.12, 0.22],
	[0.19, 0.97, 0.03],
	# 3rd hidden unit
	[0.5, 0.16, 0.93],
	[0.89, 0.97, 0.11],
	[0.94, 0.12, 0.09],
	[0.04, 0.06, 0.13]
]).reshape(-1)
init_t1 = np.array([0.97, 0.92, 0.94])
init_t2_1 = np.array([0.18, 0.92, 0.06])
init_t2_2 = np.array([0.99, 0.10, 0.84])
init_params = np.concatenate([init_weights, init_t1, init_t2_1, init_t2_2])

result = minimize(loss, init_params, method='BFGS')

print("最小誤差Q:", result.fun)
print("最適化されたパラメータ:")
print("hidden_layer_weights:")
print(result.x[:36].reshape((3,4,3)))
print("layer1 thresholds:", result.x[36:39])
print("layer2_1 thresholds:", result.x[39:42])
print("layer2_2 thresholds:", result.x[42:45])
