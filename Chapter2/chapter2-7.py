import numpy as np
import torch

x_tensor = torch.randn(2,3)
y_numpy = np.random.randn(2,3)

# randn正态分布
# rand 均匀分布

x_numpy = x_tensor.numpy()
y_tensor = torch.from_numpy(y_numpy)