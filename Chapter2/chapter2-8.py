import torch
x = torch.rand(5,3)
y = torch.ones(5,3)

if torch.cuda.is_available():
    x = x.cuda()
    y = y.cuda()
    print (x+y)
else:
    x = x.cpu()
    y = y.cpu()
    print(x+y)