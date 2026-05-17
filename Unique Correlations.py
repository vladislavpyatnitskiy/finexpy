import pandas as pd
import numpy as np
import yfinance as yf

def pairs_column(y, s=None, e=None, details=False): # Correlation pairs
  
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
  
  cor_matrix = p.corr() # Calculate correlation matrix

  # Extract unique pairs and their correlations
  cor_pairs = np.triu_indices_from(cor_matrix, k=1)
  unique_pairs = pd.DataFrame({
    "Security 1": cor_matrix.index[cor_pairs[0]],
    "Security 2": cor_matrix.columns[cor_pairs[1]],
    'Correlation': cor_matrix.values[cor_pairs]
  })
  # Filter out pairs with correlation equal to 1
  filtered_pairs = unique_pairs[unique_pairs['Correlation'] != 1]

  if not details:
    filtered_pairs.reset_index(drop=True, inplace=True)
        
    return filtered_pairs
  else:
    # Descriptive Statistics
    d = pd.DataFrame({
      'Summary': [
        filtered_pairs['Correlation'].min(),
        filtered_pairs['Correlation'].median(),
        filtered_pairs['Correlation'].max(),
        filtered_pairs['Correlation'].mean()
        ]
        }, index=["Min", "Median 50%", "Max", "Mean"])

  return d

pairs_column(["XOM", "UNM", "GOOGL", "VIRT"], s = "2023-01-01", details=False)
