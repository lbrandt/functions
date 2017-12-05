def fun_hist(x, jnum):
    """
    fun_hist.py
    Computes and plots the histogram estimator of a given data vector.
    
    Inputs:
        x       Data
        #h       Bin width
        jnum    Number of bins
        
    
    Dependencies:
        numpy
        matplotlib.pyplot
    
    """
    import numpy as np
    import matplotlib.pyplot as plt
    
    # Read data dimensions
    N   = np.shape(x)[0]
    max = x.max()
    min = x.min()
    
    # Calculate bin width
    h = (max - min) /jnum
    
    # Construct histogram estimator
    count     = np.zeros(jnum)
    x_hist    = np.zeros(N)
    
    for j in range(jnum):
        
        # Interval borders
        lowerBound = min + h*j
        upperBound = min + h*(j+1)
        
        # Count observations in current bin
        count[j]   = sum((x >= lowerBound) & (x < upperBound))
        
        # Assign values to bins
        for i in range(N):
            if ((x[i] >= lowerBound) & (x[i] < upperBound)): x_hist[i] = count[j]/(N*h)
        
    
    # Plot
    plt.plot(x, x_hist, 'bo')
    plt.xlabel('Data')
    plt.ylabel('Histogram')
    return x_hist, count
