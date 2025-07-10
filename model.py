import numpy as np

training1 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1]
]
training2 = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1]
]
training3 = [
    [1, 1, 0],
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1]
]

answers = [
    0, 0, 0
]

# Hidden layer weights from the image
hidden_layer_weights = [
    # Layer 1
    [
        [0.06, 0.17, 0.12],
        [0.08, 0.33, 0.18],
        [0.15, 0.92, 0.12],
        [0.98, 0.11, 0.20],
    ],
    # Layer 2
    [
        [0.08, 0.91, 0.12],
        [0.29, 0.18, 0.21],
        [0.35, 0.12, 0.22],
        [0.19, 0.97, 0.03],
    ],
    # Layer 3
    [
        [1.00, 0.16, 0.93],
        [0.89, 0.97, 0.11],
        [0.94, 0.12, 0.09],
        [0.04, 0.06, 0.13],
    ]
]

valve_layer_weights = [
	0.97, 0.92, 0.06
]

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Example usage:
# input_matrix: shape (4, 3)  (e.g., J3:L6)
# weight_matrix: shape (4, 3) (e.g., D3:F6)
# bias: scalar (e.g., D15)

def calc_hidden_output(input_matrix, weight_matrix, bias):
    return sigmoid(np.sum(np.multiply(input_matrix, weight_matrix)) + bias)

