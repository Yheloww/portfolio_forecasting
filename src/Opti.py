import matplotlib.pyplot as plt
from pypfopt import EfficientFrontier, risk_models, expected_returns,plotting
import pandas as pd
from pypfopt import objective_functions


stocks = pd.read_pickle('../Datas/test.pkl')
cols =stocks.columns.tolist()
for col in cols:
    stocks[col] = pd.to_numeric(stocks[col])

def expected_return(stocks):
    stocks_returns = stocks.pct_change()[1:]
    stocks_returns.head()
    exp_ret = expected_returns.mean_historical_return(stocks)
    stocks.pct_change()[1:].cumsum().plot()
    plt.show()
    return exp_ret

def Cov_matrix(stocks):
    # variance / covariance matrix
    cov_matrix2 = risk_models.sample_cov(stocks)
    plotting.plot_covariance(cov_matrix2, plot_correlation=True);
    plt.show()
    return cov_matrix2

def Portfolio_weights(exp_return, covariance_matrix):
    ef = EfficientFrontier(exp_return, covariance_matrix)
    # optimizing to have less negligible weights 
    ef.add_objective(objective_functions.L2_reg, gamma=0.1)
    w = ef.max_sharpe()
    test = ef.clean_weights()
    names = list(test.keys())
    values = list(test.values())

    plt.bar(range(len(test)), values, tick_label=names)
    plt.show()
    return 

exp_ret = expected_return(stocks)
Cov_matrix = Cov_matrix(stocks)
print(Portfolio_weights(exp_ret,Cov_matrix))