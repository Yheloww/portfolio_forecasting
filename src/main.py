from create_dataset import *
from Port_Optimization import *
from Make_predictions import * 

PORTEFOLIO_1 = ['AAPL','BABA', 'XOM', 'GIS','LLY']
PORTEFOLIO_2= ['TSLA','GOOGL','AMZN','MSFT','META']
DATE = date.today() - timedelta(weeks=52*2)

def main(portefolio : list, date):
    """
    """
    # getting datas from yfinances with date chose and portfolio selected
    get_datas(date, date.today(), portefolio)
    # getting a estimation of the best porfolios
    port_opti()
    # prediction using pycaret 
    portfolio_prediction()
    return


if __name__ == "__main__":
    """
    """
    main(PORTEFOLIO_1, DATE)