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

from functions.fun_ecdf import fun_ecdf

x_ecdf = fun_ecdf(x)

from functions.fun_hist import fun_hist

x_hist1 = fun_hist(x, jnum = 10)
x_hist2 = fun_hist(x, jnum = 20, h = 2)
x_hist3 = fun_hist(x) # Should abort with error.


# Learning how to use optional arguments
def test_var_kwargs(farg, **kwargs):
    print(farg)
    print(kwargs)
    print(kwargs.keys)
    for key in kwargs:
        print(key, kwargs[key])

def test_fun(farg, **options):
    import sys
    
    print(farg)
    if options.__contains__("h"):
        if options.__contains__	("jnum"): print("Both exist, use h, override jnum")
        h = options.get("h")
        print(h)
    elif (options.__contains__	("jnum") & (options.__contains__("h")==0)):
        jnum = options.get("jnum")
        print(jnum)
    else:
        sys.exit("Not enough inputs. Need either h or jnum.")
    
    print("This is the end.")

test_fun(1)
            


test_var_kwargs(farg=1, myarg2="two", myarg3=3)
