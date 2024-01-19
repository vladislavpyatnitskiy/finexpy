import pandas as pd
import yfinance as yf

def MAE(tickers, start_date=None, end_date=None, data=True):
    if data:
        price_data = pd.DataFrame()

        for ticker in tickers:
            if start_date is None and end_date is None:
                price_data[ticker] = yf.download(ticker)['Close']
            elif start_date is not None and end_date is None:
                price_data[ticker] = yf.download(ticker,
                                                 start=start_date)['Close']
            elif start_date is None and end_date is not None:
                price_data[ticker] = yf.download(ticker,
                                                 end=end_date)['Close']
            else:
                price_data[ticker] = yf.download(ticker, start=start_date,
                                                 end=end_date)['Close']
        x = price_data.dropna()

    l = []

    for col in x.columns:
        s = x[col]
        l.append(sum(abs(s - s.mean())) / len(s))

    result = pd.DataFrame({"MAE": l}, index=x.columns)
    return result

mae_result = MAE(["AAPL", "C"], start_date="2020-01-01", data=True) # Test
print(mae_result)
