import numpy as np
import pandas as pd
import yfinance as yf

from pmdarima.arima import auto_arima
from statsmodels.tsa.statespace.sarimax import SARIMAX

def arima_model_summary(tickers):

    results = {}

    for ticker in tickers:

        # Download data
        data = yf.download(
            ticker,
            start="2007-01-01",
            auto_adjust=True,
            progress=False
        )

        if data.empty:
            print(f"No data for {ticker}, skipping.")
            continue

        close = data[["Close"]].copy()
        close.columns = [ticker]
        close.dropna(inplace=True)

        # Log returns
        log_returns = np.log(close).diff().dropna()

        # Model selection
        auto_model = auto_arima(
            log_returns,
            start_p=0,
            d=0,
            start_q=0,
            max_p=3,
            max_q=3,
            trace=False,
            with_intercept=False,
            return_valid_fits=False,
            stepwise=True
        )

        order = auto_model.order

        # Refit using statsmodels for full summary
        sm_model = SARIMAX(
            log_returns.squeeze(),
            order=order,
            trend="n"
        ).fit(disp=False)

        results[ticker] = {
            "order": order,
            "aic": sm_model.aic,
            "bic": sm_model.bic,
            "summary": sm_model.summary()
        }

    return results
  
arima_model_summary(["AMZN", "C"])
