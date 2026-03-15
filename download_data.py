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
    return company



