# pip install yfinance fix-yahoo-finance
from pandas_datareader import data as pdr #extract data from internet sources into pandas data frame
import yfinance as yf
import pandas as pd


yf.pdr_override()

#data = pdr.get_data_yahoo("MSFT", start="2010–10–10")
data = pdr.get_data_yahoo("AAPL", start="2017-01-01", end="2017-04-30")
print(data)
