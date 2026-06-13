# Financial Econometrics with Python

Welcome to my Financial Econometrics repository! This project focuses on applying econometric methods and statistical techniques to analyze financial data using Python. It is designed for those interested in understanding and implementing key concepts of financial econometrics.

```
===========Statistical Measures===========
Skewness: -0.3588
Excess Kurtosis: 1.5381

=============== Normality Tests============
                     Statistic       p-value
Shapiro-Wilk          0.984611  7.499876e-08
Kolmogorov-Smirnov    0.034609  2.491430e-01
Jarque-Bera         103.108431  4.076512e-23
D'Agostino-Pearson   49.540468  1.747527e-11

Anderson-Darling Test:
Statistic: 2.095672947810044
Critical values: [0.573 0.653 0.783 0.914 1.087]
Significance levels: [15.  10.   5.   2.5  1. ]
=============================================
```
Table 1. Full output of all Normality tests for XOM stock

```
 Performing stepwise search to minimize aic
 ARIMA(0,0,0)(0,0,0)[0]             : AIC=-22824.966, Time=0.08 sec
 ARIMA(1,0,0)(0,0,0)[0]             : AIC=-22824.600, Time=0.04 sec
 ARIMA(0,0,1)(0,0,0)[0]             : AIC=-22824.717, Time=0.13 sec
 ARIMA(1,0,1)(0,0,0)[0]             : AIC=-22825.046, Time=0.13 sec
 ARIMA(2,0,1)(0,0,0)[0]             : AIC=-22826.297, Time=0.15 sec
 ARIMA(2,0,0)(0,0,0)[0]             : AIC=-22828.276, Time=0.07 sec
 ARIMA(3,0,0)(0,0,0)[0]             : AIC=-22826.292, Time=0.09 sec
 ARIMA(3,0,1)(0,0,0)[0]             : AIC=-22824.291, Time=0.41 sec
 ARIMA(2,0,0)(0,0,0)[0] intercept   : AIC=-22835.862, Time=0.14 sec
 ARIMA(1,0,0)(0,0,0)[0] intercept   : AIC=-22831.533, Time=0.18 sec
 ARIMA(3,0,0)(0,0,0)[0] intercept   : AIC=-22833.861, Time=0.12 sec
 ARIMA(2,0,1)(0,0,0)[0] intercept   : AIC=-22833.861, Time=0.14 sec
 ARIMA(1,0,1)(0,0,0)[0] intercept   : AIC=-22832.390, Time=0.11 sec
 ARIMA(3,0,1)(0,0,0)[0] intercept   : AIC=-22831.861, Time=0.18 sec

Best model:  ARIMA(2,0,0)(0,0,0)[0] intercept
Total fit time: 1.968 seconds

AMZN best model: (2, 0, 0)
Performing stepwise search to minimize aic
 ARIMA(0,0,0)(0,0,0)[0]             : AIC=-19915.345, Time=0.06 sec
 ARIMA(1,0,0)(0,0,0)[0]             : AIC=-19922.556, Time=0.04 sec
 ARIMA(0,0,1)(0,0,0)[0]             : AIC=-19921.663, Time=0.12 sec
 ARIMA(2,0,0)(0,0,0)[0]             : AIC=-19931.685, Time=0.13 sec
 ARIMA(3,0,0)(0,0,0)[0]             : AIC=-19934.445, Time=0.15 sec
 ARIMA(3,0,1)(0,0,0)[0]             : AIC=-19931.993, Time=0.24 sec
 ARIMA(2,0,1)(0,0,0)[0]             : AIC=-19920.057, Time=0.23 sec
 ARIMA(3,0,0)(0,0,0)[0] intercept   : AIC=-19932.626, Time=0.34 sec

Best model:  ARIMA(3,0,0)(0,0,0)[0]          
Total fit time: 1.319 seconds

C best model: (3, 0, 0)
{'AMZN': ARIMA(order=(2, 0, 0), scoring_args={}, suppress_warnings=True), 'C': ARIMA(order=(3, 0, 0), scoring_args={}, suppress_warnings=True,
      with_intercept=False)}
```
Table 2. ARIMA models

```
{'AMZN': {'order': (2, 0, 0), 'aic': -22833.389395128506, 'bic': -22813.90393894689, 'summary': <class 'statsmodels.iolib.summary.Summary'>
"""
                               SARIMAX Results                                
==============================================================================
Dep. Variable:                   AMZN   No. Observations:                 4891
Model:               SARIMAX(2, 0, 0)   Log Likelihood               11419.695
Date:                Sat, 13 Jun 2026   AIC                         -22833.389
Time:                        22:24:16   BIC                         -22813.904
Sample:                             0   HQIC                        -22826.552
                               - 4891                                         
Covariance Type:                  opg                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1         -0.0192      0.009     -2.158      0.031      -0.037      -0.002
ar.L2         -0.0340      0.012     -2.894      0.004      -0.057      -0.011
sigma2         0.0005   4.45e-06    123.459      0.000       0.001       0.001
===================================================================================
Ljung-Box (L1) (Q):                   0.02   Jarque-Bera (JB):             23036.05
Prob(Q):                              0.89   Prob(JB):                         0.00
Heteroskedasticity (H):               0.61   Skew:                             0.65
Prob(H) (two-sided):                  0.00   Kurtosis:                        13.55
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
"""}, 'C': {'order': (3, 0, 0), 'aic': -19938.37792166033, 'bic': -19912.397313418172, 'summary': <class 'statsmodels.iolib.summary.Summary'>
"""
                               SARIMAX Results                                
==============================================================================
Dep. Variable:                      C   No. Observations:                 4891
Model:               SARIMAX(3, 0, 0)   Log Likelihood                9973.189
Date:                Sat, 13 Jun 2026   AIC                         -19938.378
Time:                        22:24:19   BIC                         -19912.397
Sample:                             0   HQIC                        -19929.262
                               - 4891                                         
Covariance Type:                  opg                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1          0.0428      0.005      9.486      0.000       0.034       0.052
ar.L2          0.0490      0.005     10.394      0.000       0.040       0.058
ar.L3         -0.0312      0.005     -6.171      0.000      -0.041      -0.021
sigma2         0.0010   4.95e-06    200.309      0.000       0.001       0.001
===================================================================================
Ljung-Box (L1) (Q):                   0.02   Jarque-Bera (JB):            302477.25
Prob(Q):                              0.88   Prob(JB):                         0.00
Heteroskedasticity (H):               0.26   Skew:                            -0.35
Prob(H) (two-sided):                  0.00   Kurtosis:                        41.52
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
"""}}
```
Table 3. ARIMA summary
