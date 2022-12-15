import torch
# 动态计算图
x = torch.ones(2,2,requires_grad=True)
print(x)

y = x + 2
print(y.data)
print(y.grad_fn)

z = y*y
print(z.grad_fn)

t = torch.mean(z)
print(t.grad_fn)
# 即t(x) = m(x+2)^2

t.backward()
print(x.grad)
print(y.grad)
print(z.grad)

# dt/dx = x.grad t对x的求导