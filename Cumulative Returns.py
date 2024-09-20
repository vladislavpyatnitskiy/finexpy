import numpy as np

def cmlrets(x): # Calculate cumulative returns for stocks
    
    return np.exp(np.cumsum(np.log(x / x.shift(1)).dropna())) - 1

cmlrets(result)  # Assuming input is a NumPy array or pandas DataFrame
