#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:29:41 2020

@author: victorrobert-faille
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import random
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


ua = {"user-agent": "Mozilla/5.0"}
x = ['Statue of Liberty', 'Central Park', 'Rockefeller Center ', 'Metropolitan Museum of Art', 'Broadway and the Theater District', 'Empire State Building', '9/11 Memorial and Museum ', 'High Line', 'Times Square', 'Brooklyn Bridge', 'Fifth Avenue', 'Fifth Avenue Map', 'Grand Central Terminal', 'One World Observatory ', 'The Frick Collection ', 'New York Public Library', 'Wall Street ', 'Radio City Music Hall ', "St Patrick's Cathedral ", "New York - St Patrick's Cathedral Map", 'Carnegie Hall', 'Bryant Park']
lat=[]
long = []
place = []

for i in x[:3]:
    place.append(i)
    research = i.replace(" ","+")
    url = f"https://www.latlong.net/search.php?keyword={research}"
    time.sleep(1)
    html = requests.get(url, headers = ua).content
    soup = BeautifulSoup(html, "lxml")
    if lat.append([j for i in soup.select("td:nth-child(2)") for j in i ]) == []:
        
    long.append([j for i in soup.select("td:nth-child(3)")for j in i ])


data = {key : (value1,value2) for (key,value1, value2) in zip(place, lat, long)}
df_place = pd.DataFrame(data=data)
    
#    lat.append([j.text for j in soup.find_all("body > main > div > div.col-8 > table > tbody > tr:nth-child(2) > td:nth-child(2)")])
#    long.append([k.text for k in soup.find_all("body > main > div > div.col-8 > table > tbody > tr:nth-child(2) > td:nth-child(3)")])
#    data = {key : (value1, value2) for (key,value1, value2) in zip(place,lat,long)}
