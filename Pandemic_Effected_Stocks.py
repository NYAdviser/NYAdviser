#File: Pandemic_Effected_Stocks.py
#   This program graphically displays pandemic-boosted and pandemic-riddled companies in relation to the S&P 500.
#by: Noah Porcelain

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')
import yfinance as yf

print()
print("Covid-19 has impacted many sectors of the economy, in some cases, creating irreversible change to the industry.")
print("The first case of Covid-19 case, in the US, was confirmed on January 20th, 2020, and the FDA approved the first Covid-19 vaccine on August 23rd, 2021.")
print("We will be examining several directly affected companies, and examine their stock price from those critical dates.")
print()

Market = ['voo']
Delta = ['dal']
Exxon = ['xom']
Netflix = ['nflx']
Zoom = ['zm']
Peloton = ['pton']

a = pd.DataFrame()
b = pd.DataFrame()
c = pd.DataFrame()
d = pd.DataFrame()
e = pd.DataFrame()
f = pd.DataFrame()

for security in Market:
    a[security] = yf.Ticker(security).history(start="2020-01-20", end='2021-08-23').Close
for security in Delta:
    b[security] = yf.Ticker(security).history(start="2020-01-20", end='2021-08-23').Close
for security in Exxon:
    c[security] = yf.Ticker(security).history(start="2020-01-20", end='2021-08-23').Close
for security in Netflix:
    d[security] = yf.Ticker(security).history(start="2020-01-20", end='2021-08-23').Close
for security in Zoom:
    e[security] = yf.Ticker(security).history(start="2020-01-20", end='2021-08-23').Close
for security in Peloton:
    f[security] = yf.Ticker(security).history(start="2020-01-20", end='2021-08-23').Close

plt.figure()
plt.plot(a, label='VOO')
plt.plot(b, label='Delta Airlines')
plt.plot(c, label='Exxon Mobile')
plt.plot(d, label='Netflix')
plt.plot(e, label='Zoom')
plt.plot(f, label='Peloton')
plt.legend()
plt.ylabel('Price($)')
plt.xlabel('Year')
plt.title('Pandemic Stock Price History')
plt.show()

startvooprice = 304.43
startdalprice = 60.34
startxomprice = 67.58
startnflxprice = 338.11
startzmprice = 76.73
startptonprice = 32.00

endvooprice = 411.22
enddalprice = 39.21
endxomprice = 54.91
endnflxprice =  553.33
endzmprice = 363.35
endptonprice = 106.59

voopercent = ((endvooprice - startvooprice)/startvooprice)*100
dalpercent = ((enddalprice - startdalprice)/startdalprice)*100
xompercent = ((endxomprice - startxomprice)/startxomprice)*100
nflxpercent = ((endnflxprice - startnflxprice)/startnflxprice)*100
zmpercent = ((endzmprice - startzmprice)/startzmprice)*100
ptonpercent = ((endptonprice - startptonprice)/startptonprice)*100

voo2 = voopercent
dal2 = dalpercent
xom2 = xompercent
nflx2 = nflxpercent
zm2 = zmpercent
pton2 = ptonpercent

print("Over the course of that time span, the market returned", round(voo2,2),"percent.")

if dalpercent <= voopercent:
    print("Covid negatively affected Delta Airlines, and Delta did not outperform the S&P 500. It returned", round(dal2,2),"percent")
else:
    print("Covid positively affected Delta Airlines, and Delta outperformed the S&P 500. It returned", round(dal2,2),"percent")

if xompercent > voopercent:
    print("Covid positively affected Exxon Mobile, and Exxon outperformed the S&P 500. It returned", round(xom2,2),"percent")
else:
    print("Covid negatively affected Exxon Mobile, and Exxon did not outperform the S&P 500. It returned", round(xom2,2),"percent")

if nflxpercent > voopercent:
    print("Covid positively affected Netflix, and Netflix outperformed the S&P 500. It returned", round(nflx2,2),"percent")
else:
    print("Covid negatively affected Netflix, and Netflix did not outperform the S&P 500. It returned", round(nflx2,2),"percent")

if zmpercent > voopercent:
    print("Covid positively affected Zoom Video Communications, and Zoom outperformed the S&P 500. It returned", round(zm2,2),"percent")
else:
    print("Covid negatively affected Zoom Video Communications, and Zoom did not outperform the S&P 500. It returned", round(zm2,2),"percent")

if ptonpercent > voopercent:
    print("Covid positively affected Peloton Interactive, and Peloton outperformed the S&P 500. It returned", round(pton2,2),"percent")
else:
    print("Covid negatively affected PelotonInteractive, and Peloton did not outperform the S&P 500. It returned", round(pton2,2),"percent")
