import numpy as np
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
import yfinance as yf
import matplotlib.pyplot as plt

def acfplt(y, s=None, e=None, log_returns=True): # ACF plot
  
  p = pd.DataFrame()  # Create an empty DataFrame

  # Loop for data extraction & Set up statements for start and end dates
  for ticker in y:
    if s is None and e is None:
      # When neither start date nor end date is defined
      data = yf.download(ticker, start="2007-01-01")
    elif e is None:
      data = yf.download(ticker, start=s) # Only start date is defined
    elif s is None:
      data = yf.download(ticker, end=e)  # When only end date is defined
    else:
      # When both start date and end date are defined
      data = yf.download(ticker, start=s, end=e)

    # Extract the Adjusted Close prices and add to the DataFrame
    if not data.empty:
      p[ticker] = data[('Close', f'{ticker}')]
            
  p = p.dropna() # Drop rows with NA values
  
  # Calculate log returns if log_returns is True
  if log_returns:
    p = np.log(p / p.shift(1)).dropna()  # Log returns
  
  for column in p.columns:
    plt.figure(figsize=(10, 6))
    plot_acf(p[column])  
    plt.title(f'Autocorrelation Function (ACF) for {column}')
    plt.show()

acfplt(["XOM", "UNM", "GOOGL", "VIRT"], s = "2023-01-01") # Test
