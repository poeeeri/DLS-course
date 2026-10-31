from pathlib import Path
import torch
from torch import nn


class Square(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x):
        ctx.save_for_backward(x)
        return x ** 2

    @staticmethod
    def backward(ctx, grad_output):
        (x,) = ctx.saved_tensors
        return 2 * x * grad_output


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Linear(1, 1, bias=False)

        with torch.no_grad():
            self.layer.weight.fill_(2.0)

    def forward(self, x):
        return Square.apply(self.layer(x))


model = Net()
print("Net._modules:", model._modules)
print("Net._parameters:", model._parameters)
print("Linear._parameters:", model.layer._parameters)


x = torch.tensor([[3.0]])
y = model(x)
y.backward()

print("weight dtype:", model.layer.weight.dtype)

model.to(device="cpu", dtype=torch.float64)

print("weight dtype:", model.layer.weight.dtype)