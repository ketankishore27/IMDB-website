# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 00:44:09 2018

@author: Ketan
"""

# **************************** Trying Web Scraping using BeautifulSoup ****************

# ---------------------------> Importing the required Libraries -----------------------

from bs4 import BeautifulSoup
import requests
import csv

# ----------------------------> Getting the source code for the website ---------------

source = requests.get('http://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())

with open('cms_scrap.csv', 'w') as csv_file:
  csv_writer = csv.writer(csv_file)
  csv_writer.writerow(['Headline','Summary','Video_link'])
  for article in soup.find_all('article'):
    headline = article.header.h2.a.text
    print(article.header.h2.a.text, file = csv_file)
    summary = article.div.p.text
    print(article.div.p.text, file= csv_file)
    for video in article.find_all('iframe', class_='youtube-player'):
      video_id = video['src'].split('/')[4].split('?')[0]
      link = 'https://www.youtube.com/watch?v={}'.format(video_id)
      print('https://www.youtube.com/watch?v={}'.format(video_id),  file= csv_file)
    print()


  