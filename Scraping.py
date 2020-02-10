#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 11:16:50 2020

@author: victorrobert-faille
"""
### Importing necessarry libraries ###

import pandas as pd
import time 
import numpy as np
from bs4 import BeautifulSoup
import requests
import re


###open files ###

#df = pd.read_csv("/Users/victorrobert-faille/Documents/Ironhack/Projects/Project-5/AB_NYC_2019.csv")


##Constant variabes ##

ua = {"user-agent": "Mozilla/5.0"}
url_sights = "https://www.planetware.com/tourist-attractions-/new-york-city-us-ny-nyc.htm"
html = requests.get(url_sights, headers = ua).content
soup = BeautifulSoup(html, "lxml")
url_coordinates = "https://www.latlong.net/search.php?keyword=notre+dame"

###Webscraping ###

##Functions##

def clean_names_sight(x) :
    new_list = []
    for i in x:
        if "|" in i :
            new_list.append((''.join(re.findall('.*?\|', i)).strip('|')))
        else :
            new_list.append(i)
    return new_list


def get_coordinates(x):
    ua = {"user-agent": "Mozilla/5.0"}
    lat=[]
    long = []
    place = []
    
    for i in x:
        place.append(i)
        research = i.replace(" ","+")
        url = f"https://www.latlong.net/search.php?keyword={research}"
        html = requests.get(url, headers = ua).content
        soup = BeautifulSoup(html, "lxml")
        lat.append([j for i in soup.select("td:nth-child(2)") for j in i ])
        long.append([j for i in soup.select("td:nth-child(3)")for j in i ])
        long = ["".join(i) for i in long]
        lat = ["".join(i) for i in lat]


    data = {key : (value1,value2) for (key,value1, value2) in zip(place, lat, long)}
    df_place = pd.DataFrame(data=data)
    return df_place


##Actual scraping##
    
names_sights = [i.text for i in soup.select("p.phcaption")]
names_sight_clean = clean_names_sight(names_sights)
df_place = get_coordinates(names_sight_clean)
df_place = df_place.applymap(lambda x : np.nan if x=="" else x)
df_place.dropna(axis = 1, how = "all", inplace = True)
df_place.to_csv("Distance_sights.csv")

