import pandas as pd
import yfinance as yf
from scipy import stats

def shapiro_wilk_returns(y, s=None, e=None):
    # Create an empty DataFrame to hold results
    results = pd.DataFrame(columns=['Test Statistic', 'p-value'], index=y)

    # Loop through each ticker to download data and perform the test
    for ticker in y:
        if s is None and e is None:
            data = yf.download(ticker)
        elif e is None:
            data = yf.download(ticker, start=s)
        elif s is None:
            data = yf.download(ticker, end=e)
        else:
            data = yf.download(ticker, start=s, end=e)

        # Extract the Adjusted Close prices
        if not data.empty:

            # Calculate returns
            returns = data['Adj Close'].dropna().pct_change().dropna()

            # Perform the Shapiro-Wilk test on returns
            stat, p_value = stats.shapiro(returns)

            # Store the results in the DataFrame
            results.loc[ticker] = [stat, p_value]

    return results

shapiro_wilk_returns(["AIG", "UNM"], s="2023-01-01")
