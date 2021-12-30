#File: TeslaStockGraph.py
#   This program graphically displays Tesla’s stock price history since 2007.
#by: Noah Porcelain

import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('seaborn')
import yfinance as yf

security = yf.Ticker('tsla')
stockinfo = security.info

today = datetime.now().date().strftime("%Y-%m-%d")

df = security.history(start="2007-01-01", end=today).Close

plt.figure()
plt.plot(df)
plt.ylabel('Price($)')
plt.xlabel('Year')
plt.title('Tesla Stock Price History')
plt.show()









