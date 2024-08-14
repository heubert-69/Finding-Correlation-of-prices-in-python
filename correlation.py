import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf


#only comparing the closing price and plotting to see if theres a correlation
coff = yf.download("KC=F", start="2020-01-01", end="2022-12-31")
USD = yf.download("DXY", start="2016-08-25", end="2022-12-31")

USD = USD.loc[:, "Close"]
coff = coff.loc[:, "Close"]
#Plotting 
plt.scatter(USD, coff)
plt.grid()
plt.title("Correlation of USD Index and a Coffee Futures Contract")
plt.show()

