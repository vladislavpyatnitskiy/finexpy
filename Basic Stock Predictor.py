import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def stock_prediction(y, days=30, size=0.05):
  
  p = pd.DataFrame()  # Create an empty DataFrame

  # Loop for data extraction & Set up statements for start and end dates
  for ticker in y:
    # When neither start date nor end date is defined
    data = yf.download(ticker)

    # Extract the Adjusted Close prices and add to the DataFrame
    if not data.empty: 
      p[ticker] = data['Adj Close']

    df = p.dropna() # Drop rows with NA values

  df['Prediction'] = df[y].shift(-1 * days)  # Predict 30 days into the future
  df.dropna(inplace=True)
  
  # Create independent (X) and dependent (y) datasets
  X = np.array(df.drop(['Prediction'], 1))
  Y = np.array(df['Prediction'])
  
  # Split the data into training and testing sets
  X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=size)
  
  # Initialize and train the Linear Regression model
  lr_model = LinearRegression()
  lr_model.fit(X_train, y_train)
  
  # Predict stock prices for the test dataset
  predictions = lr_model.predict(X_test)
  
  print(lr_model.predict(df.drop(['Prediction'], 1)[-1 * days:]))
    
stock_prediction(["AMZN"]) # Test
