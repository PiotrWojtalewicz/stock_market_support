import pandas as pd 
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt


def data (ticker,start_date,end_date,interval):
    company = yf.download(
        tickers= ticker,
        start= start_date,
        end =end_date,
        interval= interval
          )
    if company.empty:
        raise ValueError ("Brak danych dla wybranej spółki")
    if isinstance(company.columns, pd.MultiIndex):
        company.columns = company.columns.get_level_values(0)

    company = company.reset_index()
    company =  company[['Date','Close','Volume','Low','High']]
    return company



