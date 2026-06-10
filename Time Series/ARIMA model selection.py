import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from pmdarima.arima import auto_arima
from statsmodels.tsa.statespace.sarimax import SARIMAX
import yfinance as yf

def arima_model(tickers):
    results = {}

    for ticker in tickers:
        # Download data
        data = yf.download(ticker, start="2007-01-01", auto_adjust=True)
        if data.empty:
            print(f"No data for {ticker}, skipping.")
            continue

        close = data[["Close"]].copy()
        close.columns = [ticker]
        close.dropna(inplace=True)

        # Compute log returns 
        log_returns = np.log(close).diff().dropna()

        model = auto_arima(
            log_returns,
            start_p=0,
            d=0,          
            start_q=0,
            max_p=3,
            max_q=3,
            trace=True,
            with_intercept=False,
            return_valid_fits=False,  # return single best model
            stepwise=True,
        )

        print(f"\n{ticker} best model: {model.order}")
        results[ticker] = model

    return results  # moved outside the loop

arima_model(["AMZN", "C"])
