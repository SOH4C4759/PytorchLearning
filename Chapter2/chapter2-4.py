import torch
x = torch.rand(5,3)
# 访问张量
print(x[0])
print(x[1,2])
print(x[:,2])