# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 12:26:59 2021

@author: Aarthi
"""

import yfinance as yf
import streamlit as st
#import pandas as pd
st.write("""
         # Simple Stock Price App
         
         Shown are the stock **closing price** and **volume** of Google!
         
         """)
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start = '2010-8-10', end = '2021-8-10')
# Open  High  Low  Close  Volume Dividends  Stock Splits 

st.write("""
         ## Closing Price
         """)
st.line_chart(tickerDf.Close)
st.write("""
         ## Volume Price
         """)
st.line_chart(tickerDf.Volume) 
#Made with Streamlit
