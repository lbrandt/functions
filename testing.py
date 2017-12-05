# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:33:09 2017

@author: Lennart
"""

# Test
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(seed = 187)
x = np.random.normal(0, 1, 1000)
x.mean()

plt.plot(x)
#

fun_ecdf(x)

jnum = 50
