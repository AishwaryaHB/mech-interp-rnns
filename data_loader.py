import numpy as np
from numpy.linalg import norm, eigvals
from numpy.random import choice, random_sample, normal

import copy

from math import factorial
from itertools import permutations

import torch
from torch.autograd import Variable
from torch.utils.data import DataLoader, TensorDataset

###################################################################################################
###################################################################################################

"""
Create PyTorch dataloaders using numpy data tuples

Parameters:  dataTuple = All information that is to be processed through the dataloader: tuple
             bsize = Batch size: int
             shuffle = Whether or not the data are to be shuffled by the loader: bool

Returns:     loader = Python iterable over the dataset: DataLoader

"""

def makeTensorLoaders(dataTuple,bsize,shuffle):
    ll = len(dataTuple)
    dataTuple = list(dataTuple)

    for ii in range(ll):
        if dataTuple[ii].dtype == 'float64':
            dataTuple[ii] = Variable(torch.from_numpy(dataTuple[ii])).requires_grad_(True)
        else:
            dataTuple[ii] = Variable(torch.from_numpy(dataTuple[ii])).requires_grad_(False)

    dataTuple = tuple(dataTuple)

    tensorData = TensorDataset(*dataTuple)
    loader = DataLoader(tensorData, batch_size=bsize, shuffle=shuffle)

    return loader

###################################################################################################
###################################################################################################