# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 23:51:14 2018

@author: Ketan
"""

def retrieve(name: str):
  
  movie_put = name
  #movie_put = 'Avengers: Age of Ultron'
  dummy_movie = '+'.join(movie_put.split(' '))
  data = {}
  data['Movie'] = movie_put
  
  reference_id = None
  
  source = requests.get('https://www.imdb.com/search/title?title={}&sort=num_votes,desc'.format(dummy_movie)).text
  code = BeautifulSoup(source, 'lxml')
  
  try:
    section = code.find('div', class_= 'lister-item-content')

    reference_id = section.find('a')['href'].split('/')[2]
    
    #link_test = 'https://www.imdb.com/title/{}/?ref_=fn_al_tt_1'.format(reference_id)
    individual_movie_source = requests.get('https://www.imdb.com/title/{}/?ref_=fn_al_tt_1'.format(reference_id)).text
    
    individual_soup = BeautifulSoup(individual_movie_source, 'lxml')
  except:
    print('link not accessible for movie {}'.format(movie_put))
  try:
    column = individual_soup.find_all('div', class_='txt-block')
    for part in column:
      try:
        if part.h4.text == 'Color:':
          color = part.a.text
      except:
        continue
    data['Color'] = color
  except:
    data['Color'] = None
    
  try:
    for part in column:
      try:
        if part.h4.text == 'Budget:':
          budget = part.text
          data['Budget'] = budget.split('$')[1].split('\n')[0]
      except:
        continue
  except:
    data['Budget'] = None
    
  try:
    review_bar = individual_soup.find('div', class_='titleReviewBarItem titleReviewbarItemBorder')
    critic = review_bar.find_all('a')[1].text
    data['Critic'] = critic
  except:
    data['Critic'] = None
    
  try:
    rating = individual_soup.find('span', class_='rating').text
    data['Rating'] = rating
  except:
    data['Rating'] = None
    
  try:
    content_rating = individual_soup.find('div', class_='subtext').text.split('\n')[1].strip()
    data['Content Rating'] = content_rating
  except:
    data['Content Rating'] = None
    
  try:
    for gener in individual_soup.find_all('div', class_='see-more inline canwrap'):
      if gener.h4.text == 'Genres:':
        final_gener = []
        for sample in gener.find_all('a'):
          final_gener.append(sample.text.strip())
    
    genres = ', '.join(i for i in final_gener)
    data['Genres'] = genres
  except:
    data['Genres'] = None
    
  try:
    for star in individual_soup.find_all('div', class_='credit_summary_item'):
      if star.h4.text == 'Stars:':
        final_star=[]
        for sample in star.find_all('a'):
          final_star.append(sample.text.strip())
        final_star.pop()
        
    stars = ', '.join(i for i in final_star)
    data['Star'] = stars
  except:
    data['Star'] = None
   
  try:  
    for director in individual_soup.find_all('div', class_='credit_summary_item'):
      if director.h4.text == 'Director:':
        final_director=[]
        for sample in director.find_all('a'):
          final_director.append(sample.text.strip())
        
    director = ', '.join(i for i in final_director)
    data['Director'] = director
  except:
    data['Director'] = None
    
  try:
    for plots in individual_soup.find_all('div', class_='see-more inline canwrap'):
      if plots.h4.text == 'Plot Keywords:':
        final_plot = []
        for sample in plots.find_all('a'):
          final_plot.append(sample.text.strip())
        final_plot.pop()
    
    plots = ', '.join(i for i in final_plot)
    data['Plots'] = plots
  except:
    data['Plots'] = None
    
  try:
    total_count = individual_soup.find('span', class_='small').text
    data['Total Vote Count'] = total_count
  except:
    data['Total Vote Count'] = None
    
  df_temp = pd.DataFrame(data = data, index = [0], columns=index)
  return df_temp
#  df1 = pd.concat([df1, df_temp])

import pandas as pd
from bs4 import BeautifulSoup
import requests

df = pd.read_json('data.json', orient='records')
df = df[['Movie', 'Production-Budget', 'Domestic Gross', 'Worldwide Gross']]

index = ['Movie', 'Color', 'Critic', 'Rating', 'Content Rating', 'Genres', 'Star', 'Director', 'Plots', 'Total Vote Count', 'Budget']

df1 = pd.DataFrame(columns = index)

for i in df['Movie']:
  df1 = pd.concat([df1, retrieve(i)])
  
df1.to_json('scrap.json', orient='records')
  
final = df1
final.to_json('final.json', orient='records')









      



