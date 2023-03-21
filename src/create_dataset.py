from datetime import datetime, date, timedelta
import yfinance as yf

import numpy as np 
import pandas as pd


def get_datas(start_date, end_date: date.today(), tickers):
    """
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

