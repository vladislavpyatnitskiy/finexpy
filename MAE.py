import pandas as pd
import yfinance as yf

def MAE(y, s=None, e=None, data=True):
  
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
    
    p.columns = y
    
    l = []

    for col in p.columns:
        a = p[col]
        l.append(sum(abs(a - a.mean())) / len(a))

    result = pd.DataFrame({"MAE": l}, index=p.columns)
    
    return result

MAE(["AAPL", "C"], s="2020-01-01", data=True) # Test
