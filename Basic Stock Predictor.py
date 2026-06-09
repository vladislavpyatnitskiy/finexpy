import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def stock_prediction(y, days=30, size=0.05):
  
    for ticker in y:
        # Download data
        data = yf.download(ticker, start="2007-01-01")
        if data.empty:
            print(f"No data for {ticker}, skipping.")
            continue

        # With auto_adjust=True, Close is a simple column
        close = data[['Close']].copy()
        close.columns = [ticker]
        close.dropna(inplace=True)

        # Predict `days` days into the future
        close['Prediction'] = close[ticker].shift(-days)
        close.dropna(inplace=True)

        # Independent (X) and dependent (Y) datasets
        X = np.array(close[[ticker]])
        Y = np.array(close['Prediction'])

        # Train/test split
        X_train, X_test, y_train, y_test = train_test_split(
          X, Y, test_size=size)

        # Train Linear Regression model
        lr_model = LinearRegression()
        lr_model.fit(X_train, y_train)

        # Predict the last `days` rows (the future window)
        future_X = np.array(close[[ticker]])[-days:]
        future_predictions = lr_model.predict(future_X)

        # Plot historical close price
        plt.figure()
        plt.plot(future_predictions)
        plt.title(ticker)
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.grid(True, linestyle=":", color="grey")
        plt.legend()
        plt.show()

stock_prediction(["AMZN", "C"])
