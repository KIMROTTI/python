from re import X
import numpy as np
import matplotlib.pylab as plt

def step_function(X):
    return np.array(X>0, dtype = np.int)

x = np.arange(-5.0,5.0,0.1)
y = step_function(x)
print(y)