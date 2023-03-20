# loading in modules
import sqlite3
import pandas as pd 
import random
from datetime import date, timedelta
import matplotlib.pyplot as plt
import numpy as np

dbfile = './data.db'

def sqlite_access(dbfile):
    con = sqlite3.connect(dbfile)
    return con

def random_tickers(con):
    cur = con.cursor()
    tickers = cur.execute("SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';").fetchall()
    tickers = tickers[1:]
    choice = random.sample(tickers, 5)
    return choice


def df_per_tickers(ticker, con):
    df = pd.read_sql(f'SELECT  Date,"Adj Close**" fROM {ticker[0]}',
                       con,
                       parse_dates=['Date'], index_col='Date')
     
    start_date = "2020-03-13"
    end_date = "2023-03-13"
    mask = (df.index > start_date) & (df.index <= end_date)
    df2 = df.loc[mask]
    df2 = df2.rename(columns={"Adj Close**": f"{ticker[0]}"})

    return df2 

def complete_df(choice,con):
    final_dataframe = pd.DataFrame()
    for ticker in choice :   
        df2 = df_per_tickers(ticker,con)
        df2 = df2.replace('-', np.nan)
        df2 = df2.dropna()

        if final_dataframe.empty: 
            final_dataframe = df2
        else : 
            final_dataframe = final_dataframe.join(df2)
        
    final_dataframe.to_pickle('./test.pkl')
    print("saved")
    print(final_dataframe)
    return final_dataframe

def plot(df2):
    df2 = pd.read_pickle("../Datas/test.pkl")
    cols =df2.columns.tolist()
    for col in cols:
        df2[col] = pd.to_numeric(df2[col])

    df2.plot()
    plt.show()
    return 


con = sqlite_access(dbfile)
choice = random_tickers(con)
df2 = complete_df(choice,con)
plot(df2)
