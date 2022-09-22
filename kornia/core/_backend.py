import torch
import torch.nn.functional as F

# classes
Tensor = torch.Tensor
Module = torch.nn.Module
Parameter = torch.nn.Parameter

# functions
concatenate = torch.cat
stack = torch.stack
normalize = F.normalize
zeros_like = torch.zeros_like
zeros = torch.zeros

# constructors
as_tensor = torch.as_tensor

# random
rand = torch.rand
