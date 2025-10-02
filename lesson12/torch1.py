import torch

# Initialize parameters with some starting values (these can be changed)
x = torch.tensor(2.0, requires_grad=True)
y = torch.tensor(2.0, requires_grad=True)
a = torch.tensor(2.0, requires_grad=True)

# Set up optimizer (Adam is efficient for this)
optimizer = torch.optim.Adam([x, y, a], lr=0.1)  # lr is learning rate; adjust if needed

# Target value
target = torch.tensor(4.56)

# Optimization loop
for i in range(30):  # More iterations can improve accuracy
    z = x * y + a
    loss = (z - target) ** 2
    print(f"z={x.item():.4f}*{y.item():.4f}+{a.item():.4f}={z.item():.4f} loss={loss.item():.6f}")
    
	# optimizer.zero_grad(): Resets (clears) the gradients of all optimized parameters to zero. 
	# This is necessary because by default, PyTorch accumulates gradients from each backward pass.
    # 将所有参数的梯度清零。因为 PyTorch 默认会累加梯度，所以每次迭代前都需要清零。
    #
	# loss.backward(): Computes the gradients of the loss with respect to each parameter (x, y, a, b) 
	# by backpropagation. 根据损失函数，计算各参数的梯度（即反向传播）。
    #
	# optimizer.step(): Updates the parameters using the computed gradients according to the 
	# optimizer’s algorithm (Adam in this case). 根据计算得到的梯度，使用优化器（这里是 Adam）更新参数的值。
    
    optimizer.zero_grad()  # Reset gradients
    loss.backward()  # Compute gradients
    optimizer.step()  # Update parameters

# Get final values
print(f"Final x: {x.item()}")
print(f"Final y: {y.item()}")
print(f"Final a: {a.item()}")
print(f"Final z: {x.item() * y.item() + a.item()}")

