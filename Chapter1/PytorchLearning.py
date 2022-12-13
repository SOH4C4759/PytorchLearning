import torch

"""x= torch.rand(2,1)
y= torch.rand(2,1)
z= torch.rand(1,2)
a= torch.ones(1,2)
b= torch.zeros(2,1)

print(x)
print(y)
print(z)
print(a)
print(b)

if torch.cuda.is_available():
    x = x.cuda()
    y = y.cuda()
    print(x+y)
else:
    print(torch.cuda.is_available())
    pass"""

"""x = torch.ones(2,2,requires_grad=True)
print(x)"""

"""# numpy多维数组
numpylist ='' # 需要为array序列数据
tenlist= torch.from_numpy(numpylist)
print(tenlist)"""

"""s= torch.tensor([[0.01,0.02]],requires_grad=True)
x = torch.ones(2,2,requires_grad= True)
for i in range(10):
    s= s.mm(x)
z = torch.mean(s)
z.backward()
print(x.grad)
print(s.grad)"""

x = torch.linspace(0,100,1).type(torch.FloatTensor)
rand = torch.randn(100)*10
y = x+ rand

x_train = x[:-10]
x_test = x[-10:]
y_train = y[:-10]
y_test = y[-10:]

import matplotlib.pyplot as plt
plt.figure(figsize=(10,8))

plt.plot(x_train.data.numpy(),y_train.data.numpy(),'o')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()