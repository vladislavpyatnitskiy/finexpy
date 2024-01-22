import yfinance as yf
import numpy as np
import pandas as pd

def MSE(tickers, s=None, e=None, data=True, root=True):
    if data:
        price_data = pd.DataFrame()

        for ticker in tickers:
            if s is None and e is None:
                price_data[ticker] = yf.download(ticker)['Close']
            elif s is not None and e is None:
                price_data[ticker] = yf.download(ticker, start=s)['Close']
            elif s is None and e is not None:
                price_data[ticker] = yf.download(ticker, end=e)['Close']
            else:
                price_data[ticker] = yf.download(ticker,start=s,end=e)['Close']
        x = price_data.dropna()

    l = []
    
    for col in x.columns:
        s = x[col] # For each column get RMSE and MSE values
        
        if root is True:
          l.append(np.sqrt(np.mean((s - np.mean(s))**2))) # RMSE values
          
        else:
          l.append(np.mean((s - np.mean(s))**2)) # MSE values
    
    if root is True:
      result = pd.DataFrame({"RMSE": l}, index=x.columns) # RMSE Column Name
      
    else:
      result = pd.DataFrame({"MSE": l}, index=x.columns) # MSE Column Name
      
    return result # Display

print(MSE(["AAPL", "C"], s="2020-01-01", data=True, root=True)) # Test
