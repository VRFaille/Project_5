#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 11:16:50 2020

@author: victorrobert-faille
"""
### Importing necessarry libraries ###

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
        time.sleep(1)
        html = requests.get(url, headers = ua).content
        soup = BeautifulSoup(html, "lxml")
        lat.append([j for i in soup.select("td:nth-child(2)") for j in i ])
        long.append([j for i in soup.select("td:nth-child(3)")for j in i ])


    data = {key : (value1,value2) for (key,value1, value2) in zip(place, lat, long)}
    df_place = pd.DataFrame(data=data)
    return df_place


##Actual scraping##
    
names_sights = [i.text for i in soup.select("p.phcaption")]
names_sight_clean = clean_names_sight(names_sights)
df_place = get_coordinates(names_sight_clean)

##Poubelles##

#    browser.get(url_coordinates)
#    search_for_sights = browser.find_element_by_id("place")
#    search_for_sights.send_keys("blabla")
#    search_for_sights.send_keys(Keys.ENTER)
#    time.sleep(2)
#    url_to_scrap = browser.current_url
#    html = requests.get(url_to_scrap, headers = ua).content
#    soup = BeautifulSoup(html, "lxml")
#    lat_long = [i.text for i in soup.select("#latlngspan")]
#    print(lat_long)
#    return lat_long

#regex : .*?\|
#
##Getting longitude and latitude#
#def researching() :
#    browser.get("https://www.abebooks.fr/")
#    patience()
#    Abebooks_SearchBar_Auteur = browser.find_element_by_id("hp-search-author")
#    Abebooks_SearchBar_Auteur.send_keys(str(author_choice))
#    Abebooks_SearchBar_Title = browser.find_element_by_id("hp-search-title")
#    Abebooks_SearchBar_Title.send_keys(str(title_choice))
#    patience()
#    Abebooks_SearchBar_Title.send_keys(Keys.ENTER)
#
#### Cleaning ###
#
#ùdf.reviews_per_month.fillna(0, inplace=True) # if past reviews is na, therefore reviews_per_month should equal 0 
