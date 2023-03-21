import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

from pycaret.time_series import *

from sktime.forecasting.model_selection import SlidingWindowSplitter

def get_datas():
    """
    """
    stocks = pd.read_pickle("./['AAPL', 'BABA', 'XOM', 'GIS', 'LLY'].pkl")
    stocks.index = pd.to_datetime(stocks.index).to_period('B')

    tickers = stocks.columns.tolist()
    return stocks, tickers

def datetime_changes(stocks : pd.DataFrame, ticker : str):
    """
    """
    df = stocks[ticker]
    idx = pd.period_range(min(df.index), max(df.index))
    df.index.symmetric_difference(idx)
    df = df.reindex(idx, fill_value=np.nan)
    df = df.fillna(method = 'ffill')

    return df 

def setup(df : pd.DataFrame, ticker : str ):
    """
    """ 
    exp = TSForecastingExperiment()
    exp.setup(data = df, target=ticker ,coverage=0.90, fold_strategy=SlidingWindowSplitter(fh=np.arange(1,23), window_length=130, step_length=130))
    print(type(exp))
    return exp


def model_selection(exp):
    """
    """
    my_models = ['naive', 'arima','lightgbm_cds_dt','theta']
    best_model = exp.compare_models(include=my_models, sort='rmse')
    print(type(best_model))
    return best_model

def model_tuning(best_model,exp,number:int):
    """
    """
    model_ = exp.create_model(best_model)
    tuned_model = exp.tune_model(model_)
    final_model = exp.finalize_model(tuned_model)
    exp.plot_model(final_model, plot='forecast', data_kwargs={'fh':24})
    plt.show()
    plt.savefig(f'prediction{number}.png')
    return final_model


def portfolio_prediction():
    """
    """
    stocks, tickers = get_datas()
    number = 0
    for ticker in tickers : 
        df = datetime_changes(stocks, ticker)
        exp = setup(df, ticker)
        model = model_selection(exp)
        model_tuning(model,exp,number)
        number +=1

    return 

