# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 00:17:55 2018

@author: Ketan
"""

# *************************Scrap Movies using dataframe ********************************

# ------------------------> Getting important LIbraries --------------------------------

import pandas as pd
import requests

# -------------------------> Creating a null dataframe to append -----------------------

index = ['Sl.no', 'Date', 'Movie', 'Production-Budget', 'Domestic Gross', 'Worldwide Gross']
final = pd.DataFrame(columns = index)

# ------------------------> Requesting pages --------------------------------------------

for i in range(1, 5591, 100):
  url = 'https://www.the-numbers.com/movie/budgets/all/{}'.format(i)
  source = requests.get(url).text
    
# ------------------------> Scraping the data into dataframe ----------------------------
    
  df = pd.read_html(source)[0]
  df.dropna(inplace=True)
  df.columns = index
  final = pd.concat([final,df])

# ------------------------> Taking backup -----------------------------------------------
backup = final

# ------------------------> Making the dataframe ready ----------------------------------

final = final.drop(['Sl.no', 'Date'], axis=1)
final.reset_index(inplace=True)

# ------------------------> Converting to Json File -------------------------------------

final.iloc[:, 1:].to_json('data.json', orient='records')







