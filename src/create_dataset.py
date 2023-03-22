from datetime import datetime, date, timedelta
import yfinance as yf

import numpy as np 
import pandas as pd


def get_datas(start_date, end_date: date.today(), tickers :list):
    """
    Get the Adjusted close price from yfinance from today's date to chosen date. And save the pd.dataframe to a pickel file

    Parameters
    ----------
    start_date : the chose date
    end_date : today's date
    tickers : list of tickers

    Returns
    -------
    None

    """
    # download adj close for each tickers
    df = yf.download(tickers,
    start=start_date,
    end = end_date
    )['Adj Close']
    #save the dataframe to pickle file
    cols =df.columns.tolist()
    for col in cols:
        df[col] = pd.to_numeric(df[col])

    df.to_pickle(f'./{tickers}.pkl')
    
    return

