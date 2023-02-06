class some:
    def __init__(self,x):
        self.x = x
        self.y = x-2

a = some(3)
print(a.y)
import torch
print(torch.get_device(torch.zeros((2,2)).to("cuda")))
