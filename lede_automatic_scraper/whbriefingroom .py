#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


response = requests.get('https://www.whitehouse.gov/briefing-room/')
doc = BeautifulSoup(response.text,'html.parser')


# In[3]:


all_articles = doc.find_all('article')
df = pd.DataFrame()
for article in all_articles:
    title = article.find('a').text.strip()
    ###print (title)
    article_url = article.find('a')['href']
    ##print(article_url)
    article_date = article.find('time').text.strip()
    ##print(article_date)
    d = {}
    print(title)
    print(article_url)
    print(article_date) 
    d['title'] = title
    d['url'] = article_url
    d['article_date'] =  article_date
    df = df.append(d,ignore_index=True)
    
print(df)
    
    


# In[ ]:


paginated_url = 'https://www.whitehouse.gov/briefing-room/'
count = 1

while count <= 999:
    count += 1
    print (count)
    request = requests.get(paginated_url+str(count))
    if request.status_code != 404:
        all_articles = doc.find_all('article')
        df = pd.DataFrame()
        for article in all_articles:
            title = article.find('a').text.strip()
            ###print (title)
            article_url = article.find('a')['href']
            ##print(article_url)
            article_date = article.find('time').text.strip()
            ##print(article_date)
            d = {}
            print(title)
            print(article_url)
            print(article_date) 
            d['title'] = title
            d['url'] = article_url
            d['article_date'] =  article_date
            df = df.append(d,ignore_index=True)
    
    else: 
        df.to_csv('text.csv', index=False)
    


# In[ ]:





# In[ ]:




