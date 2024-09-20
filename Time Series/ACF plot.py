import numpy as np
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt

def acfplt(dataframe, log_returns=True): # ACF plot for stock data frames
  
  # Calculate log returns if log_returns is True
  if log_returns:
    dataframe = np.log(dataframe / dataframe.shift(1)).dropna()  # Log returns
  
  for column in dataframe.columns:
    plt.figure(figsize=(10, 6))
    plot_acf(dataframe[column])  
    plt.title(f'Autocorrelation Function (ACF) for {column}')
    plt.show()

acfplt(result) # Test
