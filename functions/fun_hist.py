def fun_hist(x, **kwargs):
    """
    fun_hist.py
    Computes and plots the histogram estimator of a given data vector.
    Supply number of bins via jnum.
    
    If h is supplied, this function computes a centered histogram with
    bandwidth h. 
    
    Inputs:
        x       Data
        **jnum  Number of bins
        **h     Bandwidth        
    
    Dependencies:
        sys
        numpy
        matplotlib.pyplot
    
    """
    import sys
    import numpy as np
    import matplotlib.pyplot as plt
    
    # Construct histogram estimator
    # If h exists
    if kwargs.__contains__("h"):
        if kwargs.__contains__("jnum"): print("If both jnum and h are supplied, override jnum and compute Centered with bandwidth h.")
        h = kwargs.get("h")
        
        # Read data dimensions
        N   = np.shape(x)[0]
        
        x_hist    = np.zeros(N)
        for i in range(N):
            
            x_hist[i] = 1/(N*h) *sum(abs((x - x[i])/h) <= 0.5)
    
        # Plot
        plt.plot(sorted(x), x_hist[np.argsort(x)]) # Plot hist sorted by x
        plt.xlabel('Data')
        plt.ylabel('Centered Histogram')
        return x_hist
    
    # If jnum exists but not h
    elif (kwargs.__contains__	("jnum") & (kwargs.__contains__("h") == 0)):
        jnum = kwargs.get("jnum")
        
        # Read data dimensions
        N   = np.shape(x)[0]
        max = x.max()
        min = x.min()
        
        # Calculate bin width
        h = (max - min) /jnum
        
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
        plt.bar(x, x_hist, align='center')
        plt.xlabel('Data')
        plt.ylabel('Histogram')
        return x_hist

    # If neither exist, abort with error message
    else:
        sys.exit("Not enough inputs. Need either h or jnum.")
