# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 02:55:16 2018

@author: Ketan
"""

# ************************** Scraping movie data ***************************************

# -------------------------> Importing the libraries -----------------------------------

from bs4 import BeautifulSoup
import requests
import json

# -------------------------> Looping through the requested pages ----------------------

url = 'https://www.the-numbers.com/movie/budgets/all/0'
source = BeautifulSoup(requests.get(url).text, 'lxml')

#final = []
##with open('sample.json', 'w') as data_file:
#count = 0
#data = {}
#for entry in source.find_all('tr'):
##  data = {}
#  for names in entry.find_all('b'):
#    data['movie'] = names.a.text
#  count = count + 1
#  if count%2 == 0:
#    a,b,c,d = entry.find_all('td', class_='data')
#    data['production_budget'] = b.text
#    data['domestic_budget'] = c.text
#    data['worldwide_gross'] = d.text
#    print(data)
#  final.append(data)
##    json.dump(final, data_file, ensure_ascii=False)
  
  
final1 = []
with open('sample.json', 'w') as data_file:
  for i in range(1, 5591, 100):
    url = 'https://www.the-numbers.com/movie/budgets/all/{}'.format(i)
    source = BeautifulSoup(requests.get(url).text, 'lxml')
    
    for entry in source.find_all('tr'):
      data = {}
      if(len(entry)>0):
        for names in entry.find_all('b'):
          data['movie'] = names.a.text
          a,b,c,d = entry.find_all('td', class_='data')
          data['production_budget'] = b.text
          data['domestic_budget'] = c.text
          data['worldwide_gross'] = d.text
          json.dump(data, data_file, ensure_ascii=True)
          print(data)
          final1.append(data)
      else:
        print('Tag is empty')
      
  with open('sample.json', 'w') as data_file:
    json.dump(final1, data_file, ensure_ascii=True)



  

