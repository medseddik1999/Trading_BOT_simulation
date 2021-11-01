#!/usr/bin/env python
# coding: utf-8

# il y' a des codes utliser à partir des sites internet comme github 

# In[7]:


import ftx 
import ta 
import time 
import json 
import pandas as pd
from math import *


# In[8]:


Strg='trix'#put trend or trix for statgy 


# #Connecter au sous-compte de trading et importer en dircte les donnes 

# In[13]:


accountName = 'advencedprograming'
pairSymbol = 'XRP/USD'
fiatSymbol = 'USD'
cryptoSymbol = 'XRP'
myTruncate = 4

client = ftx.FtxClient(api_key='fShnnkX96Fs0bevsKNxm1Y4vjeXgf1q39PY342HB',
                   api_secret='-AHMz3a4o3nGn-DUfLu0-0WoI1OIFRkMZDOVuL7l', subaccount_name=accountName)

data = client.get_historical_data(
    market_name=pairSymbol, 
    resolution=3600, 
    limit=650, 
    start_time=float(
    round(time.time()))-650*3600, 
    end_time=float(round(time.time())))
df = pd.DataFrame(data)  


# 

# ## avoir les information sur le portefeuille 

# In[14]:


def getBalance(myclient, coin):
    jsonBalance = myclient.get_balances()
    pandaBalance = pd.DataFrame(jsonBalance)
    if pandaBalance.loc[pandaBalance['coin'] == coin].empty : return 0
    else : return float(pandaBalance.loc[pandaBalance['coin'] == coin]['free'])

def truncate(n, decimals=0):
    r = floor(float(n)*10**decimals)/10**decimals
    return str(r)
    

actualPrice = df['close'].iloc[-1]
fiatAmount = getBalance(client, fiatSymbol)
cryptoAmount = getBalance(client, cryptoSymbol)
print(actualPrice, fiatAmount, cryptoAmount)  


# ## Automatiser les ordres d'achat et vente selon une stratégie données

# ##Trend stratgie 

# In[15]:


df['SMA200'] = ta.trend.sma_indicator(df['close'], 200)
df['SMA600'] = ta.trend.sma_indicator(df['close'], 600)

if Strg == 'trend' : 
   if float(fiatAmount) > 5 and df['SMA200'].iloc[-2] > df['SMA600'].iloc[-2]:## condition d'achat selon la stratigie 
      quantityBuy = truncate(float(fiatAmount)/actualPrice, myTruncate)
      buyOrder = client.place_order(
        market=pairSymbol, 
        side="buy", 
        price=None, 
        size=quantityBuy, 
        type='market')
      print(buyOrder) 
    

   if float(cryptoAmount) > 0.0001 and df['SMA200'].iloc[-2] < df['SMA600'].iloc[-2]: ## pour changer la stratigier 
#faut just changer les condition 
      buyOrder = client.place_order(                    
        market=pairSymbol, 
        side="sell", 
        price=None, 
        size=truncate(cryptoAmount, myTruncate), 
        type='market')
      print(buyOrder) 
   


# ##TRIX stratgy 

# In[16]:


trix_length= 150  ##prametre optimiser à la main de cette stratigie  
trix_signal=2520 ##prametre optimiser  à la main de cette stratigie 

df["TRIX"]=ta.trend.ema_indicator(ta.trend.ema_indicator(ta.trend.ema_indicator(df['close'],window=trix_length),window=trix_length),window=trix_length)  
df["TRIX_PCT"]=df["TRIX"].pct_change()*100  
df["TRIX_singal"]=ta.trend.sma_indicator(df["TRIX_PCT"],trix_signal) 
df["TRIX_histo"]=df["TRIX_PCT"]-df["TRIX_singal"]  
df["stoch_rsi"]=ta.momentum.stochrsi(df["close"] , window=14 ,smooth1=3 ,smooth2=3 )  


# In[17]:




if Strg == 'trix' :
   if float(fiatAmount) > 5 and df['TRIX_histo'].iloc[-2] >0 and df['stoch_rsi'].iloc[-2]<0.8:## condition d'achat selon la stratigie 
      quantityBuy = truncate(float(fiatAmount)/actualPrice, myTruncate)
      buyOrder = client.place_order(
        market=pairSymbol, 
        side="buy", 
        price=None, 
        size=quantityBuy, 
        type='market')
      print(buyOrder)

   if float(cryptoAmount) > 0.0001 and df['TRIX_histo'].iloc[-2] <0 and df['stoch_rsi'].iloc[-2]>0.2: ## pour changer la stratigier 
#faut just changer les condition 
      buyOrder = client.place_order(                    
        market=pairSymbol, 
        side="sell", 
        price=None, 
        size=truncate(cryptoAmount, myTruncate), 
        type='market')
      print(buyOrder)


# In[41]:


with  open ("tito.txt" ,"a+") as f : 
       f.write("hello i work/") 

