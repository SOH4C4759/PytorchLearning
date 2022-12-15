import torch
x = torch.rand(5,3)
y = torch.ones(5,3)

q = x.mm(y.t())
print(q)