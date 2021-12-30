#File: FAANGvsS&P
#   This program graphically displays the S&P 500 and the FAANG stocks since 2010.
#by: Noah Porcelain

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('seaborn')
import yfinance as yf

securities = ['voo', 'fb', 'aapl', 'amzn', 'nflx', 'googl']

df = pd.DataFrame()

today = datetime.now().date().strftime("%Y-%m-%d")

for security in securities:
    df[security] = yf.Ticker(security).history(start="2010-01-01", end=today).Close

plt.figure()
plt.plot(df)
plt.ylabel('Price($)')
plt.xlabel('Year')
plt.show()







