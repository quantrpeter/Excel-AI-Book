import math

# Initial values (you can change these; starting points affect the solution found)
x = 1.0
y = 1.0
a = 1.0

# Hyperparameters
learning_rate = 0.01  # Adjust if convergence is too slow/fast (e.g., try 0.001 or 0.1)
num_iterations = 60  # More iterations for better accuracy
target = 4.56
epsilon = 1e-8  # Small value to prevent log(0) or negative bases

# Optimization loop
for i in range(num_iterations):
    # Ensure a is positive for safe exponentiation and log
    a = max(a, epsilon)
    
    # Compute z
    z = x * y + a
    
    # Compute loss
    loss = (z - target) ** 2
    
    # Compute gradients
    dz = 2 * (z - target)  # Common factor: ∂loss/∂z
    grad_x = dz * x
    grad_y = dz * y
    grad_a = dz * a
    
    # Update parameters
    x -= learning_rate * grad_x
    y -= learning_rate * grad_y
    a -= learning_rate * grad_a
    
    # Optional: Print progress every 1000 iterations
    # if i % 10 == 0:
    print(f"Iteration {i}: loss = {loss:.6f}, z = {z:.6f}")

# Final results
final_z = x * y + a
print(f"\nFinal x: {x:.4f}")
print(f"Final y: {y:.4f}")
print(f"Final a: {a:.4f}")
print(f"Final z: {final_z:.4f}")