#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:31:26 2020

@author: victorrobert-faille
"""
### Importing necessarry libraries ###

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re


##Constant variables ##

ua = {"user-agent": "Mozilla/5.0"}
url_housing_price = "https://www.theweek.co.uk/99093/london-house-prices-which-boroughs-are-falling-and-which-are-on-the-rise"
html = requests.get(url_housing_price, headers = ua).content
soup = BeautifulSoup(html, "lxml")





