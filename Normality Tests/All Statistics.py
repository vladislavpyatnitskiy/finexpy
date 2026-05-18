import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from scipy import stats

def normal_test(y, s=None, e=None):
  
    p = pd.DataFrame()
    
    for ticker in y:
        if s is None and e is None:
            data = yf.download(ticker, start="2007-01-01", auto_adjust=False)
        elif e is None:
            data = yf.download(ticker, start=s, auto_adjust=False)
        elif s is None:
            data = yf.download(ticker, end=e, auto_adjust=False)
        else:
            data = yf.download(ticker, start=s, end=e, auto_adjust=False)
        
        if not data.empty:
            p[ticker] = data['Close']
    
    prices = p.dropna()
    if prices.empty:
        print("No data retrieved")
        return None
    
    returns = np.log(prices / prices.shift(1)).dropna()
    returns_clean = returns.values.flatten()
    returns_clean = returns_clean[~np.isnan(returns_clean)]
    
    fig, axes = plt.subplots(2, 1, figsize=(12, 10))
    
    axes[0].hist(returns_clean, bins=30, edgecolor='black', alpha=0.7)
    axes[0].set_title("Histogram of Returns")
    axes[0].set_xlabel("Returns")
    axes[0].set_ylabel("Frequency")
    
    stats.probplot(returns_clean, dist="norm", plot=axes[1])
    axes[1].set_title("Q-Q Plot Against Normal Distribution")
    
    plt.tight_layout()
    plt.show()
    
    print("===========Statistical Measures===========")
    print(f"Skewness: {round(stats.skew(returns_clean), 4)}")
    print(f"Excess Kurtosis: {round(stats.kurtosis(returns_clean), 4)}")
    
    shapiro_stat, shapiro_p = stats.shapiro(returns_clean[:5000])
    ks_stat, ks_p = stats.kstest(
      returns_clean, 'norm', args=(returns_clean.mean(), returns_clean.std()))
    jb_stat, jb_p = stats.jarque_bera(returns_clean)
    k2_stat, k2_p = stats.normaltest(returns_clean)
    
    df_tests = pd.DataFrame(
      {
        "Statistic": [shapiro_stat, ks_stat, jb_stat, k2_stat],
        "p-value": [shapiro_p, ks_p, jb_p, k2_p]
        }, 
      index=[
        "Shapiro-Wilk", 
        "Kolmogorov-Smirnov", 
        "Jarque-Bera", 
        "D'Agostino-Pearson"
      ]
    )
    
    print("\n=============== Normality Tests============")
    print(df_tests)
    
    ad = stats.anderson(returns_clean, dist='norm')
    print("\nAnderson-Darling Test:")
    print(f"Statistic: {ad.statistic}")
    print(f"Critical values: {ad.critical_values}")
    print(f"Significance levels: {ad.significance_level}")
    print("=============================================")

normal_test(["XOM"], s="2023-01-01")
