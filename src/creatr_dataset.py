from datetime import datetime, date, timedelta
import yfinance as yf

import numpy as np 
import pandas as pd

tickers = ['AAPL','BABA', 'XOM', 'GIS','LLY']


def get_datas(start_date, end_date: date.today(), tickers):
    """
    """
    # download adj close for each tickers
    df = yf.download(tickers,
    start=start_date,
    end = end_date
    )['Adj Close']
    #save the dataframe to pickle file
    df.to_pickle('./tickers21-23')
    
    return print(df.head())

get_datas(date.today() - timedelta(weeks=52*2), date.today(), tickers)