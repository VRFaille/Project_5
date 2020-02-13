#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 16:49:05 2020

@author: victorrobert-faille
"""

## Importing necessary library ##

import pandas as pd


## Creating the dataframes ##

df = pd.read_csv("/Users/victorrobert-faille/Documents/Ironhack/Projects/Project-5/AirBNB-London.csv")
df_selected_cols = df[['id','name','host_id','host_name','neighbourhood_cleansed','latitude','longitude','market','property_type',\
             'bathrooms','bedrooms','beds','bed_type','amenities','square_feet','price','extra_people','minimum_nights',\
            'number_of_reviews','host_is_superhost', 'accommodates','minimum_nights','maximum_nights']]

## Cleaning ##

# Dealing with NA

df_selected_cols.drop(columns = "square_feet", inplace=True) # 99% of the values were NA --> drop the entire column

# Ajusting values type 

df_selected_cols.price = df_selected_cols.price.map(lambda x : float(x.strip("$").replace(",","")) ) # col price xas turn to float for calculations

# Substituting categorical variables with dummies

df_selected_cols.host_is_superhost = df_selected_cols.host_is_superhost.map(lambda  x : 1 if x=="t" else 0 )

# Droping rows with market != London, assuminng there were scraping mistakes

df_selected_cols.drop(index = df_selected_cols.loc[df_selected_cols["market"]!= "London"].index, inplace = True)

def cat_to_dummies(df,col):# Creating a function to add new dummy column
    for i in set(col):
        df[i]= col.map(lambda x : 1 if x== i else 0)
        
cat_to_dummies(df_selected_cols,df_selected_cols.neighbourhood_cleansed) # Neighbourhood dummy column add 

# Dealing with host id outliers - in C2C perspective (drop the following if you want to study the entire AIRBNB market)

pivot_count_hid = df_selected_cols.pivot_table(index = "host_id", values = "id", aggfunc="count") # Using pivot table to store value_count host_id
lst_hid_to_drop  = (pivot_count_hid.loc[pivot_count_hid.id >20]).index.tolist() # mean = 1,05 , std = 5 , selecting index that has more than 3 times std accomodations
lst_to_drop = df_selected_cols.loc[df_selected_cols.host_id.isin(lst_hid_to_drop)].index.tolist() # matching pivot table index with df index 
df_selected_cols.drop(index = lst_to_drop, inplace = True) # Droping 

# Dealing with price outliers : 

def del_dir_outliers(df, colnum): 
    mean = colnum.mean()
    std = colnum.std()
    lst_outliers = df.loc[(colnum > mean + 3*std) | (colnum < mean - 3*std)].index.tolist()
    df.drop(index = lst_outliers, inplace = True)
    
del_dir_outliers(df_selected_cols, df_selected_cols.price)
df_selected_cols.to_csv("Database.csv")




