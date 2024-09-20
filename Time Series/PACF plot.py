import numpy as np
import pandas as pd
from statsmodels.graphics.tsaplots import plot_pacf
import matplotlib.pyplot as plt

def pacfplt(dataframe, log_returns=True): # PACF plot for stock data frames
  
  # Calculate log returns if log_returns is True
  if log_returns:
    dataframe = np.log(dataframe / dataframe.shift(1)).dropna()  # Log returns
  
  for column in dataframe.columns:
    plt.figure(figsize=(10, 6))
    plot_pacf(dataframe[column])  
    plt.title(f'Partial Autocorrelation Function (PACF) for {column}')
    plt.show()

pacfplt(result) # Test
