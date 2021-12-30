#File: MicrosoftDividends.py
#   This program graphically displays Microsoft's historical dividend payments
#by: Noah Porcelain

import matplotlib.pyplot as plt
plt.style.use('seaborn')
import yfinance as yf

msft = yf.Ticker('msft')
stockinfo = msft.info

dividend = msft.dividends
data = dividend.resample('Y').sum()
data = data.reset_index()

data['Year'] = data['Date'].dt.year

plt.figure()
plt.bar(data['Year'], data['Dividends'])
plt.ylabel('Dividend Yield ($)')
plt.xlabel('Year')
plt.title('Microsoft Dividend History')
plt.xlim(2002,2020)
plt.show()


