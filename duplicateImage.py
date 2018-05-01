from scipy.misc import imread
import numpy as np
import os
path = "<Images directory path>"
dataset = os.listdir(path)
for i in dataset:
    im1 = imread(path + i)
    for j in dataset:
        if i != j:
            im2 = imread(path + j)
            if np.all(im1 - im2 == 0):
                os.remove(path + j)

