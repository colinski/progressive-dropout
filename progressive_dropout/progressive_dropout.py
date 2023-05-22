import numpy as np
import torch

class ProgressiveDropout(torch.nn.Module):
    def __init__(self, train_only=True):
        super().__init__()
        self.train_only = train_only
    
    #x has shape: batch_size x num_channels x height x width
    def forward(self, x):
        if not self.training and self.train_only:
            return x
        num_channels = x.shape[1]
        a = np.arange(1, num_channels + 1)
        p = np.ones(a.shape, dtype=np.float32) / num_channels #uniform distribution
        samples = np.random.choice(a=a, p=p, size=x.shape[0]) #random number of channels left
        mask = torch.ones_like(x)
        for i, j in enumerate(samples):
            mask[i, j:] = 0.0
        x = x * mask
        return x
