import pandas as pd 
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import download_data as dd

def candle_body_strength(df):
    df = (df['Close'] - df['Low'])/(df['High'] - df['Low'])
    return df