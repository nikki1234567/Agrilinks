# -*- coding: utf-8 -*-
"""
Created on Tue May  4 10:18:00 2021

@author: nikhi
"""


import requests
import pandas as pd

#place the url of table to extract
url = 'https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=24&Tx_State=UP&Tx_District=0&Tx_Market=0&DateFrom=27-Apr-2021&DateTo=27-Apr-2021&Fr_Date=27-Apr-2021&To_Date=27-Apr-2021&Tx_Trend=0&Tx_CommodityHead=Potato&Tx_StateHead=Uttar+Pradesh&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-2]
print(df)
df.to_csv('Agr_data.csv')