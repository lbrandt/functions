def fun_ecdf(x):
    """
    fun_ecdf.py
    Computes and plots the empirical distribution of a given data vector.
    
    Dependencies:
        numpy
    
    """
    import numpy as np
    import matplotlib.pyplot as plt
    
    # Read data size
    N = np.shape(x)[0]
    
    # Sort values
    x_sort = sorted(x)
    
    # Make steps
    x_ecdf    = np.zeros(N)
    x_ecdf[0] = 1/N
    
    for i in range(1, N):
        x_ecdf[i] = x_ecdf[i-1] + 1/N
    
    
    plt.plot(x_sort, x_ecdf)
    plt.xlabel('Data')
    plt.ylabel('ECDF')
    return x_ecdf
