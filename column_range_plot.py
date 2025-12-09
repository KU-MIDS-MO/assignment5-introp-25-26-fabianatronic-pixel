import numpy as np
import matplotlib.pyplot as plt

def column_range_plot(A, filename="column_ranges.pdf"):
    A = np.array(A)
    
    if A.ndim != 2:
        return None
    
    n_rows, n_cols = A.shape
    
    ranges = np.zeros (n_cols, dtype = float)
    
    for j in range(n_cols):
        column = A[:, j]
        col_min = column. min()
        col_max = column. max()
        ranges[j] = col_max  - col_min
    
    x_positions = np.arange(n_cols)
    
    plt.figure()
    plt.bar(x_positions, ranges)
    plt.xlabel ("column inndex")
    plt.ylabel("range (max min)")
    plt.title ("column ranges")

    plt.savefig (filename)
    plt.show()
    
    return ranges
         
